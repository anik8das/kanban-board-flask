# Pytests for Kanban Board Flask application
from app import create_app


def test_home_page():
    """
    Testing if the home page loads successfully
    Algorithm: Checking if header is present
    """
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        # Checking if the heading loads up in the webpage
        assert b"Kanban Board" in response.data


def test_add_task():
    """
    Testing if a task can be added successfully
    Algorithm: Checking if added task is present in HTML
    """
    flask_app = create_app()
    data = {
        # Simulating form data required for adding a task
        'title': 'test task add',
        'description': 'this is the add testing task',
    }
    with flask_app.test_client() as test_client:
        response = test_client.post('/add/todo',
                                    data=data,
                                    follow_redirects=True)
        # Checking if task name is present in the webpage
        assert b"test task add" in response.data


def test_remove_task():
    """
    Testing if a task can be removed successfully
    Algorithm: Adding a task, deleting the task, and verifying that task isn't 
               present in webpage
    """
    flask_app = create_app()
    data = {
        # Simulating form data required for adding a task
        'title': 'test task delete',
        'description': 'this is the delete testing task',
    }
    with flask_app.test_client() as test_client:
        response = test_client.post('/add/doing',
                                    data=data,
                                    follow_redirects=True)
        response = test_client.get('/delete/doing/0')
        # Verifying that the deleted task is not in the webpage
        assert b"test task delete" not in response.data


def test_move_task():
    """
    Testing first if a task can be moved successfully
    Algorithm: Adding a task, moving the task, checking if still present, deleting
               the task from the new category, verify that it's removed from page
    """
    flask_app = create_app()
    data = {
        # Simulating form data required for adding a task
        'title': 'test task move',
        'description': 'this is the move testing task',
    }
    with flask_app.test_client() as test_client:
        response = test_client.post('/add/complete',
                                    data=data,
                                    follow_redirects=True)
        response = test_client.post(
            '/move/complete/0', data={'finalCat': 'todo'}, follow_redirects=True)
        # Verifying that task is still present in page
        assert b"test task move" in response.data

        # Removing task from the new category
        response2 = test_client.get('/delete/todo/0')
        # Checking that the task was removed. If it wasn't moved to the new category,
        # the following assert statement would throw an exception
        assert b"test task move" not in response2.data
