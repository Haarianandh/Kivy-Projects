from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import webbrowser
class GoogleMapApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        open_map_button = Button(text="Open Google Maps")
        open_map_button.bind(on_press=self.open_google_maps)
        layout.add_widget(open_map_button)
        return layout
    def open_google_maps(self, instance): webbrowser.open("https://www.google.com/maps")
if __name__ == "__main__":
    GoogleMapApp().run()
