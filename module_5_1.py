class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей \nПоднимаемся на {new_floor}-й')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

h = House('ЖК Славянка', 9)
h2 = House('ЖК Лазурный', 25)

h.go_to(8)
h2.go_to(26)