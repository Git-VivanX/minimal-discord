from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base

# SQLite database URL - change this to PostgreSQL or MySQL in production
SQLALCHEMY_DATABASE_URL = "sqlite:///./discord_clone.db"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
