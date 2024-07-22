from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.expression = TextInput(multiline=False, readonly=True, font_size=50, size_hint_y=None, height=100)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.expression)
        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40)
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            layout.add_widget(row_layout)
        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.expression.text = str(eval(self.expression.text))
            except:
                self.expression.text = 'Error'
        elif instance.text == 'C':
            self.expression.text = ''
        else:
            self.expression.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()
