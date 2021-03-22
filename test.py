from random import randint

ctly = 0
inct = 0
cycles = 1

while True:
    if(cycles == 1):
        print(f"{cycles}회 문제") # f-string 파이썬 3.6부터 지원
    else:
        print(f"{cycles}회 문제(현재 정답률: {(ctly/(cycles-1))*100}%)") # f-string
        print("{}회 문제(현재 정답률: {}%)".format(cycles, (ctly/(cycles-1))*100)) # .format
    cycles += 1
    x = randint(1,100)
    y = randint(1,100)
    if int(input(f"{x} + {y} = ")) == x+y:
        print("정답입니다.")
        ctly +=1
    else:
        print(f"오답입니다. (정답: {x+y})")
        inct +=1
    print("------------------------------------------")