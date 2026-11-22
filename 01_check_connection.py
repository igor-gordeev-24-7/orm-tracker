from sqlalchemy import text

from database import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT current_database(), current_user"))
    database, user = result.one()
    print(f"База: {database}")
    print(f"Пользователь: {user}")