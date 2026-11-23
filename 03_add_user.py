from database import SessionLocal
from models import User


def main() -> None:
    name = input("Имя: ").strip()
    email = input("Email: ").strip().lower()

    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print("Пользователь добавлен")
        print(f"ID: {user.id}")

if __name__ == "__main__":
    main()