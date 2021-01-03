from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
Screen:
    FloatLayout:
        MDRaisedButton:
            text: "ALERT DIALOG"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_alert_dialog()

'''

class JarvisApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        txtclr = [0, 1, 1, 1 ] #text color in rgba value
        c_button = MDFlatButton(text="CANCEL", text_color=txtclr, on_release= self.close_fun)
        d_button = MDFlatButton(text="DISCARD", text_color=txtclr)

        self.dialog = MDDialog(text="Discard draft?",radius = [30, 7, 30, 7], buttons=[c_button, d_button])
        self.dialog.open()

    def close_fun(self, obj):
        self.dialog.dismiss()

JarvisApp().run()