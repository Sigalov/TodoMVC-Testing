import pytest

@pytest.mark.complete
def test_complete_todo_item(todo_page):
    """
    Test marking a todo item as completed.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_items = todo_page.get_todo_items()
    todo_page.complete_todo_item(0)
    assert "completed" in todo_items[0].get_attribute("class")

@pytest.mark.complete
def test_mark_all_complete(todo_page):
    """
    Test marking all todo items as completed.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.mark_all_complete()
    todo_items = todo_page.get_todo_items()
    for item in todo_items:
        assert "completed" in item.get_attribute("class")

@pytest.mark.complete
def test_clear_completed(todo_page):
    """
    Test clearing all completed todo items.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.complete_todo_item(0)
    todo_page.clear_completed_items()
    remaining_items = todo_page.get_todo_items()
    assert len(remaining_items) == 1
    assert "Read a book" in remaining_items[0].text

@pytest.mark.complete
def test_toggle_todo_item(todo_page):
    """
    Test toggling the completion status of a todo item.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_items = todo_page.get_todo_items()
    todo_page.complete_todo_item(0)
    todo_page.complete_todo_item(0)
    assert "completed" not in todo_items[0].get_attribute("class")

@pytest.mark.complete
def test_reopen_completed_todo_item(todo_page):
    """
    Test reopening a completed todo item.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_items = todo_page.get_todo_items()
    todo_page.complete_todo_item(0)
    assert "completed" in todo_items[0].get_attribute("class")
    todo_page.complete_todo_item(0)
    assert "completed" not in todo_items[0].get_attribute("class")
