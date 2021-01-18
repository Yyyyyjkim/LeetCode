from itertools import product
import random

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.collection
        self.x_cord = random_sample

        for i in range(len(self.rects)):
            colle

    def pick(self):
        i = random.sample(range(len(self.rects)),1)[0]
        cord = self.rects[i]
        x_cord = random.sample(range(cord[0],(cord[2]+1)),1)[0]
        y_cord = random.sample(range(cord[1],(cord[3]+1)),1)[0] 
        return [x_cord, y_cord]

i = random.sample(range(len(rects)),1)[0]
cord = rects[i]
x_cord = random.sample(range(cord[0],(cord[2]+1)),1)[0]
y_cord = random.sample(range(cord[1],(cord[3]+1)),1)[0] 
[x_cord, y_cord]

cord = rects[0]
x_cord = random.sample(range(cord[0],(cord[2]+1)),1)[0]
y_cord = random.sample(range(cord[1],(cord[3]+1)),1)[0]
[x_cord, y_cord]
random.sample()

for i in range(len([])):
    print(i)

rects = [[[-2,-2,-1,-1],[1,0,3,0]],[],[],[],[],[]]
rects = [[[[1,1,5,5]]],[],[],[]]
rects = [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
rects = [[-2,-2,-1,-1],[1,0,3,0]]
rects = [[82918473, -57180867, 82918476, -57180863],
        [83793579, 18088559, 83793580, 18088560], 
        [66574245, 26243152, 66574246, 26243153], 
        [72983930, 11921716, 72983934, 11921720]]

obj = Solution(rects)
param_1 = obj.pick()

i = 0
pos_cord = []
cord = input1[0][0][i]
print(cord)
x_cord = list(range(cord[0],(cord[2]+1)))
y_cord = list(range(cord[1],(cord[3]+1)))
print(y_cord)
pos_cord.append(list(product(x_cord,y_cord)))
print(pos_cord)



list(zip(x_cord,y_cord))

selection = []
for i in range(len(rects[0][0])):
    cord = rects[0][0][i]
    x_cord = list(range(cord[0],(cord[2]+1)))
    y_cord = list(range(cord[1],(cord[3]+1)))
    selection.append(list(product(x_cord,y_cord)))


result = [list(i) for i in sum(selection,[])]
result = random.sample(result,(len(rects)-1))
result.insert(0, None)

