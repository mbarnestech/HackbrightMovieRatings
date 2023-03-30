"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/movies.json') as file:
    movie_data = json.loads(file.read())

movies_in_db = []

for movie in movie_data:
    overview, poster_path, release_date_string, title = movie.values()
    format_date = '%Y-%m-%d'
    release_date = datetime.strptime(release_date_string, format_date)
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)

for n in range(10):
    email = f"user{n}@test.com"  
    password = f"test{n}"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for i in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        model.db.session.add(rating)



model.db.session.commit()
