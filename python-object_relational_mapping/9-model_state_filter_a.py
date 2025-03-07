#!/usr/bin/python3
"""
This script that lists all State objects that contain
the letter a from the database 'hbtn_0e_6_usa'.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost/{db}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
