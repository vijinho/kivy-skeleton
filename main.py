# -*- coding: utf-8 -*-
'''
Skeleton GUI
============

An App

This app is written in Python using the Kivy library for cross-platform support (Android, IOS, Windows, Linux, Mac OSX).  See http://kivy.org/docs/guide/packaging.html for instructions on packaging the application for the different platforms.
'''
__title__ = 'Skeleton'
__version__ = '0.0.0'
__author__ = 'vijay.mahrra@gmail.com'

import kivy
kivy.require('1.8.0')
from kivy import platform
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.factory import Factory
from kivy.core.text import LabelBase
#from kivy.core.clipboard import Clipboard
#from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock

import os
import shutil
import imghdr
import random
import re
import time
import json
from peewee import *
#from models import


class AppError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MyBoxLayout(BoxLayout):
    pass


class MyGridLayout(GridLayout):
    pass


class MyLabel(Label):
    pass

class MyScreenManager(ScreenManager):
    """Set the background image for the app screens"""
    background_image = ObjectProperty(
        Image(
            source='assets/img/bg/background.png'))


class MyImage(Image):
    """Some extensions to the default image class"""
    def __init__(self, **kwargs):
        super(MyImage, self).__init__()

    def texture_width(self):
        """Return the actual width of the loaded image source (texture)"""
        return self.texture.size[0]

    def texture_height(self):
        """Return the actual height of the loaded image source (texture)"""
        return self.texture.size[1]

    def rescale(self, width, height):
        """
        Resize the image to fit the given dimensions, zooming in or out if
        needed without losing the aspect ratio
        :param width: target width
        :param height: target height
        :return: new dimensions as a tuple (width, height)
        """
        ratio = 0.0
        new_width = 0.0
        new_height = 0.0

        target_width = float(width)
        target_height = float(height)

        image_width = float(self.texture_width())
        image_height = float(self.texture_height())

        ratio = target_width / image_width
        new_width = image_width * ratio
        new_height = image_height * ratio

        if (new_height < target_height):
            ratio = target_height / new_height
            new_height *= ratio
            new_width *= ratio

        if new_width > 0 and new_height > 0:
            self.width = new_width
            self.height = new_height

        return (new_width, new_height)


class MyButton(Button):

    """
    Button with a possibility to change the color on on_press (similar to background_down in normal Button widget)
    and also the background image
    """
    background_image = ObjectProperty(Image(source='assets/img/pixel.png'))
    background_color_normal = ListProperty([0.5, 0.5, 0.5, 0.5])
    background_color_down = ListProperty([0.9, 0.9, 0.9, 0.9])

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.background_color = self.background_color_normal

    def on_press(self):
        self.background_color = self.background_color_down

    def on_release(self):
        self.background_color = self.background_color_normal


class ImageClickable(ButtonBehavior, MyImage):
    """An image which acts like a button"""
    source_up = ObjectProperty(Image(source='assets/img/pixel.png'))
    source_down = ObjectProperty(Image(source='assets/img/pixel.png'))

    def __init__(self, **kwargs):
        super(ImageClickable, self).__init__(**kwargs)
        self.source = 'assets/img/pixel.png'

    def on_press(self):
        self.source = self.source_down

    def on_release(self):
        self.source = self.source_up


class Notify(ButtonBehavior, BoxLayout):
    """Display a floating user notification on the current screen"""
    msg = StringProperty()
    icon = StringProperty()

    def __init__(self, **kwargs):
        super(Notify, self).__init__()
        self.type = ''
        self.text = ''

    def message(self, msg_type, msg):
        """Show the message using an icon named after the given type"""
        self.msg_type = msg_type
        self.msg = msg
        self.icon = 'assets/img/icons/notify/' + msg_type + '.png'


class FormTextInput(TextInput):
    """TextInput which checks against a regexp and length of input"""
    max_chars = 255
    valid_chars = ''

    def insert_text(self, substring, from_undo=False):
        """Check against regexp of characters"""
        if len(self.valid_chars) > 0:
            valid_chars = '[^' + self.valid_chars + ']'
            pat = re.compile(valid_chars)
            s = re.sub(valid_chars, '', substring)
        else:
            s = substring
        super(FormTextInput, self).insert_text(s, from_undo=from_undo)
        self.validate(self.max_chars)

    def validate(self, max_chars):
        """Check the string length of text input"""
        if int(max_chars) <= 0:
            max_chars = self.max_chars
        s = self.text
        self.text = (s[:max_chars]) if len(s) > max_chars else s


class Main(MyScreenManager):
    backup_results = ObjectProperty()

    def __init__(self, **kwargs):
        self.transition = NoTransition()
        super(Main, self).__init__()


class MainApp(App):
    pixel = 'assets/img/pixel.png'
    use_kivy_settings = False
    folder = StringProperty()
    data_folder = StringProperty()
    notifications_queue = []

    def __init__(self):
        self.title = 'Skeleton'
        self.icon = 'assets/img/icon.png'
        self.folder = os.path.dirname(os.path.abspath(__file__))
        # make sure android uses the /sdcard folder instead of data/
        if platform == 'android':
            path = '/sdcard/skeleton/'
#            if not os.path.exists(path):
#                os.mkdir(path)
#            for f in copyfiles:
#                shutil.copyfile(os.path.join('data', f), os.path.join(path, f))
#            self.data_folder = path
        else:
            self.data_folder = os.path.join(self.folder, 'data')

        Factory.register('Notify', cls=Notify)
        App.__init__(self)

    def build(self):
        return Main()

    def build_config(self, config):
        if platform == 'android':
            if os.path.exists('/sdcard/'):
                pass
        else:
            pass

    def build_settings(self, settings):
#        with open('data/settings.json', 'r') as settings_json:
#            settings.add_json_panel('Skeleton Settings',
#                                    self.config, data=settings_json.read())
        pass

    def on_config_change(self, config, section, key, value):
        if config is self.config:
            token = (section, key)
#            if token == ('foo', 'bar'):
#                pass

    def on_start(self):
        """
        Fired when the application is being started (before the runTouchApp() call.
        """
        self.setup_database()
        return True

    def on_stop(self):
        """
        Fired when the application stops.
        """
        return True

    def on_pause(self):
        """ For phones/tablets (experimental feature)
        Fired when the application is paused by the OS.
        Warning
        Both on_pause and on_stop must save important data because after
        on_pause is called, on_resume may not be called at all.
        """
        return True

    def on_resume(self):
        """
        Fired when the application is resumed from pause by the OS.
        Beware: you have no guarantee that this event will be fired after the
        on_pause event has been called.
        """
        pass

    def setup_database(self):
        """Initial setup for the application/database if empty or not existing"""
        try:
            pass
        except Exception:
            pass
        else:
            pass

    def notify(self, msg_type, msg, screen=None):
        """Create and display a floating user notification box and timer to remove it"""
        if screen is None:
            screen = app.root.current
        id = 'notifications_' + str(screen)
        w = Factory.Notify()
        w.message(msg_type, msg)
        wid = 'n' + str(random.randint(1000, 20000))
        w.id = wid
        exec 'app.root.ids.' + id + '.add_widget(w)'
        exec 'i = app.root.ids.' + id
        exec 'kids = app.root.ids.' + id + '.children'
        for k in kids:
            if k.id == wid:
                self.notifications_queue.append(id + '.' + k.id)
                Clock.schedule_once(self.remove_notification, 8)

    def remove_notification(self, dt):
        """Callback from the clock to remove a given floating user notification"""
        if len(self.notifications_queue) > 0:
            x = self.notifications_queue.pop(0)
            x = x.split('.')
            id, wid = x
            exec 'i = app.root.ids.' + id
            exec 'kids = app.root.ids.' + id + '.children'
            for k in kids:
                if k.id == wid:
                    i.remove_widget(k)

    def get_rst_doc(self, doc):
        """a crash happened on android when using a KV file or importing at the top"""
        from kivy.uix.rst import RstDocument
        return RstDocument(source=doc)

    def about(self):
        self.WidgetAbout().open()

    class WidgetAbout(Popup):

        def __init__(self, **kwargs):
            super(MainApp.WidgetAbout, self).__init__()
            self.ids.rst_doc.add_widget(app.get_rst_doc('docs/about.rst'))

    def help(self):
        self.WidgetHelp().open()

    class WidgetHelp(Popup):
        """help screen popup"""
        def __init__(self, **kwargs):
            super(MainApp.WidgetHelp, self).__init__()
            self.ids.rst_doc.add_widget(app.get_rst_doc('docs/help.rst'))

if __name__ in ('__main__', '__android__'):
    Config.set('kivy', 'window_icon', 'assets/img/icon.png')

    KIVY_FONTS = [
        {
            "name": "Ubuntu",
            "fn_regular": "assets/fonts/ubuntu/Ubuntu-L.ttf",
            "fn_bold": "assets/fonts/ubuntu/Ubuntu-M.ttf",
            "fn_italic": "assets/fonts/ubuntu/Ubuntu-LI.ttf",
            "fn_bolditalic": "assets/fonts/ubuntu/Ubuntu-MI.ttf"
        }
    ]
    for font in KIVY_FONTS:
        LabelBase.register(**font)

    files = []
    for root, dirs, files in os.walk('widgets'):
        for file in files:
            if file.endswith('.kv'):
                Builder.load_file(os.path.join(root, file))

    global app
    app = MainApp()
    app.run()
