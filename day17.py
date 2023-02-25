from math import lcm
from argparse import ArgumentParser

'''
The tall, vertical chamber is exactly seven units wide. Each rock appears so
that its left edge is two units away from the left wall and its bottom edge
is three units above the highest rock in the room (or the floor, if there
isn't one).
'''

class Chamber:
    def __init__(self):
        with open(args.f, 'r') as f:
            self.gusts = next(f).strip()
        self.debris = []
        self.rocks = [[[0,0,1,1,1,1,0]],
                    [[0,0,0,1,0,0,0],
                    [0,0,1,1,1,0,0],
                    [0,0,0,1,0,0,0]],
                    [[0,0,1,1,1,0,0],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0]],
                    [[0,0,1,0,0,0,0],
                    [0,0,1,0,0,0,0],
                    [0,0,1,0,0,0,0],
                    [0,0,1,0,0,0,0]],
                    [[0,0,1,1,0,0,0],
                    [0,0,1,1,0,0,0]]
                    ]
        self.gust = 0
        self.fall = 0
        # print(lcm(len(self.rocks), len(self.gusts)))


    def rockfall(self, rock):
        self.fall += 1
        bot = len(self.debris)+3
        self.debris.extend([[0 for _ in range(7)] for _ in range(3)])
        self.debris.extend(self.rocks[rock])
        while True:
            # print(str(['#']*7))
            # for row in self.debris:
            #     print(row)
            # print(bot)
            # print(str(['#']*7))
        # while 1 in self.debris[-1]:
            gustdir = ord(self.gusts[self.gust])-61
            self.gust += 1
            self.gust %= len(self.gusts)
            shift = True
            for row in range(bot, len(self.debris)):
                if not shift:
                    break
                for col in range(7):
                    try:
                        if self.debris[row][col] == 1:
                            if col+gustdir not in range(7) or self.debris[row][col+gustdir] == 2:
                                shift = False
                                break
                    except:
                        pass
                        # print(row, col, len(self.debris), bot)
            if shift:
                for row in range(bot, len(self.debris)):
                    newrow = [0 for _ in range(7)]
                    for col in range(7):
                        if self.debris[row][col] == 1:
                            newrow[col+gustdir] = 1
                        elif self.debris[row][col] == 2:
                            newrow[col] = 2
                    self.debris[row] = newrow
            fall = True
            for row in range(bot,len(self.debris)):
                if row == 0:
                    fall=False
                if fall is False:
                    break
                for col in range(7):
                    if self.debris[row][col] == 1 and self.debris[row-1][col] == 2:
                        fall = False
                        break
            if fall:
                # print(f'rock {rock} falling from {bot} to {bot-1}')
                for row in range(bot, len(self.debris)):
                    newrow = [0]*7
                    for col in range(7):
                        if self.debris[row][col] == 1:
                            self.debris[row-1][col] = 1
                            newrow[col]=0
                        elif self.debris[row][col]== 2:
                            newrow[col] = 2
                    self.debris[row]= newrow
                bot -= 1
                # print(bot)
                # for row in self.debris:
                    # print(row)
                try:
                    while max(self.debris[-1]) == 0:
                        x=self.debris.pop()
                except:
                    continue
                    # print(f'fail {len(self.debris)}')
                    # print(self.debris)
            else:
                for row in range(bot, len(self.debris)):
                    for col in range(7):
                        if self.debris[row][col] == 1:
                            self.debris[row][col]= 2
                    # if sum(self.debris[row]) == 14:
                    #     print(rock, len(self.debris), bot, self.fall)
                break



def main():
    chamber = Chamber()
    if args.p == 1:
        playlen = 2022
    elif args.p == 2:
        #after rock 1827, every 1745 rocks a pattern repeats and the debris gets 
        #2750 taller
        #after 1827 the height is 2859
        #subtract 1827 from 1000000000000
        reps, rem = divmod(1000000000000 - 1827, 1745)
        baseheight = (reps)*2750
        playlen = 1827+rem
    else:
        raise NotImplementedError('Solution for this part not yet implemented')
    gust = 0
    beep = 0
    for i in range(playlen):
        rock = i%5
        gust = chamber.rockfall(rock)
        # if not i%lcm(len(chamber.rocks),len(chamber.gusts)):
        #     print(len(chamber.debris) - beep)
        #     beep= len(chamber.debris)
    # for row in chamber.debris[::-1]:
    #     print(''.join(['#' if x else '.'  for x in row]))
    if args.p == 1:
        print(len(chamber.debris))
    else:
        print(len(chamber.debris)+baseheight)
        #1575931229326 is too low
        #1575931232076 is too 

    # return gust

if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('f', type=str)
    argparser.add_argument('p', type=int)
    args = argparser.parse_args()
    main()