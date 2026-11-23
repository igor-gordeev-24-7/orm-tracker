from database import SessionLocal
from models import User, Task


def main() -> None:
    user_id_raw = input("ID пользователя: ").strip()
    title = input("Название: ").strip()
    priority = input("Приоритет: ").strip().lower() or "low"

    user_id = int(user_id_raw)

    with SessionLocal() as session:
        user = session.get(User, user_id)

        if user is None:
            print("Пользователи не найдены")
            return

        task = Task(title=title, priority=priority, user=user)
        session.add(task)
        session.commit()

        print(f"Задача добавлена. ID: {task.id}")
        print(f"Владелец: {user.name}")

if __name__ == "__main__":
    main()