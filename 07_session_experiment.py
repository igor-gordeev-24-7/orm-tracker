from database import SessionLocal
from models import User


def without_commit() -> None:
    with SessionLocal() as session:
        user = User(name="Временный", email="test@mail.ru")
        session.add(user)
        print("add() выполнен, commit() НЕ вызывался")

def with_commit() -> None:
    with SessionLocal() as session:
        user = User(name="Постоянный", email="perm@mail.ru")
        session.add(user)
        session.commit()
        print(f"commit() выполнен, ID: {user.id}")

if __name__ == "__main__":
    without_commit()
    with_commit()