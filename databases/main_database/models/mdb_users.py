# package imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

__base = declarative_base()

# Entity model
class User(__base):
    __tablename__ = "users"

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_username = Column(String)
    user_password = Column(String)
    user_role_id = Column(Integer, autoincrement=False)
    user_email = Column(String)
    user_state = Column(String) # active, inactive, pending

    def __repr__(self) -> str:
        return f'("user_id: {self.user_id}", user_username: "{self.user_username}", user_password: "{self.user_password}", user_role_id: "{self.user_role_id}", user_email: "{self.user_email}", user_state: "{self.user_state}")'





