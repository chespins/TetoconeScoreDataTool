# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from util import util

Builder.load_file(util.find_data_file('.\\kvfile\\menu.kv'))


class MenuScreen(Screen):
    pass


if __name__ == '__main__':
    pass
