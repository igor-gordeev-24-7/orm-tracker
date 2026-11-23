from sqlalchemy.orm import Session

from database import SessionLocal
from models import User


def main() -> None:
    users = [
        User(name="Иван", email="ivan@mail.ru"),
        User(name="Мария", email="maria@mail.ru"),
        User(name="Алексей", email="alex@mail.ru"),
    ]

    with SessionLocal() as session:
        session.add_all(users)
        session.commit()

        for user in users:
            print(f"ID: {user.id} — {user.name} <{user.email}>")

if __name__ == "__main__":
    main()