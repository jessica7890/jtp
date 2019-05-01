"""
연습 : 띄우기\n 랑 / 띄움표 3개 이런것들 활용,

"""

print(" she's gone")
print(' she\'s gone.')
print(" she\"s gone" )
print(' she"s gone ')
print("""i want to talk long.
 hehehe because i have many things to talk about. 
 yes I really do
      """)
print("this is another good way to \n change a line.\n however this may look very \n messy!")

a = "head "
b = "tail"
print("*"*10)
print(a+b)
print(a*3)
print("*"*10)
print(len(a))
c = "Life is too short, you need python"
print(len(c))
print(c[-1])
d =c[:17]
print(d)
print(c[19:])
print(c[:])
print(c[0]+"\n" + c[-1])
e = "happyness"
print(e[:4]+"i"+e[5:9])

f =1
print(""""I ate %d apples
and I drank %s cups of coffee 
with %d piece of cake
the chance to win is %d %% """ % (3, "five", f, 100) )