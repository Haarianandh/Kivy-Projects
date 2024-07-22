from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HelloWorldApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.colors = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)]  # Red, Green, Blue
        self.fonts = ['arial.ttf', 'cour.ttf', 'times.ttf']
        self.current_index = 0

        self.create_label()

        self.change_color_button = Button(text='Change Color and Font', on_press=self.change_color_and_font)
        self.layout.add_widget(self.change_color_button)

        return self.layout

    def create_label(self):
        # Create a new Label with the current color and font
        self.label = Label(text='Haaripriya!', font_size=30, color=self.colors[self.current_index], font_name=self.fonts[self.current_index])
        self.layout.add_widget(self.label)

    def change_color_and_font(self, instance):
        # Remove the current label from the layout
        self.layout.remove_widget(self.label)

        # Cycle through the list of colors and fonts
        self.current_index = (self.current_index + 1) % len(self.colors)

        # Create a new label with the updated color and font
        self.create_label()

if __name__ == '__main__':
    HelloWorldApp().run()
