import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from logic.domain import Domain

class App(App):

    def build(self):
        button.bind(on_release=self.button_released)
        layout=BoxLayout(orientation="vertical")
        layout.add_widget(label)
        layout.add_widget(button)
        
        return layout
  
    def button_released(self,instance):
        text = dom.process_electro()

        if text == "0.0":
            label.text = "result = 0.0\n sano"
        elif text == "1.0":
            label.text = "result = 1.0\n x"
        elif text == "2.0":
            label.text = "result = 2.0\n x"
        elif text == "3.0":
            label.text = "result = 3.0\n noise"
        else:
            label.text = "!!! error !!!"

if __name__ == '__main__':
    dom = Domain()
    label = Label(text="Bienvenido")
    button = Button(text="Clica aquí para obtener el análisis",size_hint=(0.5,0.5),pos_hint={'center_x': 0.5, 'center_y': 0.5})
    App().run()
