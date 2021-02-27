import pytest

from app import app, db, User, Post, Category


@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def db_init():
    db.drop_all()
    db.create_all()


def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()

def test_home(client):
    status_code, body, data = do_get(client, '/')
    old_count = data['count']

    assert status_code == 200
    assert '"text":"Hello, world"' in body


    status_code, body, data = do_get(client, '/')
    new_count = data['count']

    assert status_code == 200
    assert new_count == old_count + 1

def test_abuse(client):
    status_code, body, data = do_get(client, '/')
    old_count = data['count']

    assert status_code == 200

    status_code, body, data = do_get(client, '/abuse')
    new_count = data['count']

    assert status_code == 200
    assert new_count == old_count + 100

def test_creating_User(db_init):
    admin = User(username='admin', email='admin@gmail.com')
    db.session.add(admin)
    db.session.commit()

    assert User.query.filter_by(username='admin').first() == admin

def test_creating_Post(db_init):
    admin = User(username='admin', email='admin@gmail.com')
    category = Category(name='Python')
    post = Post(
        title='New Python Book', body='New Book released!!',
        category=category, user=admin
    )

    db.session.add(category)
    db.session.add(admin)
    db.session.commit()

    assert Post.query.filter_by(title='New Python Book').first().category == category
    assert Post.query.filter_by(title='New Python Book').first().user == admin
    assert Category.query.first().posts[0] == post
    assert User.query.first().posts[0] == post