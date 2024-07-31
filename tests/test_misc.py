import pytest

@pytest.mark.count
def test_count_items_left(todo_page):
    """
    Test counting the number of items left.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.complete_todo_item(0)
    items_left = todo_page.count_items_left()
    assert "1 item left" in items_left
