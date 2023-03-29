"""CRUD operations."""

# import functions from model.py
from model import db, User, Movie, Rating, connect_to_db

# CRUD functions
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

    



   
    
    
    
    
    
# Connect to database when running crud.py interactively
if __name__ == '__main__':
    from server import app
    connect_to_db(app)

