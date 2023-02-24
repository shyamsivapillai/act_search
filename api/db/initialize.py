import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os
from .helpers import write_act
from .schemas import Base
from ..settings import get_settings

settings = get_settings()

def initialize_data():

    DB_PATH = settings["DB_URI"]
    engine = create_engine(DB_PATH, echo=True)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    db_file_names = os.listdir("data/")
    acts_written = session.execute(text("SELECT * FROM acts;"))
    acts_written = set([act[2] for act in list(acts_written)])
    
    acts_to_write = []
    for act in db_file_names:
        expected_act_file = act.split(".json")[0]
        if expected_act_file not in acts_written:
            acts_to_write.append(act)

    if acts_to_write:
        print(f"Found {len(acts_to_write)} acts to be stored in database ...")
        acts_to_write_db = []
        for act in acts_to_write:
            j_file = open(f"data/{act}")
            j_data = json.load(j_file)
            db_data = write_act(j_data, act.split(".json")[0], session)
            acts_to_write_db.extend(db_data)

        print("Writing to database now ...")
        session.bulk_save_objects(acts_to_write_db)
        session.commit()

        print(f"Completed writing {len(acts_to_write)} to database ...")
    else:
        print("All acts already available in database..")

    session.close()
