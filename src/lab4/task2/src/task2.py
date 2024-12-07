class MembersList:
    """Класс для списка участников"""
    def __init__(self, file_path):
        self.members = []
        self.load_members(file_path)


    def load_members(self, file_path):
        """Загружает участников из файла"""
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == "END":
                    break
                name, age = line.strip().split(",")
                self.members.append((name.strip(), int(age.strip())))

    def get_members(self):
        """Возвращает список всех участников"""
        return self.members


class AgeGroup:
    """Класс для разбивки участников по возрастным группам"""
    def __init__(self, age_borders, members_list):
        self.age_borders = age_borders
        self.members_list = members_list

    def sort_members(self, member):
        """Сортировка по возрасту  и по имени """
        name, age = member
        return (-age, name)

    def group_members(self):
        """Распределяет участников по возрастным группам"""
        # Сортируем участников
        self.members_list.get_members().sort(key=self.sort_members)

        # словарь для групп
        groups = {i: [] for i in range(len(self.age_borders))}

        # Распределяем участников по группам
        for name, age in self.members_list.get_members():
            for i in range(len(self.age_borders) - 1):
                if self.age_borders[i] <= age < self.age_borders[i + 1]:
                    groups[i].append((name, age))
                    break
            if age >= self.age_borders[-1]:
                groups[len(self.age_borders) - 1].append((name, age))  # Для группы 101+

        return groups


    def print_groups(self):
        """Выводит результат по возрастным группам"""
        groups = self.group_members()
        for i in range(len(groups) - 1, -1, -1):
            if groups[i]:
                if i == len(self.age_borders) - 1:
                    group_str = f"{self.age_borders[i]} и старше: "
                else:
                    lower_border = self.age_borders[i]
                    upper_border = self.age_borders[i + 1] - 1
                    group_str = f"{lower_border}-{upper_border}: "
                group_str += ", ".join([f"{name} ({age})" for name, age in groups[i]])
                print(group_str)


def task2():
    """Функция для выполнения задачи"""
    MEMBERS_FILE = "../files/members.txt"
    INPUT_FILE = "../files/input.txt"

    with open(INPUT_FILE, 'r') as file:
        age_borders_input = list(map(int, file.readline().strip().split(' ')))
    age_borders = age_borders_input + [101]

    members_list = MembersList(MEMBERS_FILE)
    age_group = AgeGroup(age_borders, members_list)

    age_group.print_groups()


if __name__ == "__main__":
    task2()
