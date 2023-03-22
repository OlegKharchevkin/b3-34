import math
class Lunolet3():
    def __init__(self, output_ = print, input_ = input, r = ([0]*13), config_ = True):
        self.output = output_
        self.input = input_
        self.r = r
        if config_: self.__config()
    def __call__(self):
        pass
    def __config(self):
        pass
    def step(self, x, y, z):
        pass
    
if __name__ == "__main__":
    l3 = Lunolet3()
    l3()