from database import SessionLocal
from models import User


def main() -> None:
    user_id = int(input("ID пользователя: ").strip())

    with SessionLocal() as session:
        user = session.get(User, user_id)

        if user is None:
            print("Пользователь не найден.")
            return

        print(f"Пользователь: {user.name}")

        if not user.tasks:
            print("У пользователя пока нет задач.")
            return

        print("Задачи:")
        for i, task in enumerate(user.tasks, start=1):
            status = "выполнена" if task.is_completed else "не выполнено"
            print(f"{i}. {task.title} | {status} | {task.priority}")

if __name__ == "__main__":
    main()
