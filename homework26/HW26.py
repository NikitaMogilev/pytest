import random
from hw26_api import UserApi


def test_read_user_by_id():
    api = UserApi()
    user_id = api.get_user_id(2)
    user_data, get_user_status_code = api.get_user(user_id)
    keys = list(user_data.keys())
    user_keys = ['id', 'email', 'gender', 'name', 'status']
    assert all(x in keys for x in user_keys)
    assert get_user_status_code == 200


def test_get_all_users():
    api = UserApi()
    all_users_data, get_all_users_status_code = api.get_all_users()
    for users in all_users_data:
        for key in ['id', 'email', 'gender', 'name', 'status']:
            assert key in users
    assert get_all_users_status_code == 200


def test_create_user():
    api = UserApi()
    random_number = str(random.randint(0, 10000))
    input_data = {"name": f"Nikita Mogilev{random_number}", "gender": "male",
                  "email": f"test-user-{random_number}@mail.com", "status": "active"}
    user_id, create_status_code = api.create_user(input_data=input_data)
    assert create_status_code == 201
    create_user = api.get_user(user_id)[0]
    input_data['id'] = user_id
    assert input_data == create_user


def test_patch():
    api = UserApi()
    user_id, create_status_code = api.create_user()
    assert create_status_code == 201
    update_status_code = api.update_user(user_id=user_id, patch_data={'name': 'Nikita Updated111'})
    assert update_status_code == 200
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 200
    assert get_user_data['name'] == 'Nikita Updated111'


def test_rewrite_user_put():
    api = UserApi()
    user_id, create_status_code = api.create_user()
    assert create_status_code == 201
    random_number = str(random.randint(0, 10000))
    new_data = {"name": f"Vasya Oblomov{random_number}", "gender": "male",
                "email": f"Vasya{random_number}@oblomov.com", "status": "inactive"}
    rewrited_status_code = api.rewrite_user(user_id=user_id, put_data=new_data)
    assert rewrited_status_code == 200
    rewrited_user = api.get_user(user_id)[0]
    new_data['id'] = user_id
    assert rewrited_user == new_data


def test_delete_user():
    api = UserApi()
    user_id, create_status_code = api.create_user()
    assert create_status_code == 201
    remove_status_code = api.remove_user(user_id=user_id)
    assert remove_status_code == 204
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 404


def test_full_flow():
    api = UserApi()
    user_id, create_status_code = api.create_user()
    assert create_status_code == 201
    updated_user_code = api.update_user(user_id=user_id, patch_data={'name': 'Nikita Updated222'})
    assert updated_user_code == 200
    random_number = str(random.randint(0, 10000))
    new_data = {"name": f"Vasya Oblomov{random_number}", "gender": "male",
                "email": f"Vasya{random_number}@oblomov.com", "status": "inactive"}
    full_rewrited_user_st_code = api.rewrite_user(user_id=user_id, put_data=new_data)
    assert full_rewrited_user_st_code == 200
    full_rewrited_user = api.get_user(user_id)[0]
    new_data['id'] = user_id
    assert full_rewrited_user == new_data
    remove_status_code = api.remove_user(user_id=user_id)
    assert remove_status_code == 204
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 404
