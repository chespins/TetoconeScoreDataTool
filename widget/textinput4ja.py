'''
textinput4ja.py
TextInput class for Japanese
Tested on macOS Monterey 12.6 and Android emulator api=33 using Kivy 2.1.0
MIT License
Copyright ©︎ 2022 bu
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from kivy.utils import platform
from kivy.uix.textinput import TextInput, FL_IS_LINEBREAK, FL_IS_WORDBREAK
from kivy.properties import StringProperty, ListProperty, BooleanProperty, NumericProperty
from kivy.core.window import Window
from kivy.base import EventLoop
import copy
import re
from kivy.clock import Clock
# Androidでの言語設定を取得
# if platform == 'android':
#     from jnius import autoclass
#     Locale = autoclass('java.util.Locale')
#override TextInput
class TextInput_JA(TextInput):
    __events__ = ('on_text_validate', 'on_double_tap', 'on_triple_tap',
                  'on_quad_touch')
    _resolved_base_dir = None #よくわからん
    is_JP_ime_on = BooleanProperty() #日本語IMEの起動状態のフラグ
    is_lang_en = BooleanProperty()   #言語設定がEnglishかどうかのフラグ
    is_lang_ja = BooleanProperty()   #言語設定が日本語かどうかのフラグ
    is_android_ime_on = BooleanProperty() #androidでのIMEの起動状態のフラグ
    lines = ListProperty() #TextInputに入力されているテキストの行ごとのリスト
    alltext= StringProperty() #TextInputに入力済みの全テキスト
    add_to_end = BooleanProperty() #テキストの追加が入力済みテキストの末端への追加かどうかのフラグ
    del_by_bkspc = BooleanProperty()  #backspaceを押してテキストを消去したかどうかのフラグ
    _text_confirmed = BooleanProperty() #テキスト入力を確定したかどうかのフラグ
    _justbreaklined = BooleanProperty()  #テキスト入力して直後に改行されたかどうかのフラグ
    _row_start_of_typing = NumericProperty() #テキスト入力を始めた行を格納
    _ci_start_of_typing = NumericProperty() #テキスト入力を始めたときのcursor indexを格納
    def __init__(self, **kwargs):
        super(TextInput_JA, self).__init__(**kwargs)
        self.is_JP_ime_on = False #初期設定はFalseとする
        if platform == 'android':
            #言語設定を取得してフラグを立てておく
            if Locale.getDefault().getLanguage() == 'en':
                self.is_lang_en = True
                self.is_lang_ja = False
            elif Locale.getDefault().getLanguage() == 'ja':
                self.is_lang_en = False
                self.is_lang_ja = True
            else:
                self.is_lang_en = False
                self.is_lang_ja = False
        self.is_android_ime_on = False
        self.gcursor_index = self.cursor_index()
        self.lines = ['','']
        self.alltext = ''
        self.add_to_end = True
        self.del_by_bkspc = False
        self._text_confirmed = False
        self._justbreaklined = False
        self._row_start_of_typing = 0
        self._ci_start_of_typing = 0
    def do_backspace(self, from_undo=False, mode='bkspc'):
        '''Do backspace operation from the current cursor position.
        This action might do several things:
            - removing the current selection if available.
            - removing the previous char and move the cursor back.
            - do nothing, if we are at the start.
        '''
        # IME system handles its own backspaces
        #元のコードは if self._ime_composition:  となっていたが、これだとbackspaceが効かなくなってしまっていたので改良。
        #androidの場合はreadonlyの時だけreturn, android以外の時はis_JP_ime_onのときもreturn
        if platform == 'android':
            if self.readonly:
                return
        else:
            if self.readonly or self.is_JP_ime_on:
                return
        self.del_by_bkspc = True
        #以下、print文以外はオリジナルのコードのまま
        col, row = self.cursor
        _lines = self._lines
        _lines_flags = self._lines_flags
        text = _lines[row]
        cursor_index = self.cursor_index()
        if col == 0 and row == 0:
            return
        start = row
        if col == 0:
            if _lines_flags[row] == FL_IS_LINEBREAK:
                substring = u'\n'
                new_text = _lines[row - 1] + text
            else:
                substring = _lines[row - 1][-1] if len(_lines[row - 1]) > 0 \
                    else u''
                new_text = _lines[row - 1][:-1] + text
            self._set_line_text(row - 1, new_text)
            self._delete_line(row)
            start = row - 1
        else:
            # ch = text[col-1] 
            substring = text[col - 1]
            new_text = text[:col - 1] + text[col:]
            self._set_line_text(row, new_text)
        # refresh just the current line instead of the whole text
        start, finish, lines, lineflags, len_lines = (
            self._get_line_from_cursor(start, new_text)
        )
        self._refresh_text_from_property(
            'insert' if col == 0 else 'del', start, finish,
            lines, lineflags, len_lines
        )
        self.cursor = self.get_cursor_from_index(cursor_index - 1)
        # handle undo and redo
        self._set_unredo_bkspc(
            cursor_index,
            cursor_index - 1,
            substring, from_undo, mode)
    # current IME composition in progress by the IME system, or '' if nothing
    _ime_composition = StringProperty('')
    # cursor position of last IME event
    _ime_cursor = ListProperty(None, allownone=True)
    def window_on_textedit(self, window, ime_input):
        #android用
        if platform == 'android':
            text_lines = self._lines or ['']        #text入力済み内容を保持
            self.is_android_ime_on = True           #window_on_textedit実行中のときはTrueになるように設定
            gcc, gcr = copy.deepcopy(self.cursor)   #カーソル位置を保持
            ci = self.cursor_index()                #カーソルインデックスを保持
            #新たに入力を始めたときの行とカーソルインデックスを保持
            if self._text_confirmed:
                self._row_start_of_typing = self.cursor[1]
                self._ci_start_of_typing = self.cursor_index()
            #_ime_compositionを保持しているときとそうでないときで処理を分ける
            if self._ime_composition:
                pcc, pcr = self._ime_cursor     #入力中のテキストのカーソル位置を保持
                cc,cr = self.cursor             #カーソル位置を保持
                #改行がなかった場合はcr == pcrとなる。その場合はtext_linesで現在の行のpcrを指定する
                if cr == pcr:
                    text = text_lines[pcr]
                #改行があった場合はcr != pcrとなる。その場合はtext_linesで元の行pcrの1つ前の行を指定する
                #ただし、enterキーを押して改行された場合はpcrの行を指定する
                elif cr != pcr and self._justbreaklined:
                    text = text_lines[pcr]
                else:
                    text = text_lines[pcr-1]
                len_ime = len(self._ime_composition) #_ime_compositionの長さを格納
                #text入力中の未確定部分において改行が含まれているか否かによって処理を分ける
                #改行なし(たぶん)
                if text[pcc - len_ime:pcc] == self._ime_composition:  # always?
                    #さらに、途中挿入か末端への追加かで条件分岐する
                    #textがime_inputより長く、text[cc:]が存在する、または以降の行が存在する =&gt; 途中挿入中ということ
                    if len(text) > len(ime_input) and len(text[cc:]) != 0 or len(text_lines[cr:]) > 1:
                        #末端への追加では無い。
                        self.add_to_end = False
                    else:
                        self.add_to_end = True #末端への追加なのでフラグを立てる
                    ci = self.cursor_index() #カーソルインデックスを格納しておく
                    #textをrefreshする。ここのrefreshでは行にpcr, テキストにtextを使う
                    self._refresh_text_from_property(
                        "insert",
                        *self._get_line_from_cursor(pcr, text)
                    )
                    #カーソル位置をrefreshする
                    self.cursor = self.get_cursor_from_index(ci)
                #改行あり（たぶん）
                else:
                    ci = self.cursor_index() #カーソルインデックスを格納しておく
                    #途中挿入か末端への追加かで条件分岐させる。len(text)とlen(ime_input)との比較を基準にする。
                    if len(text) > len(ime_input):
                        self.add_to_end = False #末端への追加では無い
                        alltext = copy.deepcopy(self.text) #sel.text全部を格納しておく
                        diff_ime_input = ime_input[len(alltext[ci:]):] #ime_inputとの差分を取得
                        diff_alltext = alltext[ci:] #alltextの差分を取得
                        self.add_to_end = False #末端への追加では無いのでFalseにしておく
                        #ただし、backspaceによって len(text) &gt; len(ime_input)になった時とそうでないときで処理を分ける必要がある
                        if self.del_by_bkspc == False:
                            #テキストを挿入中
                            #text全体を更新する
                            self.text = alltext[:ci - len(self._ime_composition)] + ime_input + alltext[ci:]
                            #カーソル位置を更新する
                            self.cursor = self.get_cursor_from_index(ci - len(self._ime_composition))
                        else:
                            #backspaceでテキストを削除中
                            #text全体を更新する
                            self.text = self.text[:ci - 1] + self.text[ci:]
                            #カーソル位置を更新する
                            self.cursor = self.get_cursor_from_index(ci - len(self._ime_composition))
                    else:
                        self.add_to_end = True #末端追加なのでフラグを立てる
                        #テキストをリフレッシュする
                        self._refresh_text_from_property(
                            "insert",
                            *self._get_line_from_cursor(self.cursor[1], text)
                        )
                        #カーソル位置をリフレッシュする
                        self.cursor = self.get_cursor_from_index(ci - len_ime)
                    #refreshをここでも実施。行はpcr, テキストはtextを使う
                    self._refresh_text_from_property(
                        "insert",
                        *self._get_line_from_cursor(pcr, text)
                    )
                    #カーソル位置をリフレッシュ
                    self.cursor = self.get_cursor_from_index(ci)
            if ime_input:
                #_selectionがある時は削除
                if self._selection:
                    self.delete_selection()
                cc, cr = self.cursor #カーソル位置を格納
                #_ime_compositionがあるときとない時で処理を分ける
                if self._ime_composition:
                    if cr == pcr:
                        text = text_lines[cr]
                        #テキスト入力が確定前かどうかで切り分ける必要性があるので確認しておく
                        #日本語入力の場合 、子音が入力されたときに改行され、母音が入力されたら改行なしの状態になるケースがあり、
                        #その場合はcr == pcr かつ text[pcc - len_ime:pcc] != self._ime_compositionの状態になっている。
                        #そのためここで分岐を入れて処理を分ける
                        if text[pcc - len_ime:pcc] != self._ime_composition:
                            #カーソル以降にテキストがないときとあるときで途中挿入か末端追加かを分けてフラグを立て直す
                            if len(text[cc:]) != 0:
                                self.add_to_end = False #末端への追加では無い
                            else:
                                self.add_to_end = True #末端への追加である
                            #子音1つ分を削除する。で、ime_inputの最後の文字を入れる
                            new_text = text[:cc-1] + ime_input[len_ime-1:] + text[cc:]
                        #英数字入力の場合、text[pcc - len_ime:pcc] == self._ime_compositionである
                        #日本語入力でも途中挿入はtext[pcc - len_ime:pcc] == self._ime_compositionになる
                        else:
                            #ここで、カーソルが最右端の場合はlen(text[cc:])が0になってしまうので条件分岐する
                            #末端にカーソルがあるときでは無い
                            if len(text[cc:]) != 0:
                                self.add_to_end = False #末端への追加では無い
                            #text[cc:]が存在しないかつ挿入位置が一番右側。かつ以降の行が存在する場合
                            elif len(text[cc:]) == 0 and cc == len(self._lines[cr]) and len(text_lines[cr:]) > 1:
                                self.add_to_end = False #末端への追加では無い
                            #それ以外
                            else:
                                self.add_to_end = True #末端への追加である
                            #入力中テキストの確定前と確定した後で処理を分ける
                            if self._text_confirmed == False:
                                new_text = text[:cc - len(self._ime_composition)] + ime_input + text[cc:]
                            else:
                                #確定後用は
                                new_text = text[:cc] + ime_input + text[cc:]
                        #テキストをnew_textを使ってリフレッシュする
                        self._refresh_text_from_property(
                            "insert", *self._get_line_from_cursor(cr, new_text)
                        )
                    #改行があった場合はcr != pcrとなる。text_linesで元の行のpcr、およびpccを指定するしてtextとする
                    #ただし、enterキーを押して直前に改行されている場合は現在の行のcrおよびccを指定する
                    elif cr != pcr and self._justbreaklined:
                        text = text_lines[cr]
                        new_text = text[:cc] + ime_input + text[cc:]
                        #テキストをリフレッシュ
                        self._refresh_text_from_property(
                            "insert", *self._get_line_from_cursor(cr, new_text)
                        )
                    #enterキーを押しての直前の改行がない場合
                    else:
                        text = text_lines[pcr]
                        new_text = text[:pcc] + ime_input + text[pcc:]
                        #テキストをリフレッシュ
                        self._refresh_text_from_property(
                            "insert", *self._get_line_from_cursor(pcr, new_text)
                        )
                    #カーソル位置のリフレッシュ
                    self.cursor_index()
                    #末端への追加の場合とそうでない場合で処理を分ける
                    if self.add_to_end == True:
                        #入力中の改行の有無で条件分岐。保持しているカーソル行crと現在のカーソル行の比較で検出
                        if cr == self.cursor[1]:
                            #カーソル位置は素直に新規に入力した分移動したものに更新する
                            self.cursor = self.get_cursor_from_index(
                                self.cursor_index() + len(ime_input)
                                )
                        else:
                            #カーソル位置はカーソルインデックスを元に更新する
                            self.cursor = self.get_cursor_from_index(
                                ci
                                )
                    else:
                        #backspaceで消している場合はself._ime_composition[:-1] == ime_inputとなる
                        #これを考慮してカーソル位置を更新する
                        self.cursor = self.get_cursor_from_index(
                            self.cursor_index() + len(ime_input) - len(self._ime_composition)
                            )
                #########################################
                ###   self._ime_compositionがない場合 ###
                #########################################
                #現在のカーソル位置の行の文字列をrefresh
                else:
                    text = text_lines[cr]
                    #行の文字数と入力中テキストの文字数によって途中挿入か末端への追加かのフラグを更新
                    if len(text) > len(ime_input):
                        self.add_to_end = False #末端への追加では無い
                    else:
                        self.add_to_end = True #末端への追加である
                    #言語が英語の時は。 
                    #IME on/offの切り替えが起こるときの処理。必要ない? 
                    if self.is_lang_en:
                        new_text = text[:cc] + ime_input[len(text[:cc]):] + text[cc:]
                    else:
                        new_text = text[:cc] + ime_input + text[cc:]
                    #テキストをリフレッシュ
                    self._refresh_text_from_property(
                        "insert", *self._get_line_from_cursor(cr, new_text)
                    )
                    #カーソル位置を更新
                    self.cursor = self.get_cursor_from_index(
                    self.cursor_index() + len(ime_input)
                    )
            #ime_inputが無い時#back spaceが押されてime_inputが無い場合の処理
            #途中挿入の入力中に、backspaceでime_inputの文字数以上に削除した場合が該当する
            else:
                cc, cr = self.cursor
                ci = self.cursor_index()
                new_text = text[:cc-1] + ime_input + text[cc:]
                #テキストをリフレッシュ
                self._refresh_text_from_property(
                    "insert", *self._get_line_from_cursor(cr, new_text)
                )
                #ime_input文字数を超えてbackspace押した時のカーソル位置を、
                #途中挿入か末端追加かで切り分けて処理
                #末端追加のとき
                if self.add_to_end == True:
                    if new_text == '':
                        #この場合はcr-1行の最後の位置をindexとして使用する
                        self.cursor = self.get_cursor_from_index(
                            len(self.text)
                        )
                    else:
                        self.cursor = self.get_cursor_from_index(
                            self.cursor_index()
                        )
                #途中入力のとき
                else:
                    self.cursor = self.get_cursor_from_index(
                        self.cursor_index() - 1
                    )
                #このケースの時はself.is_android_ime_onをFalseに戻す。不要かもしれない。
                self.is_android_ime_on = False
            #_ime_compositionをime_inputで更新
            self._ime_composition = ime_input
            #_ime_cursorをself.cursorで更新
            self._ime_cursor = self.cursor
            #self._text_confirmed等ををFalseに戻す
            self._text_confirmed = False
            self._justbreaklined = False
            self.del_by_bkspc = False
            self.add_to_end = False
    ########################
    ####  android以外用  ###
    ########################
        else:
            self.gcursor_index = self.cursor_index()
            self.gcursor = self.cursor
            col, row = self.cursor
            _lines = self._lines
            text_lines = self._lines or ['']
            #if self._ime_composition and not ime_input:
            if self._ime_composition:
                pcc, pcr = self._ime_cursor
                #入力開始した行よりも下に行があるかないかでtextに採用する行を分ける
                if len(text_lines) >  pcr:
                    text = text_lines[pcr]
                else:
                    text = text_lines[pcr-1]
                #_ime_compositionの文字数を取得しておく
                len_ime = len(self._ime_composition)
                #改行がない時
                if text[pcc - len_ime:pcc] == self._ime_composition:  # always?
                    #入力行のテキストを更新する
                    remove_old_ime_text = text[:pcc - len_ime] + text[pcc:]
                    ci = self.cursor_index()
                    #ここ検討してスッキリさせる余地あり
                    #入力開始した行が現在のカーソルがある行と一致しているかどうかで処理を分ける
                    if pcr == self.cursor[1]:
                        self._refresh_text_from_property(
                            "insert",
                            *self._get_line_from_cursor(pcr, remove_old_ime_text)
                        )
                    else:
                        self._refresh_text_from_property(
                            "insert",
                            *self._get_line_from_cursor(self.cursor[1], remove_old_ime_text)
                        )
                    #カーソル位置は入力文字数分を戻して更新
                    self.cursor = self.get_cursor_from_index(ci - len_ime)
                    #IME開始直後はself.is_JP_ime_onがFalseなのでその時に入力されているテキストを取得し反映する
                    #保持しているカーソル位置はime_inputで取得しているccだとここでは定義されてないので使えないため、self. gcursorから取ってくる
                    if self.is_JP_ime_on == False:
                        gcc, gcr = self.gcursor
                        new_text = text[:gcc] + text[gcc:]
                        #テキストをリフレッシュ
                        self._refresh_text_from_property(
                            "insert", *self._get_line_from_cursor(gcr, new_text)
                        )
                        #new_textの長さを加味して修正したカーソル位置を更新
                        self.cursor = self.get_cursor_from_index(
                        self.cursor_index() + len(new_text)
                        )
                #改行があるとき
                else:
                    if len(text_lines) >  pcr:
                        text = text_lines[pcr]
                    else:
                        text = text_lines[pcr-1]
                    cc, cr = self.cursor
                    #remove_old_ime_text = ''としたら改行時に余計な文字が付かなくなって正常に動く。なぜかよくわからん。
                    remove_old_ime_text = ''
                    ci = self.cursor_index()
                    if len(text) > len(ime_input):
                        #テキスト全体の取得と差分の取得
                        alltext = copy.deepcopy(self.text)
                        diff_ime_input = ime_input[len(alltext[ci:]):]
                        diff_alltext = alltext[ci:]
                        self.add_to_end = False
                        #テキストの挿入の時はime_input &gt;= self._ime_compositionかつself.del_by_bkspc==Falseになる。
                        #そうでなければ削除操作中。それぞれで処理を分ける
                        if self.del_by_bkspc == False:
                            self.text = alltext[:ci - len(self._ime_composition)] + ime_input + alltext[ci:]
                            self.cursor = self.get_cursor_from_index(ci - len(self._ime_composition))
                        else:
                            self.text = self.text[:ci - 1] + self.text[ci:]
                            self.cursor = self.get_cursor_from_index(ci - len(self._ime_composition))
                    else:
                        self.add_to_end = True #フラグを更新
                        #改行があるかどうかを入力開始行と現在の行の比較で検出し、改行の有無で処理を分ける
                        if pcr == self.cursor[1]:
                            self._refresh_text_from_property(
                                "insert",
                                *self._get_line_from_cursor(pcr, remove_old_ime_text)
                            )
                        else:
                            self._refresh_text_from_property(
                                "insert",
                                *self._get_line_from_cursor(self.cursor[1], remove_old_ime_text)
                            )
                        self.cursor = self.get_cursor_from_index(ci - len_ime)
                    #IME開始直後はself.is_JP_ime_onがFalseなのでその時に入力されているテキストを取得し反映する
                    #カーソル位置はime_inputで取得しているccは定義されてないので使えないためself. gcursorを使う
                    if self.is_JP_ime_on == False:
                        gcc, gcr = self.gcursor
                        new_text = text[:gcc] + text[gcc:] #これでうまくいった。
                        if gcr == self.cursor[1]:
                            self._refresh_text_from_property(
                                "insert", *self._get_line_from_cursor(gcr, new_text)
                            )
                        else:
                            self._refresh_text_from_property(
                                "insert", *self._get_line_from_cursor(self.cursor[1], new_text)
                            )
                        #new_textの長さを加味してカーソル位置を更新
                        self.cursor = self.get_cursor_from_index(
                        self.cursor_index() + len(new_text)
                        )
            if ime_input:
                if self._selection:
                    self.delete_selection()
                #_ime_compositionがあるかどうかで処理を分ける
                if self._ime_composition:
                    #改行しないとき
                    if text[pcc - len_ime:pcc] == self._ime_composition:  # always?
                        cc, cr = self.cursor
                        text = text_lines[cr]
                        #original
                        new_text = text[:cc] + ime_input + text[cc:]
                    #改行するとき new_textをtext(カーソルより前),ime_input, text(カーソルより後ろ)を元にして生成
                    else:
                        #いろいろ取得しておく
                        cc, cr = self.cursor
                        pcc, pcr = self._ime_cursor
                        text = text_lines[cr]
                        alltext = copy.deepcopy(self.text)
                        ci = self.cursor_index()
                        diff_ime_input = ime_input[len(alltext[ci:]):]
                        diff_alltext = alltext[ci:]
                        #末尾への挿入か途中挿入かで切り分け
                        if self.add_to_end == True:
                            #テキストの挿入の時はlen(ime_input) &gt;= len(self._ime_composition)になる。
                            #そうでなければ削除操作中
                            if len(ime_input) >= len(self._ime_composition):
                                new_text = text[:cc] + ime_input + alltext[ci:][len(ime_input)-1:]
                            else:
                                new_text = text[:cc] + ime_input
                        #途中挿入の時
                        else:
                            #テキストの挿入の時はself.del_by_bkspc==Falseになる。
                            #そうでなければ削除操作中
                            if self.del_by_bkspc == False:
                                new_text = text[:cc] + text[cc:]
                            else:
                                new_text = text[:cc] + text[cc:]
                else:
                    cc, cr = self.cursor
                    text = text_lines[cr]
                    #new_textを作成する
                    new_text = text[:cc] + ime_input + text[cc:]
                #リフレッシュする
                self._refresh_text_from_property(
                    "insert", *self._get_line_from_cursor(cr, new_text)
                )
                #カーソル位置の更新
                self.cursor = self.get_cursor_from_index(
                    self.cursor_index() + len(ime_input)
                )
            #_ime_compositionをime_inputで更新
            self._ime_composition = ime_input
            #_ime_cursorを現在のカーソル位置で更新
            self._ime_cursor = self.cursor
            #is_JP_ime_onをTrueに戻す
            self.is_JP_ime_on = True
            #del_by_bkspcをFalseに戻す
            self.del_by_bkspc = False
    def insert_text(self, substring, from_undo=False):
        '''Insert new text at the current cursor position. Override this
        function in order to pre-process text for input validation.
        '''
        _lines = self._lines
        _lines_flags = self._lines_flags
        self.gcursor = self.cursor
        #ここ必要ないかもしれない
        if platform == 'android':
            if substring.isascii() == False:
                self.is_JP_ime_on = True
            else:
                self.is_JP_ime_on = False
        if self.readonly or not substring or not self._lines:
            return
        if isinstance(substring, bytes):
            substring = substring.decode('utf8')
        if self.replace_crlf:
            substring = substring.replace(u'\r\n', u'\n')
        self._hide_handles(EventLoop.window)
        if not from_undo and self.multiline and self.auto_indent \
                and substring == u'\n':
            substring = self._auto_indent(substring)
        mode = self.input_filter
        if mode not in (None, 'int', 'float'):
            substring = mode(substring, from_undo)
            if not substring:
                return
        col, row = self.cursor
        cindex = self.cursor_index()
        text = _lines[row]
        len_str = len(substring)
        #改変ここから
        #ここで末端追加か途中挿入かのフラグを立てておく 必要ないかも
        if len(text[col:]) == 0:
            self.add_to_end = True
        else:
            self.add_to_end = False
        #androidかそうでないかで分ける
        #androidでないとき
        if platform != 'android':
            #改行コードの入力の有無により条件分岐
            if substring == u'\n':
                #IMEがONの時は改行コードを入れずに改行しないようにする。IMEがOFFの時は改行コードを入れて改行する。
                if self.is_JP_ime_on == True:
                    #is_JP_ime_onをFalseに設定
                    self.is_JP_ime_on = False
                    new_text = text[:col] + text[col:]
                else:
                    new_text = text[:col] + u'\n' + text[col:]
                    ##カーソルの表示が一行下になるように更新する
                    Clock.schedule_once(lambda x: self.cursor_update(self.cursor), 0.1)
            else:
                if self.is_JP_ime_on == True:
                    #is_JP_ime_onをFalseに設定
                    self.is_JP_ime_on = False
                    new_text = text[:col] + text[col:]
                else:
                    #ime_compositionとsubstringが同じだったらIMEがOFF(？)に切り替わった直後なので、
                    #生成テキストの重複を避けるためsubstringを使わずにnew_textを生成し、substringと_ime_compositionの内容を消去
                    if self._ime_composition==substring:
                        substring = ''
                        self._ime_composition = ''
                        new_text = text[:col] + text[col:]
                    else:
                        new_text = text[:col] + substring + text[col:]
            if mode is not None:
                if mode == 'int':
                    if not re.match(self._insert_int_pat, new_text):
                        return
                elif mode == 'float':
                    if not re.match(self._insert_float_pat, new_text):
                        return
            self._set_line_text(row, new_text)
            # len_strはsubstringの長さ
            if len_str > 1 or substring == u'\n' or\
                (substring == u' ' and _lines_flags[row] != FL_IS_LINEBREAK) or\
                (row + 1 < len(_lines) and
                 _lines_flags[row + 1] != FL_IS_LINEBREAK) or\
                (self._get_text_width(
                    new_text,
                    self.tab_width,
                    self._label_cached) > (self.width - self.padding[0] -
                                           self.padding[2])):
                # Avoid refreshing text on every keystroke.
                # Allows for faster typing of text when the amount of text in
                # TextInput gets large.
                (
                    start, finish, lines, lines_flags, len_lines
                ) = self._get_line_from_cursor(row, new_text)
                # calling trigger here could lead to wrong cursor positioning
                # and repeating of text when keys are added rapidly in a automated
                # fashion. From Android Keyboard for example.
                self._refresh_text_from_property(
                    'insert', start, finish, lines, lines_flags, len_lines
                )
            #IMEがONで入力した時は
            #cindexの位置(insert_textに入った時のself.cursor.index()の戻り値)よりも
            #後ろに何もついていなければ末尾追加なので、len_str分カーソル位置を移動
            #後ろに文字がついていれば挿入追加なので、カーソル位置はそのまま
            # isalnum()を使って、
            #substringが半角英数字のみ、またはlen(self.text[ciindex:])==0のときはlen_strを追加する。
            #それ以外（つまりIME ONで挿入追加を行った時）はカーソル位置はそのまま
            if substring.isalnum() or len(self.text[cindex:]) == 0:
                self.cursor = self.get_cursor_from_index(cindex + len_str)
            # handle undo and redo
            self._set_unredo_insert(cindex, cindex + len_str, substring, from_undo)
            #is_JP_ime_onをFalseに設定
            self.is_JP_ime_on = False
        #################
        # androidの場合 #
        #################
        else:
            '''Insert new text at the current cursor position. Override this
            function in order to pre-process text for input validation.
            '''
            text_lines = self._lines
            cc, cr = self.cursor
            #末端追加か途中挿入かを判定して処理を分ける
            #textがime_inputより長くて、text[cc:]が存在する。または以降の行が存在する =&gt; ime_inputが無いので使えません
            if len(text[cc:]) != 0:
                self.add_to_end = False #末端への追加では無い
            #text[cc:]が存在しないかつ挿入位置が一番右側だ。かつ以降の行が存在する
            elif len(text[cc:]) == 0 and cc == len(self._lines[cr]) and len(text_lines[cr:]) > 1:
                self.add_to_end = False #末端への追加では無い
            else:
                self.add_to_end = True #末端への追加である
            #substringに改行コードが含まれていない =&gt; 変換が確定。この直後かそうでないかで処理を分ける。
            if u'\n' not in substring:
                self._text_confirmed = True
            else:
                self._justbreaklined = True  #フラグを更新
            #改行コードが含まれている場合。改行コードのみが入力されたときとそれ以外で分ける
            if substring == u'\n':
                new_text = text[:col] + substring + text[col:]
                #下に設定している、[カーソル位置の最終的なリフレッシュ] での分岐2に相当するので、後でリフレッシュされないため、ここでリフレッシュ
                (
                    start, finish, lines, lines_flags, len_lines
                ) = self._get_line_from_cursor(row, new_text)
                # calling trigger here could lead to wrong cursor positioning
                # and repeating of text when keys are added rapidly in a automated
                # fashion. From Android Keyboard for example.
                self._refresh_text_from_property(
                    'insert', start, finish, lines, lines_flags, len_lines
                )
            elif u'\n' in substring and substring != u'\n':
                #この分岐の時も変換後の文字列にリフレッシュする機会がないようなので、ここで実施する。
                new_text = text[:col] + text[col:]
                #このケースの時はself.is_android_ime_onをFalseに戻す
                self.is_android_ime_on = False
            else:
                #substring == self._ime_compositionのときは変換候補からの変換なしで挿入
                # =&gt; len(substring)を引いておく
                #substring == self._ime_compositionではないときは変換候補から選択しての挿入
                # =&gt; len(self._ime_composition)を引いておく
                if substring == self._ime_composition:
                    #substringに改行コードが含まれていない =&gt; 変換が確定。変換直後かそうでないかで切り分ける。
                    if self._text_confirmed:
                        new_text = text[:col] + text[col:]
                        #compositionをリセット
                        self._ime_composition = ''
                        #この分岐の時は変換後の文字にリフレッシュする機会がないようなので、ここで実施する。
                        self._refresh_text_from_property(
                            "insert", *self._get_line_from_cursor(row, new_text)
                        )
                    else:
                        new_text = text[:col - len(substring)] + substring + text[col:]
                else:
                    if self._row_start_of_typing != row:
                        #入力開始行と完了行が異なる場合は、選択された変換候補と、変換前の該当テキスト部分を置換し、全textを取り直してからnew_textを作成
                        self.text = self.text[:cindex-len(self._ime_composition)] + substring + self.text[cindex:]
                        #一連のパラメータも取り直す
                        _lines = self._lines
                        _lines_flags = self._lines_flags
                        self.gcursor = self.cursor
                        text_lines = self._lines
                        cc, cr = self.cursor
                        col, row = self.cursor
                        cindex = self.cursor_index()
                        text = _lines[row]
                        len_str = len(substring)
                        #現在の行のテキストをnew_textに入れる
                        new_text = _lines[row]
                    else:
                        #入力開始行と完了行が同じ場合は、その行のみにおいて、選択された変換候補と変換前の該当テキスト部分を置換してnew_textを作成
                        new_text = text[:col - len(self._ime_composition)] + substring + text[col:]
                    #self._ime_compositionはリセットしておく。
                    #連続で変換候補からの入力になったときの場合にリセットが必要となるため。
                    #リセット前に、最後のカーソル位置調整の段階で使用するself._ime_compositionの文字数を取得しておく。
                    self._ime_composition = ''
                    #この分岐の時は変換後の文字にリフレッシュする機会がないようなので、ここで実施する。
                    self._refresh_text_from_property(
                        "insert", *self._get_line_from_cursor(self.cursor[1], new_text)
                    )
                    #このケースの時はself.is_android_ime_onをFalseに戻す
                    self.is_android_ime_on = False
            if mode is not None:
                if mode == 'int':
                    if not re.match(self._insert_int_pat, new_text):
                        return
                elif mode == 'float':
                    if not re.match(self._insert_float_pat, new_text):
                        return
            #下に記載しているカーソル位置の最終的なリフレッシュの、分岐2および分岐4のケースと改行のみの時は、ここの条件式の処理を回避するようにする
            if substring == u'\n':
                pass
            elif self.add_to_end==True and self.is_android_ime_on==False:
                pass
            elif self.add_to_end==False and self.is_android_ime_on==False:
                pass
            else:
                self._set_line_text(row, new_text)
                if len_str > 1 or substring == u'\n' or\
                    (substring == u' ' and _lines_flags[row] != FL_IS_LINEBREAK) or\
                    (row + 1 < len(_lines) and
                     _lines_flags[row + 1] != FL_IS_LINEBREAK) or\
                    (self._get_text_width(
                        new_text,
                        self.tab_width,
                        self._label_cached) > (self.width - self.padding[0] -
                                               self.padding[2])):
                    # Avoid refreshing text on every keystroke.
                    # Allows for faster typing of text when the amount of text in
                    # TextInput gets large.
                    (
                        start, finish, lines, lines_flags, len_lines
                    ) = self._get_line_from_cursor(row, new_text)
                    # calling trigger here could lead to wrong cursor positioning
                    # and repeating of text when keys are added rapidly in a automated
                    # fashion. From Android Keyboard for example.
                    self._refresh_text_from_property(
                        'insert', start, finish, lines, lines_flags, len_lines
                    )
            ################################################
            #                                              #
            # カーソル位置の最終的なリフレッシュ           #
            #  末尾追加の場合はlen_str分カーソル位置を移動 #
            #  挿入追加の場合は、カーソル位置はそのまま    #
            #                                              #
            ################################################
            #self.add_to_endとself.is_android_ime_onの組み合わせで条件分岐
            if self.add_to_end:
                if self.is_android_ime_on:
                    self.cursor = self.get_cursor_from_index(cindex + len_str)
                else:
                    self.cursor = self.get_cursor_from_index(cindex + len_str)
            else:
                if self.is_android_ime_on:
                    self.cursor = self.get_cursor_from_index(cindex)
                else:
                    #両方ともFalseであれば
                    #(途中挿入でテキスト入力中かつ変換候補から選択しているケース) 、
                    #カーソル位置をテキスト挿入後の位置になるように調整する。
                    self.cursor = self.get_cursor_from_index(self._ci_start_of_typing + len_str)
                    self._ci_start_of_typing = self.cursor_index()
            # handle undo and redo
            self._set_unredo_insert(cindex, cindex + len_str, substring, from_undo)
            self.is_android_ime_on = False
    #androidでない場合は、IMEがONの時にテキストボックス中でのカーソル移動を無効にする
    def do_cursor_movement(self, action, control=False, alt=False):
        if platform == 'android':
            TextInput.do_cursor_movement(self, action, control=False, alt=False)
        else:
            if self.is_JP_ime_on:
                return
            else:
                TextInput.do_cursor_movement(self, action, control=False, alt=False)
    #  on_focusについて #
    # - androidでないとき 
    #textinputをdefocusしたときにis_JP_ime_onをFalseに変更する。
    #これによりIME入力中にdefocusになってもfocusが復帰した時にbackspaceが効く
    #また、defocusしたときはself._ime_compositionをリセットしておき、次にfocusしたときの入力に影響がないようにする
    # - androidのとき 
    #input_typeを有するインスタンス(つまりTextInput)をfocusした場合、
    #言語設定が日本語のときはinput_typeを'text'にする。=&gt; 日本語入力を受け付けるようになる。
    #言語設定が日本語以外ではinput_typeを'null'にする。=&gt; English入力のみを受け付けるようになる（ただしGboardの入力予測などが使えない）
    def on_focus(self, instance, value):
        if value:
            if hasattr(instance, 'input_type'):
                if self.is_lang_ja == True:
                    self.input_type = 'text'
                else:
                    self.input_type ='null'
        else:
            self.is_JP_ime_on = False
            self._ime_composition = ''

    #画面でのカーソル表示位置のupdate用        
    def cursor_update(self, cursornow):
        self.cursor = cursornow[0], cursornow[1]+1
        return self.cursor
        
if __name__ == '__main__':
    pass
