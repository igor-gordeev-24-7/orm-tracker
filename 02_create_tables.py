from sqlalchemy import text

from database import engine
from models import Base

# Создаёт в базе данных все таблицы, описанные в моделях SQLAlchemy.
def create_table() -> None:
    Base.metadata.create_all(engine)


def check_structure() -> None:
    with engine.connect() as conn:
        result = conn.execute(text
            (
            """
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'users'
            ORDER BY ordinal_position
            """
            )
        )
        for column_name, data_type, is_nullable in result:
            print(f"{column_name:<12} {data_type:<20} nullable={is_nullable}")

if __name__ == "__main__":
    create_table()
    print("Структура таблицы users")
    check_structure()