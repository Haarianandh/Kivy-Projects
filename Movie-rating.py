from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class MovieRatingApp(App):
    movies = {}

    def build(self):
        self.title = 'Movie Rating App'
        self.main_layout = BoxLayout(orientation='vertical')
        
        self.input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.movie_input = TextInput(hint_text='Enter movie name')
        self.rating_input = TextInput(hint_text='Enter rating')
        self.add_button = Button(text='Add Rating', on_press=self.add_rating)
        self.input_layout.add_widget(self.movie_input)
        self.input_layout.add_widget(self.rating_input)
        self.input_layout.add_widget(self.add_button)
        
        self.movies_layout = BoxLayout(orientation='vertical')
        self.main_layout.add_widget(self.input_layout)
        self.main_layout.add_widget(self.movies_layout)
        
        return self.main_layout
    
    def add_rating(self, instance):
        movie_name = self.movie_input.text.strip()
        rating = self.rating_input.text.strip()
        
        if movie_name and rating:
            if movie_name not in self.movies:
                self.movies[movie_name] = [float(rating)]
            else:
                self.movies[movie_name].append(float(rating))
            
            self.update_movies_layout()
            self.movie_input.text = ''
            self.rating_input.text = ''
    
    def update_movies_layout(self):
        self.movies_layout.clear_widgets()
        for movie, ratings in self.movies.items():
            avg_rating = sum(ratings) / len(ratings)
            movie_label = Label(text=f"{movie}: {avg_rating:.2f}")
            self.movies_layout.add_widget(movie_label)

if __name__ == '__main__':
    MovieRatingApp().run()
