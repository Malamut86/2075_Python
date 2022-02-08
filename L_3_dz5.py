import random


class rlist ():
    def __init__(self, lst, rg=None, rseed=None):

        self.lst = lst

        if rg is not None:
            self.rg = rg
        else:
            self.rg = random.Random()
            if rseed is not None:
                self.rg.seed(rseed)

    def choice(self):
         return self.rg.choice(self.lst)

if __name__ == '__main__':
    rl1 = rlist(["автомобиль","лес","огонь","город","дом"], rseed=1234)
    rl2 = rlist(["сегодня", "вчера", "завтра", "позавчера", "ночью"], rseed=1234)
    rl3 = rlist(["веселый", "яркий", "зеленый", "утопичный", "мягкий"], rseed=1234)
    print('Raz:')
    print(rl1.choice(), rl3.choice(), rl2.choice())
    print('Dva:')
    print(rl1.choice(), rl2.choice(), rl3.choice())
    print('Tri:')
    print( rl3.choice(), rl1.choice(), rl2.choice())
