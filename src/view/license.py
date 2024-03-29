# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from util import util
from constant.systemconstant import LIBRARY_LICENSE_DIR
from constant.systemconstant import KIVY_CURRENT_DIR


Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'license.kv'))


class LicenseScreen(Screen):

    def __init__(self, **kwargs):
        super(LicenseScreen, self).__init__(**kwargs)
        self.ids.Font.text = util.readFileStr(LIBRARY_LICENSE_DIR + 'FONT-LICENSE')
        self.ids.kivylicense.text = util.readFileStr(LIBRARY_LICENSE_DIR + 'kivy-LICENSE')
        self.ids.requests.text = util.readFileStr(LIBRARY_LICENSE_DIR + 'requests-LICENSE')

    def on_leave(self, *args):
        self.manager.remove_widget(self)
        super().on_leave(*args)


if __name__ == '__main__':
    pass
