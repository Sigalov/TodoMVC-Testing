import pytest

@pytest.mark.edit
def test_edit_todo_item(todo_page):
    """
    Test editing a todo item.
    """
    todo_page.add_todo_item("Buy groceries")
    todo_page.edit_todo_item(0, "Buy milk")
    updated_todo_items = todo_page.get_todo_items()
    assert "Buy milk" in updated_todo_items[0].text

@pytest.mark.edit
def test_edit_multiple_todo_items(todo_page):
    """
    Test editing multiple todo items.
    """
    todo_page.add_todo_item("Item 1")
    todo_page.add_todo_item("Item 2")
    todo_page.edit_todo_item(0, "Updated Item 1")
    todo_page.edit_todo_item(1, "Updated Item 2")
    updated_todo_items = todo_page.get_todo_items()
    assert "Updated Item 1" in updated_todo_items[0].text
    assert "Updated Item 2" in updated_todo_items[1].text
