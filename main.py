from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button, ButtonBehavior
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import strftime


Window.borderless = True

class ImageButton(ButtonBehavior,Image):
    pass

class StopwatchScreen (Screen):
    pass


class ClockScreen (Screen):
    pass


class MainApp (App):
    sw_started = False
    sw_seconds = 0

    def update(self,nap):
        if self.sw_started:
            self.sw_seconds += nap

        self.root.ids['clock_screen'].ids['time'].text=strftime('[b]%H[/b]:%M:%S')
        m,s = divmod(self.sw_seconds,60)
        self.root.ids['stopwatch_screen'].ids['stopwatch'].text=('%02d: %02d.[size=40]%02s[/size]'%(int(m),int(s),int(s*100%100)))

    def on_start(self):
        Clock.schedule_interval(self.update,0)

    def go_forward(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction="right")
        screen_manager.current = 'stopwatch_screen'

    def go_back(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition (direction="left")
        screen_manager.current = 'clock_screen'

    def start_stop(self):
        self.root.ids['stopwatch_screen'].ids['start_stop'].text='Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started
        #print("Start Stop")

    def reset(self):
        if self.sw_started:
            self.root.ids['stopwatch_screen'].ids['start_stop'].text='Start'
            self.sw_started = False
        self.sw_seconds = 0
        #print("Reset")


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex ('#101216')
    LabelBase.register(name='Roboto', fn_regular='Roboto-Thin.ttf', fn_bold='Roboto-Medium.ttf')
MainApp ().run ()
