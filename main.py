from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.popup import Popup
import testing_audio

class RootWidget(App):
    def build(self): 
        btn = Button(text ="Push Me !", 
                   font_size ="20sp", 
                   background_color =(1, 1, 1, 1), 
                   color =(1, 1, 1, 1), 
                   size =(32, 32), 
                   size_hint =(.2, .2), 
                   pos =(300, 250))

        btn.bind(on_press = self.callback) 
        return btn

    def callback(self, event):
        return testing_audio.run_cmd()
        # print("button pressed") 
        # print('Yoooo !!!!!!!!!!!')


root = RootWidget()
root.run()

# class ActionApp(App):
    # def build(self):
        # return RootWidget()

# if __name__ == "__main__":
#     ActionApp().run()
#     RootWidget().run()
 