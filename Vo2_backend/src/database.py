from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your MySQL connection string
# Replace 'username', 'password', 'hostname', and 'database' with your actual values
db_uri = 'mysql+pymysql://aashish:Aashish%4099@localhost/endurunz'


# Create a SQLAlchemy engine
engine = create_engine(db_uri)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()