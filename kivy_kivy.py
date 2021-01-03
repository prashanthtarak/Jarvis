from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class PalmWidget(Widget):

    def play(self):

        img=ResizeableImage(source = "C:/Users/Prash/OneDrive/Desktop/New folder/Photos/ab1.jpg")
        self.add_widget(img)
        img2=ResizeableImage(source = "C:/Users/Prash/OneDrive/Desktop/New folder/Photos/ab2.jpg")
        self.add_widget(img2)
        return

class ResizeableImage(Image):
    pass

class Collection(Widget):
    pass

class PalmApp(App):
    def build(self):

        layout = FloatLayout()
        palm = PalmWidget()
        layout.add_widget(palm)
        palm.play()
        return layout


if __name__ == '__main__':
    PalmApp().run()