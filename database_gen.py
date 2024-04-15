import json
import random

# Sample lists of words for generating titles, content, and tags
title_words = ['The', 'A', 'An', 'Love', 'War', 'Adventure', 'Secret', 'Lost', 'Dream', 'Mystery',
               'King', 'Queen', 'Prince', 'Princess', 'Journey', 'Quest', 'Legend', 'Magic', 'Hero', 'Villain',
               'Star', 'Galaxy', 'Space', 'Time', 'Future', 'Past', 'Ancient', 'Modern', 'Epic',
               'Forest', 'Mountain', 'Desert', 'Ocean', 'Island', 'City', 'Town', 'Country', 'World', 'Universe']

beginning_words = ['In a world where,', 'When', 'After', '', 'At dawn,', 'One morning,',
                   'Once upon a time', 'Long ago,', 'One year,', 'In a distant future,', 'In a faraway land,',
                   'In a post-apocalyptic world,', 'At the edge of the universe,', 'In the heart of darkness,',
                   'In the shadows,', 'Deep underground,', 'Beyond the horizon,', 'Under the light of the moon,',
                   'Under the stars,', 'Within the depths,', 'Amidst the chaos,', 'On the outskirts of the city,']

climax_words = ['has to go on an intense adventure', 'faces their greatest challenge', 'discovers a hidden truth',
                'must confront their fears', 'embarks on a dangerous journey', 'finds themselves in a race against time',
                'encounters a life-changing event', 'is forced to make a difficult decision', 'enters a world of mystery',
                'uncovers a dark secret', 'is drawn into an epic conflict', 'must overcome seemingly insurmountable odds',
                'gets caught up in a hilarious misunderstanding', 'trips over their own feet at the worst possible moment',
                'loses their pants in front of the entire town', 'becomes the accidental leader of a ragtag group',
                'discovers they have a secret talent for interpretive dance', 'befriends a talking squirrel',
                'gets mistaken for a famous celebrity', 'starts a food fight in the middle of a fancy dinner party']

ending_words = ['learns a valuable lesson about the world', 'discovers the true meaning of friendship', 'finds redemption',
                'realizes their inner strength', 'achieves their ultimate goal', 'finds peace and closure',
                'forgives those who wronged them', 'returns home changed but wiser', 'starts a new chapter in their life',
                'learns to believe in themselves', 'creates a better future for themselves and others',
                'shares a laugh with newfound friends', 'rides off into the sunset on a llama', 
                'wins the heart of their one true love', 'throws the party of the century', 'becomes the talk of the town',
                'wakes up and realizes it was all just a dream', 'finds a pot of gold at the end of the rainbow']

character_names = ['John', 'Emily', 'Michael', 'Sarah', 'Marissa', 'Emma', 'Daniel', 'Olivia', 'James', 'Sophia', 
                   'Will', 'Isabella', 'Chadwick', 'Penelope', 'Rex', 'Gertrude', 'Frodo', 'Gandalf', 
                   'Hermione', 'Chuckles', 'Samantha', 'Bartholomew', 'Beatrice', 'Giggles', 'Barnaby', 
                   'Snickerdoodle', 'Esmeralda', 'Waldo', 'Clementine', 'Reginald', 'Prudence', 'Bubba', 
                   'Pumpkin', 'Rutherford', 'Thomas', 'Buttercup', 'Benedict', 'Stelios', 'Mortimer', 
                   'Kit-Kat', 'Pepper', 'Gumbo', 'Ginger', 'Bubbles', 'Biscuit', 'Pickle', 'Tater Tot']

tag_words = ['Action', 'Comedy', 'Drama', 'Thriller', 'Horror', 'Romance', 'Sci-Fi', 'Fantasy',
             'Adventure', 'Mystery', 'Crime', 'Historical', 'Animation', 'Family', 'Superhero', 'Musical',
             'Documentary', 'Biography', 'War', 'Western', 'Sports', 'Alien', 'Robot', 'Zombie', 'Vampire']

# Generate a random movie title
def generate_title():
    return ' '.join(random.sample(title_words, random.randint(1, 3))) + ' Movie'

# Generate random content summary
def generate_content():
    beginning = random.choice(beginning_words)
    character = random.choice(character_names)
    climax = random.choice(climax_words)
    ending = random.choice(ending_words)
    
    return f"{beginning} {character} {climax}, {character} {ending}"

# Generate random tags
def generate_tags():
    return random.sample(tag_words, random.randint(1, 3))

# Generate movie data
def generate_movie_data(num_movies):
    movies = []
    for i in range(num_movies):
        movie = {
            "title": generate_title(),
            "content": generate_content(),
            "tags": generate_tags(),
            "id": i
        }
        movies.append(movie)
    return movies

# Generate 10,000 movie data
movies_data = generate_movie_data(10000)

# Write movie data to a JSON file
with open('database.json', 'w') as f:
    json.dump({"entries": movies_data, "max_id": 10000}, f, indent=4)