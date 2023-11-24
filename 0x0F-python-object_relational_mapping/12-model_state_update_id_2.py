#!/usr/bin/python3
'''
script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
                           localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    sta_tes = session.query(State).filter(State.name.ilike("%a%")).all()
    for row in sta_tes:
        session.delete(row)
    session.commit()
    session.close()
