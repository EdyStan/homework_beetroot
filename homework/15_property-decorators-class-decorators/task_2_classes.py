class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers_list = []

    @property
    def workers(self):
        return self._workers_list

    @workers.setter
    def workers(self, *values):
        for value in values:
            self._workers_list.append(value)

    @workers.deleter
    def workers(self):
        self._workers_list = []
        print('Deleted!')

    def __str__(self):
        return str(self.id) + ': ' + self.name

    def __repr__(self):
        return str(self.id) + ': ' + self.name


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value: Boss):
        self._boss = value

    @boss.deleter
    def boss(self):
        self._boss = None
        print('Freelancer!')

    def __str__(self):
        return str(self.id) + ': ' + self.name

    def __repr__(self):
        return str(self.id) + ': ' + self.name
