import pytest
from models import UserHelper

CONNECTION_STRING = ""
db = UserHelper(CONNECTION_STRING)


def test_add_user():
    target_id = 101

    db.add_user(
        user_id=target_id,
        user_email="add_test@email.com",
        subject_id=None)

    added_user = db.get_user_by_id(target_id)
    assert added_user is not None
    assert added_user.user_email == "add_test@email.com"

    db.delete_user_by_id(target_id)


def test_update_user():
    target_id = 102
    db.add_user(user_id=target_id, user_email="initial@email.com")

    db.update_user_email(target_id, "updated@email.com")

    updated_user = db.get_user_by_id(target_id)
    assert updated_user.user_email == "updated@email.com"

    db.delete_user_by_id(target_id)


def test_delete_user():
    target_id = 103
    db.add_user(user_id=target_id, user_email="delete_me@email.com")

    db.delete_user_by_id(target_id)

    deleted_user = db.get_user_by_id(target_id)
    assert deleted_user is None
