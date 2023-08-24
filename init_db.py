# re-initialize the database with a single admin user
from app import db, app
from models import Words

with app.app_context():
    db.drop_all()
    db.create_all() 

    word = Words(
    	word = 'admin',
        part = 'noun',
         ) 

    db.session.add(word)  
    db.session.commit()