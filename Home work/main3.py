import random

ajectives = ["Весёлый", "Грозный", "Ленивый", "Крутой", "Безграничный"]
colors = ['Чёрный', 'Белый', 'Красный', 'Жёлтый', 'Голубой']
animals = ['Кот', 'Собака', 'Волк', 'Ёжик', 'Лиса', 'Медведь']

adjective = random.choice(ajectives)
color = random.choice(colors)
animal = random.choice(animals)

print(f"{adjective}{color}{animal}")