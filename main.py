#  3. Решите задачу. Класс Tomato.


class Tomato:                                                      # Создайте класс Tomato
    states = {0: 'отсутствуют', 1: 'зеленый',                      # Создайте статическое свойство states, которое будет содержать
              2: 'краснеет', 3: 'созрел'}                          # все стадии созревания помидора

    def __init__(self, index):                                     # Создайте метод __init__(), внутри которого будут определены
        self._index = index                                        # два динамических protected свойства:
        self._state = 0                                            # 1) _index - передается параметром и
                                                                   # 2) _state - принимает первое значение из словаря states
    def grow(self):
        if self._state < 3:                                        # Создайте метод grow(), который будет переводить томат на
            self._state += 1                                       # следующую стадию созревания
        self.print_states()

    def is_ripe(self):                                             # Создайте метод is_ripe(), который будет проверять, что томат
        if self._state == 3:                                       # созрел (достиг последней стадии созревания)
            return True
        return False

    def print_states(self):
        print(f'Томат {self._index} сейчас {Tomato.states[self._state]}.')



class TomatoBush:                                                           # Создайте класс TomatoBush (куст)

    def __init__(self, count):                                              # Определите метод __init__(), который будет принимать в
        self.tomatoes = [Tomato(index) for index in range(1, count+1)]      # качестве параметра количество томатов и на его основе
    # создали список из объектов класса Tomato                              # будет создавать список объектов класса Tomato.
                                                                            # Данный список будет храниться внутри динамического
                                                                            # свойства tomatoes.

    def grow_all(self):                                                     #  Создайте метод grow_all(), который будет переводить все
        for tomato in self.tomatoes:                                        # объекты из списка томатов на следующий этап созревания
            tomato.grow()                                                   # в методе grow +1

    def all_are_ripe(self):                                                 # Создайте метод all_are_ripe(), который будет возвращать True,
        return all([tomato.is_ripe() for tomato in self.tomatoes])          # если все томаты из списка стали спелыми

    def give_away_all(self):                                                # Создайте метод give_away_all(), который будет чистить список
        self.tomatoes = []                                                  # томатов после сбора урожая
        print('Все собрали. Томатов больше нет.')


class Gardener:                                                             # Создайте класс Gardener

    def __init__(self, name, plant):                                        # Создайте метод __init__(), внутри которого будут определены
        self.name = name                                                    # два динамических свойства: 1) name - передается параметром, является публичным и
        self._plant = plant                                                 # 2) _plant - принимает объект класса Tomato, является protected
    # выдаем садовнику растение для ухода

    def work(self):                                                   # Создайте метод work(), который заставляет садовника работать, что позволяет
        print('Садовник поливает.')                                   # растению становиться более зрелым.
        self._plant.grow_all()
        print('Садовник закончил поливать.\n')

    def harvest(self):                                                # Создайте метод harvest(), который проверяет, все ли плоды созрели.
        if self._plant.all_are_ripe():
            print('Садовник собирает урожай.')
            self._plant.give_away_all()
        else:
            print('Еще рано собирать урожай.\n')

    @staticmethod                                                     # Создайте статический метод knowledge_base(), который
    def knowledge_base():                                             # выведет в консоль справку по садоводству.
        print('Справка по садоводству.\n')

Gardener.knowledge_base()
tomato_bush = TomatoBush(3)
gardener = Gardener('Иван', tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
