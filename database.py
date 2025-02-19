import sqlite3


class DatabaseManager:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                        NAME TEXT,
                        EMAIL TEXT UNIQUE,
                        PASSWORD TEXT
                    )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS stocks(
            TICKER TEXT,
            NAME TEXT
            )""")
            conn.commit()

    def add_user(self, name, email, password):
        with self.connect() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email,  password))
            except sqlite3.IntegrityError:
                return False
            else:
                conn.commit()
                return True

    def get_user(self, email):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE EMAIL = ?", (email,))
            return cursor.fetchone()

    def email_check(self, email):
        with self.connect() as conn:
            cursor = conn.cursor()
            have_email = cursor.execute("SELECT COUNT(*) FROM users WHERE EMAIL = ?", (email,)).fetchone()[0]
            return have_email

    def get_password(self, email):
        with self.connect() as conn:
            cursor = conn.cursor()
            database_password = cursor.execute(f"SELECT PASSWORD FROM users WHERE email = ?", (email,)).fetchone()[0]
            return database_password

    def get_name(self, email):
        with self.connect() as conn:
            cursor = conn.cursor()
            name = cursor.execute(f"SELECT NAME FROM users WHERE EMAIL=\'" + email + "\'").fetchone()[0]
            return name

    def change_password(self, email, new_password):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE users SET PASSWORD=? WHERE EMAIL=?", (new_password, email))
            conn.commit()

