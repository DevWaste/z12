# Определение класса Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создание объекта Transport
Autobus = Transport("Renault Logan", 180, 12)

# Вывод информации об объекте
print(f"Название автомобиля: {Autobus.name}, Скорость: {Autobus.max_speed}, Пробег: {Autobus.mileage}")
