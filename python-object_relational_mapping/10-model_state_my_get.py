#!/usr/bin/python3
"""
This script that prints the State object with the name
passed as argument from the database 'hbtn_0e_6_usa'.
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

    name_filter = sys.argv[4]
    state = session.query(State).filter(State.name == name_filter).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
