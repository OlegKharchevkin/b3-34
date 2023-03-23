import math
class Lunolet3():
    r_default = [0,       # 0  горизонтальная скорость
                 0,       # 1  время манёвра
                 1.62,    # 2  ускорение свободного падения
                 2250,    # 3  масса корабля без топлива
                 3660,    # 4  скорость вылета продукнов сгорания
                 1738000, # 5  радиус Луны
                 0,       # 6  ускорение
                 0,       # 7  угол наклона корабля
                 1738000, # 8  радиус орбиты корабля
                 0,       # 9  вертикальная скорость
                 0,       # 10 угловая координата
                 3500]    # 11 запас топлива
    def __init__(self, output_ = print, input_ = input, r = ([0]*12), config_ = True):
        self.output = output_
        self.input = input_
        self.r = r
        if config_: self.__config()
    def __call__(self):
        while True:
            self.output(f"Верт. скорость:     {self.r[9]}")
            self.output(f"Высота:             {self.r[8] - self.r[5]}")
            self.output(f"Гор. скорость:      {self.r[0]}")
            self.output(f"Угловая коорд.:     {self.r[10]}")
            self.output(f"Запас топлива:      {self.r[11]}")
            self.output(f"Первая космическая: {(self.r[2] / self.r[8])**0.5 * self.r[5]}")
            if math.cos(self.r[10]): 
                self.output("Обратная сторона Луны")
            else:
                self.output("Видимая сторона Луны")
                
            while (x := float(self.input())) >= self.r[3] * 0.05 and self.r[11] >= x:
                self.output("Слишком большой расход!")
            while (y := float(self.input())) == 0:
                self.output("Время не может равняться нулю!")
            z = float(self.input())
            self.step(x, y, z)
    def __config(self):
        self.output("Для ввода значения по умолчанию введите d")
        self.output(f"Введите ускорение свододного падения ({self.r_default[2]} по умолчанию)")
        self.r[2] = self.r_default[2] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите массу корабля без топлива ({self.r_default[3]} по умолчанию)")
        self.r[3] = self.r_default[3] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите скорость продукнов сгорания  ({self.r_default[4]} по умолчанию)")
        self.r[4] = self.r_default[4] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите радиус Луны  ({self.r_default[5]} по умолчанию)")
        self.r[5] = self.r_default[5] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите начальную высоту ({self.r_default[8] - self.r[5]} по умолчанию)")
        self.r[8] = (self.r_default[8] if (i := self.input()) == 'd' else float(i)) + self.r[5]
        self.output(f"Введите начальную верт. скорость ({self.r_default[9]} по умолчанию)")
        self.r[9] = self.r_default[9] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите угловую координату ({self.r_default[10]} по умолчанию)")
        self.r[10] = self.r_default[10] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите начальную гор. скорость ({self.r_default[0]} по умолчанию)")
        self.r[0] = self.r_default[0] if (i := self.input()) == 'd' else float(i)
        self.output(f"Введите запас топлива ({self.r_default[11]} по умолчанию)")
        self.r[11] = self.r_default[11] if (i := self.input()) == 'd' else float(i)
    def step(self, x, y, z):
        self.r[7] = z
        self.r[6] = (x * self.r[4]) / ((self.r[3] + self.r[11]) * y)
        self.r[1] = y
        if self.r[8] - self.r[5] <= 10**(-2): 
            self.r[9] = 0
            self.r[0] = 0
            self.r[8] = self.r[5]
        self.r[11] -= x
        ratmp = self.r[8]
        while True:
            r0tmp = self.r[0]
            self.r[0] += (self.r[6] * math.sin(math.radians(self.r[7])) - (self.r[9] * self.r[0]) / ratmp) * self.r[1]
            self.r[10] += ((r0tmp + self.r[0]) * self.r[1] * 90) / (math.pi * ratmp)
            rbtmp = self.r[9]
            y = self.r[6] * math.cos(math.radians(self.r[7])) - (self.r[5] / ratmp)**2 * self.r[2]
            self.r[9] += ((self.r[0]**2 / ratmp) + y)* self.r[1]
            self.r[8] += ((rbtmp + self.r[9]) * self.r[1]) / 2
            if self.r[8]>=self.r[5]: 
                break
            self.r[1] = (self.r[5] - self.r[8]) / self.r[9]
            
if __name__ == "__main__":
    l3 = Lunolet3(r = Lunolet3.r_default, config_ = False)
    l3()