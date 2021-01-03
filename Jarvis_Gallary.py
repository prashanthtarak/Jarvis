from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

Window.size = (300, 500)

KV='''
MDScreen:
    radius: [0, 0, 0, 0]
    md_bg_color: [.7, .9, .9, 1]
    
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: button_on
                        title: "Photos"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [['chemical-weapon', lambda x: x],['dots-vertical', lambda x: app.menu.open()]]

                    ScrollView:

                        GridLayout:
                            cols: 3
                            row_default_height: (self.width - self.cols*self.spacing[1]) / self.cols
                            row_force_default: True
                            size_hint_y: None
                            height: self.minimum_height
                            padding: "8dp", "8dp", "8dp", "8dp"
                            spacing: dp(8)

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab4.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image4')
                            
                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab5.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image5')

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab6.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image6')

                            SmartTileWithStar:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab7.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image7')

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab2.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image8')
                            
                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab5.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image9')
                            
                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab1.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image1')

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab2.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image2')

                            SmartTileWithStar:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab3.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image3')

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab4.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image4')
                            
                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab5.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image5')

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab6.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image6')

                            SmartTileWithStar:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab7.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image7')

                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab2.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image8')
                            
                            SmartTileWithLabel:
                                source: "C:/Users/Prash/OneDrive/Desktop/New folder/photos/ab5.jpg"
                                text: '[size=0][/size]'
                                on_press: print('pressed on image9')
                                
        MDNavigationDrawer:
            id: nav_drawer

'''

class TestApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.screen = Builder.load_string(KV)
        menu_items = [
            {"text": "Name"},
            {"text": "Date Of Birth"},
            {"text": "Log Out"}]
        self.menu= MDDropdownMenu(caller=self.screen.ids.button_on, items= menu_items, width_mult=4)

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return self.screen

TestApp().run()