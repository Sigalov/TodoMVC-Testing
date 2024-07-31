from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_test import BaseTest


class TodoPage(BaseTest):
    new_todo = (By.CLASS_NAME, "new-todo")
    todo_items = (By.CSS_SELECTOR, ".todo-list li")
    complete_checkbox = (By.CSS_SELECTOR, ".toggle")
    delete_button = (By.CSS_SELECTOR, ".destroy")
    toggle_all = (By.CSS_SELECTOR, "#toggle-all-input")
    clear_completed = (By.CSS_SELECTOR, ".clear-completed")
    all_filter = (By.LINK_TEXT, "All")
    active_filter = (By.LINK_TEXT, "Active")
    completed_filter = (By.LINK_TEXT, "Completed")
    items_left = (By.CSS_SELECTOR, 'footer .todo-count')

    def __init__(self, driver):
        """
        Initialize the TodoPage with a WebDriver instance.

        :param driver: WebDriver instance
        """
        super().__init__(driver)
        self.url = "https://todomvc.com/examples/vue/dist/#/"

    def open(self):
        """
        Open the TodoMVC application.
        """
        super().open(self.url)

    def add_todo_item(self, todo_text):
        """
        Add a new todo item.

        :param todo_text: Text of the todo item to add
        """
        self.find_element(*self.new_todo).send_keys(todo_text + "\n")

    def get_todo_items(self):
        """
        Get all todo items.

        :return: List of WebElements representing the todo items
        """
        return self.find_elements(*self.todo_items)

    def complete_todo_item(self, index):
        """
        Mark a todo item as completed.

        :param index: Index of the todo item to complete
        """
        self.get_todo_items()[index].find_element(*self.complete_checkbox).click()

    def delete_todo_item(self, index):
        """
        Delete a todo item.

        :param index: Index of the todo item to delete
        """
        self.driver.execute_script("arguments[0].click();",
                                   self.get_todo_items()[index].find_element(*self.delete_button))

    def edit_todo_item(self, index, new_text):
        """
        Edit a todo item.

        :param index: Index of the todo item to edit
        :param new_text: New text for the todo item
        """
        todo_items = self.get_todo_items()
        label = todo_items[index].find_element(By.CSS_SELECTOR, 'label')
        self.double_click(label)
        edit_input = todo_items[index].find_element(By.CSS_SELECTOR, '.edit')

        # Use JavaScript to clear the input field
        self.driver.execute_script("arguments[0].value = '';", edit_input)
        edit_input.send_keys(new_text + "\n")

    def mark_all_complete(self):
        """
        Mark all todo items as completed.
        """
        self.click(*self.toggle_all)

    def clear_completed_items(self):
        """
        Clear all completed todo items.
        """
        self.click(*self.clear_completed)

    def filter_all_items(self):
        """
        Filter the todo list to show all items.
        """
        self.click(*self.all_filter)

    def filter_active_items(self):
        """
        Filter the todo list to show only active items.
        """
        self.click(*self.active_filter)

    def filter_completed_items(self):
        """
        Filter the todo list to show only completed items.
        """
        self.click(*self.completed_filter)

    def count_items_left(self):
        """
        Get the count of items left.

        :return: Text representing the count of items left
        """
        return self.find_element(*self.items_left).text
