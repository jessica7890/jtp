

#3-2 연습하기 while 문


#1. treehit
treehit = 0

while treehit < 10 :
    treehit = treehit + 1
    if treehit<10:
        print("아직멀었음.%d 번 찍음" % treehit)
    else: print("%d번찍었음. 성공!" %treehit)

#2.prompt에 값넣고 while 문
    prompt = """
    1.add
    2. del
    3. list
    4. quit
    enter number : """

    number = 0
while number !=4:
        print(prompt)
        number = int(input())

#3 coffee machine 

coffee = 10

while True :
    money = int(input(" 동전을 넣어주세요  요금은 300원입니다"))
    if money >= 300:

        if coffee > 0:
            coffee = coffee -1
            print("커피를 드립니다. 거스름돈은 %d 원입니다 남은커피는 %d잔 입니다. " % ((money - 300) ,coffee))
        else:
            print("커피가 없어서 종료합니다. 투입하신 돈을 환불해드립니다.")
            break
    else :
        print ("300원보다 적은금액을 투입하셨습니다. 커피판매는 되지 않습니다")

