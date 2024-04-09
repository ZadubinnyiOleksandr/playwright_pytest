import pytest

from pages.todo_page import TodoList

class TestTodoList:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.todo_list = TodoList(self.page)

        self.page.goto('https://webdriveruniversity.com/To-Do-List/index.html')

    def test_todo_list(self, test_setup):
        self.todo_list.clear_todo_list()
        self.todo_list.create_todos()
        self.todo_list.clear_todo_list()
