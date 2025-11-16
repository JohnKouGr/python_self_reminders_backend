from databases.main_database.mdb_engine_session import create_session
from databases.main_database.models.mdb_users import User

def select_all_users_from_main_db():
    session = create_session()
    users = []

    with session as s:
        users = s.query(User).all()

    return users

def insert_user_into_main_db(user):
    session = create_session()

    with session as s:
        s.add(user)
        s.commit()

    return user





