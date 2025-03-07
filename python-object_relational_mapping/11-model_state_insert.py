#!/usr/bin/python3
"""
This script that adds the State object “Louisiana”
to the database 'hbtn_0e_6_usa'.
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

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
