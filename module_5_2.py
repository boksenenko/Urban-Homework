class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor <= self.num_of_floors:
            for i in range(1, new_floor +1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.num_of_floors}.'

    def __len__(self):
        return self.num_of_floors

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
