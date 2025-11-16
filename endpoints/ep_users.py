from flask import Blueprint, request

from logic.lg_users import mdb_insert_user, mdb_select_all_users

app = Blueprint("ep_users", __name__)

@app.get("/doc")
def doc():
    return "<h1>Users Api's</h1>" \
           "<h2>/mdballusers</h2>" \
           "<div>Returns a list of users who belong in main db.</div>" \
           "<h2>/mdbcreatenewuser</h2>" \
           "<div>Returns the new user to be added to main db.</div>" \

@app.get("/mdballusers")
def mdb_all_users():
    users = mdb_select_all_users()

    return {"users" : users, "message" : "All users stored in main database"}

@app.post("/mdbcreatenewuser")
def mdb_create_new_user():
    user = {"user_username" : request.form.get("user_username"), "user_password" : request.form.get("user_password"), "user_email": request.form.get("user_email"), "user_state" : "pending", "user_role_id" : 0}
    user = mdb_insert_user(user)

    return {"users" : user, "message" : "All users stored in main database"}
