import math
class Lunolet2():
    r_default = [0,       # 0  режим таймера
                 0,       # 1  масса сжигаемого топлива
                 0,       # 2  время манёвра
                 0,       # 3  ускорение корабля
                 1.62,    # 4  ускорение свободного падения
                 2250,    # 5  масса корабля без топлива
                 3660,    # 6  скорость вылета продукнов сгорания
                 9.81 * 3,# 7  предельное ускорение
                 0,       # 8  расход топлива
                 0,       # 9  высота корабля
                 0,       # 10 скорость корабля
                 3600,    # 11 оставшееся время
                 400]     # 12 запас топлива
    def __init__(self, output_ = print, input_ = input, r = ([0]*13), config_ = True):
        pass
    def __call__():
        pass
    def __config():
        pass
    def __step(self, x, y, z):
        r1 = z
        r2 = y
        r8 = x / r2
        r3 = (r8 * r6) / (rd + r5)
        while True:
            while True:
                r0tmp = r0
                r0 += math.sin(r1) * r3 * r2
                rc -= ((r0tmp + r0) * 2) / 2
                rbtmp = rb
                rb -= (r4 - r3 * math.cos(r1)) * r2
                ra += ((rbtmp+rb) * 2) / 2
                rd -= r8 * r2
                if rd >=0:
                    break
                r2 = rd / r8
            if ra < 0:
                r2 = (2 * ra) / ((2 * ra * (r4 - r3 * math.cos(r1)))**0.5 - rb)
            elif ra != 0:
                if r3 < r7:
                    if rd == 0:
                        self.output("Нехватка топлива!")
                        r2 = r6
                        r8 = 0
                        r3 = 0
                    else:
                        break #ввод/вывод
                else:
                    self.output("Перегрузки!")
                    r2 = r3 - r7
                    r8 = rd / r2
                    r3 = (r8 * r6) / (rd + r5)
            else:
                break #ввод/вывод
            
if __name__ == "__main__":
    l2 = Lunolet2()
    l2()