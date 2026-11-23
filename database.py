from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

# Создаёт фабрику сессий SQLAlchemy, привязанную к движку engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)