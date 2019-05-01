# if 문 연습입니당~
money = 3000
card = False
friend = True

if money > 3000 or card:
    print("택시를 타고가라")
elif friend:
    print("카드택시를 타라")
else:
    print("걸어가자")

#아래 if문 에서  input값을 바로 int로 바꿔서 변수정의 없이 if식에 바로 넣을수도 있네~ 그리고 notin 연습
a = [1,2,3,4]

if int(input("숫자를 넣으세요\n")) not in a:
    print("해당 숫자가 리스트에 없습니다")
else:
    print("해당숫자는 리스트에 있습니다")

b = "python"
if input("알파벳하나를 넣으시오\n")in b:
    print("해당문자는 리스트에있음")
else:
    print("해당문자는 없음")

#아래연습에서 d = [b,c] 이런식으로도 리스트를 만들수 있다.
c = "java"
d = [ b , c ]
if "java" in d: print("java있네~")
else: print("java없네")
