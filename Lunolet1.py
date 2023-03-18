class Lunolet1():
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
		self.output = output_
		self.input = input_
		self.r = r
		if config_: self.__config()
	def __f1(self, x, y):
		self.r[1] = x
		self.r[2] = y
		if self.r[2] >= 0:
			self.r[8] = self.r[1] / self.r[2]
			self.r[3] = self.r[8] / (self.r[5] + self.r[12])  * self.r[6]
		rbtmp = self.r[10]
		self.r[10] +=(self.r[3] - self.r[4]) * self.r[2]
		self.r[9] +=(rbtmp + self.r[10]) / 2 * self.r[2]
		self.r[11] -= self.r[2] * self.r[0]
		self.r[12] -= self.r[1]
	def __config(self):
		self.output("Для ввода значения по умолчанию введите d")
		self.output(f"Введите ускорение свододного падения ({self.r_default[4]} по умолчанию)")
		self.r[4] = self.r_default[4] if (i := self.input()) == 'd' else float(i)
		self.output(f"Введите массу корабля без топлива ({self.r_default[5]} по умолчанию)")
		self.r[5] = self.r_default[5] if (i := self.input()) == 'd' else float(i)
		self.output(f"Введите скорость вылета продукнов сгорания  ({self.r_default[6]} по умолчанию)")
		self.r[6] = self.r_default[6] if (i := self.input()) == 'd' else float(i)
		self.output(f"Введите предельное ускорение ({self.r_default[7]} по умолчанию)")
		self.r[7] = self.r_default[7] if (i := self.input()) == 'd' else float(i)
		self.output(f"Введите начальную высоту ({self.r_default[9]} по умолчанию)")
		self.r[9] = self.r_default[9] if (i := self.input()) == 'd' else float(i)
		self.output(f"Введите начальную скорость ({self.r_default[10]} по умолчанию)")
		self.r[10] = self.r_default[10] if (i := self.input()) == 'd' else float(i)
		self.output(f"Введите режим таймера (1 - вкл., 0 - выкл.)")
		if (i := float(self.input().replace('d', str(self.r_default[0])))) == 1:
			self.output(f"Введите оставшееся время ({self.r_default[11]} по умолчанию)")
			self.r[11] = self.r_default[11] if (j := self.input()) == 'd' else float(j)
		self.r[0] = i
		self.output(f"Введите запас топлива ({self.r_default[12]} по умолчанию)")
		self.r[12] = self.r_default[12] if (i := self.input()) == 'd' else float(i)
	def __call__(self):
		while True:
			self.output(f"Скорость:      {self.r[10]}")
			self.output(f"Высота:        {self.r[9]}")
			self.output(f"Запас топлива: {self.r[11]}")
			self.output(f"Ускорение:     {self.r[3]}")
			self.output(f"Время:         {self.r[12]}")
			while (x := float(self.input())) >= self.r[5] * 0.05:
				self.output("Слишком большой расход!")
			while (y := float(self.input())) == 0:
				self.output("Время не может равняться нулю!")
			self.__step(x, y)
	def __step(self, x, y):
		self.r[1] = x
		r2tmp = y
		self.r[2] = abs(r2tmp)
		self.r[8] = self.r[1] / r2tmp
		self.r[3] = self.r[8] / (self.r[5] + self.r[12])  * self.r[6]
		if self.r[10] < 0: self.r[10] = 0
		rbtmp = self.r[10]
		self.r[10] +=(self.r[3] - self.r[4]) * self.r[2]
		self.r[9] +=(rbtmp + self.r[10]) / 2 * self.r[2]
		self.r[11] -= self.r[2] * self.r[0]
		self.r[12] -= self.r[1]
		while True:
			if self.r[12] < 0:
				self.__f1(self.r[12], self.r[12] / self.r[8])
			if self.r[9] != 0:
				if self.r[9] < 0:
					rtmp = self.r[9] * 2 /(((self.r[4] - self.r[3]) * self.r[9] * 2 + self.r[10]**2)**0.5 - self.r[10])
					self.__f1(rtmp * self.r[8], rtmp)
				else:
					if self.r[12] != 0:
						if (self.r[3]**2)**0.5 - self.r[7] < 0:
							break
						else:
							self.output("Перегрузки!")
							self.__f1(0, (self.r[3]**2)**0.5 - self.r[7])
					else:
						self.output("Нехватка топлива!")
						self.__f1(0, self.r[6])
			else:
				break
if __name__ == "__main__":
    l1 = Lunolet1()
    l1()