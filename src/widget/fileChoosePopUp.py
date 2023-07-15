# -*- coding: utf-8 -*-
import os

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.clock import Clock

from util import util
from constant.systemconstant import KIVY_CURRENT_DIR
from constant.messeges import TITLE_DIR_SELECT
import win32timezone

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'widget\\fileChoosePopUp.kv'))


class FileChoosePopUp(Popup):
    def __init__(self, selectDir,**kwargs):
        super().__init__(**kwargs)
        self.popupEvent = PopupEvent()
        self.title = TITLE_DIR_SELECT
        self.content = FileChoosePopUpWidget(selectDir)
        self.selectDir = None

    def closeFileChoosePopUp(self, selectDir):
        self.selectDir = selectDir
        self.dismiss()

    def on_dismiss(self):
        self.popupEvent.dispatch_popup_closed(self.selectDir)


class FileChoosePopUpWidget(BoxLayout):
    def __init__(self, selectDir,**kwargs):
        super().__init__(**kwargs)
        self.selectDir = selectDir
        Clock.schedule_once(self._after_kv_applied)

    def _after_kv_applied(self, dt):
        self.ids.fc.path = self.selectDir
    
    def bottunChoose(self, **kwargs):
        selectDir = self.selectDir
        if len(self.ids.fc.selection) != 0:
            selectDir = self.ids.fc.selection[0]
        self.parent.parent.parent.closeFileChoosePopUp(selectDir)
    
    def isDir(self, dirname, filename):
        return os.path.isdir(os.path.join(dirname, filename))

    def dismiss(self):
        self.parent.parent.parent.closeFileChoosePopUp(self.selectDir)


class PopupEvent(EventDispatcher):
    def __init__(self):
        self.register_event_type('on_popup_closed')

    def dispatch_popup_closed(self, parameter):
        self.dispatch('on_popup_closed', parameter)

    def on_popup_closed(self, parameter):
        pass

