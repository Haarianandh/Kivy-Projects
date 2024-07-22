# Import necessary modules
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

class GuessNumberApp(App):
    
    def build(self):
        self.secret_number = 10  # Generate a random number between 1 and 100
        self.attempts = 0  # Counter for attempts
        
        # GUI elements
        self.message = Label(text="Guess the number between 1 and 100")
        self.input = TextInput(hint_text="Enter your guess here", multiline=False)
        self.submit_button = Button(text="Submit", on_press=self.check_guess)
        
        # Layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.message)
        layout.add_widget(self.input)
        layout.add_widget(self.submit_button)
        
        return layout

    def check_guess(self, instance):
        # Get the guessed number from the input field
        guess = int(self.input.text)
        self.input.text = ""  # Clear input field
        
        # Check if the guess is correct
        if guess == self.secret_number:
            self.message.text = f"Congratulations! You guessed the number in {self.attempts} attempts!"
            self.submit_button.disabled = True  # Disable the submit button after the correct guess
        elif guess < self.secret_number:
            self.message.text = "Too low! Try again."
        else:
            self.message.text = "Too high! Try again."
            
        self.attempts += 1

# Run the app
if __name__ == "__main__":
    GuessNumberApp().run()
