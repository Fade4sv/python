from sqlalchemy import create_engine
from sqlalchemy.sql import text


class UserHelper:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_user_by_id(self, user_id):
        query = text("SELECT * FROM users WHERE user_id = :user_id")
        return self.db.execute(query, {"user_id": user_id}).fetchone()

    def add_user(self, user_id, user_email, subject_id=None):
        query = text("""
            INSERT INTO users (user_id, user_email, subject_id)
            VALUES (:user_id, :user_email, :subject_id)
        """)
        self.db.execute(query,
                        {
                            "user_id": user_id,
                            "user_email": user_email,
                            "subject_id": subject_id
                            }
                        )

    def update_user_email(self, user_id, new_email):
        query = text(
            "UPDATE users SET user_email = :new_email WHERE user_id = :user_id"
            )
        self.db.execute(query, {"new_email": new_email, "user_id": user_id})

    def delete_user_by_id(self, user_id):
        query = text("DELETE FROM users WHERE user_id = :user_id")
        self.db.execute(query, {"user_id": user_id})
