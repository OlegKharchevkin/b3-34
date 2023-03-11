class Lunolet1():
	def __init__(self, output_ = print, input_ = input, r = ([0]*13), config_ = False):
		self.output = output_
		self.input = input_
		self.r = r
		if config_: __config()
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
		self.output("Для ввода значения по умолчанию введите 0")
		self.output("Введите ускорение свододного падения (1.62 по умолчанию)")
		self.r[4] = 1.62     if (i := float(self.input())) == 0 else i
		self.output("Введите массу корабля без топлива (2250 по умолчанию)")
		self.r[5] = 2250     if (i := float(self.input())) == 0 else i
		self.output("Введите скорость продукнов сгорания  (3660 по умолчанию)")
		self.r[6] = 3660     if (i := float(self.input())) == 0 else i
		self.output("Введите предельное ускорение (29.43 по умолчанию)")
		self.r[7] = 9.81 * 3 if (i := float(self.input())) == 0 else i
		self.output("Введите режим таймера (1 - вкл., 0 - выкл.)")
		if (i := float(self.input())) == 1:
			self.output("Введите оставшееся время (3600 по умолчанию)")
			self.r[11] = 3600    if (j := float(self.input())) == 0 else j
		self.r[0] = i
		self.output("Введите запас топлива (400 по умолчанию)")
		self.r[12] = 400     if (i := float(self.input())) == 0 else i
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
