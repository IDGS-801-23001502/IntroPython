a=3
b=4
x=0
result=0
tem=""
while x<b:
    x+=1
    tem+=str(a)
    if x == b:
        tem+="="
    else:
        tem+="+"
    result+=a
tem+=str(result)
print(tem)