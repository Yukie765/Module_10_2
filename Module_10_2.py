from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.time_tick = 0
        self.enemy_count = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemy_count > 0:
            sleep(1)
            self.time_tick += 1
            self.enemy_count = self.enemy_count - self.power
            print(f'{self.name} сражается {self.time_tick} день(дня), осталось {self.enemy_count} воинов.')
        print(f'{self.name}, одержал победу спустя {self.time_tick} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')

