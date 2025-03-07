#!/usr/bin/python3
"""
This script that deletes all State objects with a name containing
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

    session.query(State).filter(
        State.name.contains('a')).delete(synchronize_session=False)
    session.commit()
    session.close()
