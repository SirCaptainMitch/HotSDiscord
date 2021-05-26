
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from app.models.user import User

Base = declarative_base()

def create_database(): 
  engine = create_engine('sqlite:///app.db')
  engine.connect()
  Session = sessionmaker()

  Session.configure(bind=engine)  

  session = Session()  

  Base.metadata.create_all(engine)

  session.commit()

  return session
