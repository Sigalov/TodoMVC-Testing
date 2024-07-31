import pytest


@pytest.mark.filter
def test_filter_active_items(todo_page):
    """
    Test filtering the todo list to show only active items.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.complete_todo_item(0)
    todo_page.filter_active_items()
    active_items = todo_page.get_todo_items()
    assert len(active_items) == 1
    assert "Read a book" in active_items[0].text


@pytest.mark.filter
def test_filter_completed_items(todo_page):
    """
    Test filtering the todo list to show only completed items.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.complete_todo_item(0)
    todo_page.filter_completed_items()
    completed_items = todo_page.get_todo_items()
    assert len(completed_items) == 1
    assert "Buy groceries" in completed_items[0].text


@pytest.mark.filter
def test_filter_all_items(todo_page):
    """
    Test filtering the todo list to show all items.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.complete_todo_item(0)
    todo_page.filter_all_items()
    all_items = todo_page.get_todo_items()
    assert len(all_items) == 2


@pytest.mark.filter
def test_filter_active_and_completed(todo_page):
    """
    Test filtering the todo list to show only active and only completed items.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_page.complete_todo_item(0)

    # Test Active filter
    todo_page.filter_active_items()
    active_items = todo_page.get_todo_items()
    assert len(active_items) == 1
    assert "Read a book" in active_items[0].text
    assert "completed" not in active_items[0].get_attribute("class")

    # Test Completed filter
    todo_page.filter_completed_items()
    completed_items = todo_page.get_todo_items()
    assert len(completed_items) == 1
    assert "Buy groceries" in completed_items[0].text
    assert "completed" in completed_items[0].get_attribute("class")
