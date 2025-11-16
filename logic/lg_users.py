from databases.main_database.commands.lg_mdb_users import insert_user_into_main_db, select_all_users_from_main_db
from databases.main_database.models.mdb_users import User

def mdb_select_all_users():
    users = select_all_users_from_main_db()
    
    return users

def mdb_insert_user(user_username, user_password, user_email, user_state, user_role_id):
    user = User(user_username = user_username, user_password = user_password, user_email = user_email, user_state = user_state, user_role_id = user_role_id)
    newUser = insert_user_into_main_db(user)

    return newUser
