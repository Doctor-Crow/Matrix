enter = int(input())
math = [[0] * enter for i in range(enter)]
counter, m = 1, 0

math[enter // 2][enter // 2]= enter * enter
for v in range(enter // 2):

    for i in range(enter - m):
        math[v][i + v] = counter
        counter+=1


    for i in range(v+1, enter - v):
        math[i][-v - 1] = counter
        counter+=1


    for i in range(v+1, enter - v):
        math[-v - 1][-i - 1] =counter
        counter+=1
        

    for i in range(v+1, enter - (v + 1)):
        math[-i - 1][v]=counter
        counter+=1
    m+=2

for i in math:
    print(*i)