from databases.main_database.commands.lg_mdb_users import insert_user_into_main_db, select_all_users_from_main_db

def mdb_select_all_users():
    users = select_all_users_from_main_db()

    return users

def mdb_insert_user(user):
    newUser = insert_user_into_main_db(user)

    return newUser
