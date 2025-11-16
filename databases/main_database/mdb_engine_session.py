from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from enviroment.dbs_config import DB_MAIN_DATABASENAME, DB_MAIN_HOST, DB_MAIN_PASSWORD, DB_MAIN_PORT, DB_MAIN_USERNAME

# connection pool
__dbUsername = DB_MAIN_USERNAME
__dbPassword = DB_MAIN_PASSWORD
__dbHost = DB_MAIN_HOST
__dbName = DB_MAIN_DATABASENAME
__dbPort = DB_MAIN_PORT

# engine to use for connection
__eng = engine.create_engine(f"postgresql://{__dbUsername}:{__dbPassword}@{__dbHost}:{__dbPort}/{__dbName}", echo=False)

# session will connect to database and give the ability to execute transactions
def create_session():
    sessionmkr = sessionmaker(bind=__eng,expire_on_commit=False)
    session = sessionmkr()

    return session 