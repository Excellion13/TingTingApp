from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        self.add_widget(Label(text='为了你，我亲爱的婷婷，\n我编写了一个应用程序来学习你的语言',
                               halign='center', valign='middle', font_size='18sp', size_hint_y=0.3))

        phrases = [
            ("Ich liebe dich", "我爱你", "wo_ai_ni.mp3"),
            ("Ich vermisse dich", "我想你", "wo_xiang_ni.mp3"),
        ]

        for de, zh, sound_file in phrases:
            btn = Button(text=f"{de}  ({zh})", font_size='20sp', size_hint_y=None, height=60)
            btn.bind(on_press=lambda x, sf=sound_file: self.play_sound(sf))
            self.add_widget(btn)

    def play_sound(self, sound_file):
        path = f"assets/sounds/{sound_file}"
        sound = SoundLoader.load(path)
        if sound:
            sound.play()

class TingTingApp(App):
    def build(self):
        self.icon = 'icon.png'
        self.title = 'TingTing 我爱你'
        return MainWidget()

if __name__ == '__main__':
    TingTingApp().run()
