# Битва Героев
# простая текстовая боевая игра, где игрок и компьютер управляют
# с различными характеристиками. Игра состоит из раундов,
# в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.
# from abc import ABC, abstractmethod
# class Hero(ABC):
#     @abstractmethod
import random

class Hero():
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power =attack_power
# Атакует другого героя(other), отнимая здоровье в размере своей силы удара
    def attack(self,other): #
#       self.other = other
        print(f'Наносим удар!')
        other.health -= self.attack_power
# Возвращает True, если здоровье героя больше 0, иначе False
    def is_alive(self):
        if self.health<=0:
           life =True
        else:
            life = False
        return life

class Game():
    def start():
        i=1
        print(f'раунд',i)
        while p1.is_alive() and p2.is_alive():
            print(f'раунд', i)
            print(f'{p1.name} наносит удар силой {p1.attack_power}')
            p1.attack(p2)
            print(f'{p2.name} теряет здоровье {p2.health})')
            print(f'{p2.name} наносит удар силой {p2.attack_power}')
            p2.attack(p1)
            print(f'{p1.name} теряет здоровье {p1.health})')
            i+=1
            print(f'раунд', i)
        if p1.health>p2.health:
            print(f'{p1.name}  победил {p2.name}')
        else:
            print(f'{p2.name} победил {p1.name}')

p1 = Hero("Player",100,10)
p2 = Hero( 'Computer',80,15)
g1 = Game
g1.start()




