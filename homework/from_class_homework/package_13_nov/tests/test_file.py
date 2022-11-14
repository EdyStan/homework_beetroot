import homework.from_class_homework.package_13_nov.todo_class.todo_class as td
import homework.from_class_homework.package_13_nov.containers.todos_containers as ct
import datetime
import unittest
# from unittest.mock import patch


class TestMeasurements(unittest.TestCase):

    def test_possible_status(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')
        todo.status = 'in progress'

        self.assertEqual(todo.status, "in progress")
        self.assertEqual(todo.__str__(), "Status: in progress\n"
                                         "Description: wash dishes\n"
                                         "Due date: 2022/11/14 19:30.")

    def test_undefined_status(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')
        todo.status = 'I did nothing'

        self.assertEqual(todo.status, "created")
        self.assertEqual(todo.__str__(), "Status: created\n"
                                         "Description: wash dishes\n"
                                         "Due date: 2022/11/14 19:30.")

    def test_set_new_description(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')
        todo.description = 'Feed the pets'

        self.assertEqual(todo.description, "Feed the pets")
        self.assertEqual(todo.__str__(), "Status: created\n"
                                         "Description: Feed the pets\n"
                                         "Due date: 2022/11/14 19:30.")

    def test_delete_description(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')
        del todo.description

        self.assertEqual(todo.description, "")

    def test_set_new_due_date(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')
        todo.due_date = '2022/11/15 20:00'

        self.assertEqual(todo.due_date, datetime.datetime(2022, 11, 15, 20, 0))

    def test_todays_date_True(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')

        self.assertEqual(todo.todays_date(), True)

    def test_todays_date_False(self):
        todo = td.ToDo('wash dishes', '2022/11/14 19:30')
        todo.due_date = '2022/11/16 20:00'

        self.assertEqual(todo.todays_date(), False)

    # @patch('builtins.print')
    # def test_find_tasks_for_today_with_no_arguments(self, mock_print):
    #     lt = ct.ListOfTodos()
    #     lt.find_tasks_for_today()
    #
    #     mock_print.assert_called_with('', '')


if __name__ == "__main__":
    unittest.main()
