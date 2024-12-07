import unittest
import datetime
from src.lab4.task2.src.task2 import AgeGroup, MembersList

class TestAgeGroup(unittest.TestCase):

    def setUp(self):
        self.members_file = "members.txt"
        self.input_file = "input.txt"

    def write_members_file(self, members):
        with open(self.members_file, 'w') as f:
            f.write("\n".join(members) + "\nEND")

    def write_input_file(self, age_borders):
        with open(self.input_file, 'w') as f:
            f.write(" ".join(map(str, age_borders)) + "\n")

    def test_full_grouping_output_case1(self):
        # given
        members = [
            "Иванов Иван, 30",
            "Петров Петр, 25",
            "Сидоров Сергей, 40",
            "Кузнецова Анна, 22",
            "Смирнова Мария, 35",
            "Ковалев Виктор, 33",
            "Попов Алексей, 50",
            "Николаева Наталья, 53",
            "Михайлов Андрей, 60",
            "Дмитриев Дмитрий, 55",
            "Павлова Людмила, 47",
            "Васильева Светлана, 45",
            "Федорова Ольга, 41",
            "Егорова Лариса, 38",
            "Чернова Вероника, 31",
            "Тимофеева Оксана, 29",
            "Крылова Ирина, 28",
            "Громова Татьяна, 27",
            "Морозов Роман, 24",
            "Соловьев Александр, 50"
        ]
        age_borders = [18, 36, 59]
        self.write_members_file(members)
        self.write_input_file(age_borders)

        expected_output = (
            "59-100: Михайлов Андрей (60)\n"
            "36-58: Дмитриев Дмитрий (55), Николаева Наталья (53), Попов Алексей (50), "
            "Соловьев Александр (50), Павлова Людмила (47), Васильева Светлана (45), "
            "Федорова Ольга (41), Сидоров Сергей (40), Егорова Лариса (38)\n"
            "18-35: Смирнова Мария (35), Ковалев Виктор (33), Чернова Вероника (31), "
            "Иванов Иван (30), Тимофеева Оксана (29), Крылова Ирина (28), "
            "Громова Татьяна (27), Петров Петр (25), Морозов Роман (24), Кузнецова Анна (22)"
        )

        # when
        members_list = MembersList(self.members_file)
        age_group = AgeGroup(age_borders + [101], members_list)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        age_group.print_groups()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue().strip()

        # then
        self.assertEqual(result, expected_output, "Вывод групп некорректен.")

    def test_single_group_output(self):
        # given
        members = [
            "Иванов Иван, 25",
            "Петров Петр, 22",
            "Кузнецова Анна, 29",
            "Громова Татьяна, 28"
        ]
        age_borders = [18, 36, 59]
        self.write_members_file(members)
        self.write_input_file(age_borders)

        expected_output = '18-35: Кузнецова Анна (29), Громова Татьяна (28), Иванов Иван (25), Петров Петр (22)'


        # when
        members_list = MembersList(self.members_file)
        age_group = AgeGroup(age_borders + [101], members_list)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        age_group.print_groups()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue().strip()

        # then
        self.assertEqual(result, expected_output, "Вывод групп некорректен.")

    def test_only_old_group_output(self):
        # given
        members = [
            "Иванов Иван, 65",
            "Петров Петр, 70",
            "Кузнецова Анна, 80"
        ]
        age_borders = [18, 36, 59]
        self.write_members_file(members)
        self.write_input_file(age_borders)

        expected_output = (
            '59-100: Кузнецова Анна (80), Петров Петр (70), Иванов Иван (65)'
        )

        # when
        members_list = MembersList(self.members_file)
        age_group = AgeGroup(age_borders + [101], members_list)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        result = age_group.print_groups()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue().strip()

        # then
        self.assertEqual(result, expected_output, "Вывод групп некорректен.")

    def test_edge_case_members_output(self):
        # given
        members = [
            "Иванов Иван, 18",
            "Петров Петр, 36",
            "Кузнецова Анна, 59",
            "Громова Татьяна, 60"
        ]
        age_borders = [18, 36, 59]
        self.write_members_file(members)
        self.write_input_file(age_borders)

        expected_output = ('59-100: Громова Татьяна (60), Кузнецова Анна (59)\n'
                           '36-58: Петров Петр (36)\n'
                           '18-35: Иванов Иван (18)')

        # when
        members_list = MembersList(self.members_file)
        age_group = AgeGroup(age_borders + [101], members_list)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        age_group.print_groups()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue().strip()

        # then
        self.assertEqual(result, expected_output, "Вывод групп некорректен.")


if __name__ == "__main__":
    unittest.main()
