import pytest

@pytest.mark.delete
def test_delete_todo_item(todo_page):
    """
    Test deleting a todo item.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.delete_todo_item(1)
    todo_items = todo_page.get_todo_items()
    assert len(todo_items) == 1
