from app.database.base import Base
from app.database.sessions import engine
from app.models.users import User


def init_db():
    """
    Initialize the database by creating all tables
    """
    # Import all models here to ensure they are registered with Base
    # This ensures all tables are created
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    init_db()
