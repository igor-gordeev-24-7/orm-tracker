from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg://postgres:password"
    "@localhost:5432/tracker_orm"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)