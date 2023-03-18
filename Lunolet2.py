import math
class Lunolet2():
    r_default = [0,       # 0  горизонтальная скорость
                 0,       # 1  наклон корабля
                 0,       # 2  время манёвра
                 0,       # 3  ускорение корабля
                 1.62,    # 4  ускорение свободного падения
                 2250,    # 5  масса корабля без топлива
                 3660,    # 6  скорость вылета продукнов сгорания
                 9.81 * 3,# 7  предельное ускорение
                 0,       # 8  расход топлива
                 0,       # 9  высота корабля
                 0,       # 10 вертикальная скорость
                 250000,  # 11 растояние до цели
                 400]     # 12 запас топлива
    def __init__(self, output_ = print, input_ = input, r = ([0]*13), config_ = True):
        self.output = output_
        self.input = input_
        self.r = r
        if config_: self.__config()
    def __call__(self):
        while True:
            self.output(f"Верт. скорость: {self.r[10]}")
            self.output(f"Высота:         {self.r[9]}")
            self.output(f"Гор. скорость:  {self.r[0]}")
            self.output(f"Растояние:      {self.r[11]}")
            self.output(f"Запас топлива:  {self.r[11]}")
            self.output(f"Ускорение:      {self.r[3]}")
            self.output(f"Время:          {self.r[12]}")
            while (x := float(self.input())) >= self.r[5] * 0.05:
                self.output("Слишком большой расход!")
            while (y := float(self.input())) == 0:
                self.output("Время не может равняться нулю!")
            z = float(self.input())
            self.__step(x, y, z)
    def __config(self):
        self.output("Для ввода значения по умолчанию введите d")
        self.output(f"Введите ускорение свододного падения ({self.r_default[4]} по умолчанию)")
        self.r[4] = self.r_default[4] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите массу корабля без топлива ({self.r_default[5]} по умолчанию)")
        self.r[5] = self.r_default[5] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите скорость продукнов сгорания  ({self.r_default[6]} по умолчанию)")
        self.r[6] = self.r_default[6] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите предельное ускорение ({self.r_default[7]} по умолчанию)")
        self.r[7] = self.r_default[7] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите начальную высоту ({self.r_default[9]} по умолчанию)")
        self.r[9] = self.r_default[9] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите начальную верт. скорость ({self.r_default[10]} по умолчанию)")
        self.r[10] = self.r_default[10] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите растояние до цели ({self.r_default[11]} по умолчанию)")
        self.r[11] = self.r_default[11] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите начальную гор. скорость ({self.r_default[0]} по умолчанию)")
        self.r[0] = self.r_default[0] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите запас топлива ({self.r_default[12]} по умолчанию)")
        self.r[12] = self.r_default[12] if (i := self.input()) == 'd' else float(i)
    def __step(self, x, y, z):
        self.r[1] = z
        self.r[2] = y
        self.r[8] = x / self.r[2]
        self.r[3] = (self.r[8] * self.r[6]) / (self.r[12] + self.r[5])
        while True:
            while True:
                r0tmp = self.r[0]
                self.r[0] += math.sin(self.r[1]) * self.r[3] * self.r[2]
                self.r[11] -= ((r0tmp + self.r[0]) * 2) / 2
                rbtmp = self.r[10]
                self.r[10] -= (self.r[4] - self.r[3] * math.cos(self.r[1])) * self.r[2]
                self.r[9] += ((rbtmp+self.r[10]) * 2) / 2
                self.r[12] -= self.r[8] * self.r[2]
                if self.r[12] >=0:
                    break
                self.r[2] = self.r[12] / self.r[8]
            if self.r[9] < 0:
                self.r[2] = (2 * self.r[9]) / ((2 * self.r[9] * (self.r[4] - self.r[3] * math.cos(self.r[1])))**0.5 - self.r[10])
            elif self.r[9] != 0:
                if self.r[3] < self.r[7]:
                    if self.r[12] == 0:
                        self.output("Нехватка топлива!")
                        self.r[2] = self.r[6]
                        self.r[8] = 0
                        self.r[3] = 0
                    else:
                        break #ввод/вывод
                else:
                    self.output("Перегрузки!")
                    self.r[2] = self.r[3] - self.r[7]
                    self.r[8] = self.r[12] / self.r[2]
                    self.r[3] = (self.r[8] * self.r[6]) / (self.r[12] + self.r[5])
            else:
                break #ввод/вывод
            
if __name__ == "__main__":
    l2 = Lunolet2()
    l2()