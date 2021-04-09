from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button, ButtonBehavior
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex


class ImageButton(ButtonBehavior,Image):
    pass

class StopwatchScreen (Screen):
    pass


class ClockScreen (Screen):
    pass


class MainApp (App):
    def go_forward(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction="right")
        screen_manager.current = 'stopwatch_screen'

    def go_back(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition (direction="left")
        screen_manager.current = 'clock_screen'


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex ('#101216')
    LabelBase.register(name='Roboto', fn_regular='Roboto-Thin.ttf', fn_bold='Roboto-Medium.ttf')
MainApp ().run ()
