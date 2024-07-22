import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class GuessingGame(GridLayout):
    def __init__(self, **kwargs):
        super(GuessingGame, self).__init__(**kwargs)
        self.cols = 1

        self.secret_number = random.randint(1, 100)
        self.add_widget(Label(text="Guess the number between 1 and 100:"))
        self.user_input = TextInput(multiline=False)
        self.add_widget(self.user_input)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.check_guess)
        self.add_widget(self.submit_button)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def check_guess(self, instance):
        try:
            guess = int(self.user_input.text)
            if guess == self.secret_number:
                self.result_label.text = "Congratulations! You guessed it right!"
            elif guess < self.secret_number:
                self.result_label.text = "Try a higher number."
            else:
                self.result_label.text = "Try a lower number."
            # Clearing the text input for the next guess
            self.user_input.text = ""
        except ValueError:
            self.result_label.text = "Please enter a valid number."

class GuessingApp(App):
    def build(self):
        return GuessingGame()

if __name__ == "__main__":
    GuessingApp().run()
