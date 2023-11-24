#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city_state = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for city, state in city_state:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
