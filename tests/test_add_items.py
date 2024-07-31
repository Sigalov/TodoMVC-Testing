import pytest

@pytest.mark.add
def test_add_todo_items(todo_page):
    """
    Test adding two todo items.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.add_todo_item("Read a book")
    todo_items = todo_page.get_todo_items()
    assert len(todo_items) == 2

@pytest.mark.add
def test_add_special_characters(todo_page):
    """
    Test adding a todo item with special characters.
    """
    special_text = "!!@#$%^&*()_+{}:\"<>?[];',./`~"
    todo_page.add_todo_item(special_text)
    todo_items = todo_page.get_todo_items()
    assert special_text in todo_items[0].text

@pytest.mark.add
def test_add_long_string(todo_page):
    """
    Test adding a todo item with a very long string.
    """
    long_text = "a" * 1000
    todo_page.add_todo_item(long_text)
    todo_items = todo_page.get_todo_items()
    assert long_text in todo_items[0].text

@pytest.mark.add
def test_add_empty_string(todo_page):
    """
    Test adding an empty string to the todo list.
    """
    todo_page.add_todo_item("")
    todo_items = todo_page.get_todo_items()
    assert todo_items[0].text.replace('Edit Todo Input', '') == ""
