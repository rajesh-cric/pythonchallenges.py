
r=eval(input('enter no.of elements: '))
s=[]
k=[]

for i in range(0,r):
    w=int(input("number "+str(i+1)+":"))
    s.append(w)
for i in range(0,r):
    x=input("string "+str(i+1)+":")
    k.append(x)
for i in range(0,r):
    if((s[i]==len(k[i]))and(s[i]!=i+1)):
       k[i]=k[i].upper()
    else :
        k[i]=k[i].lower()
k=sorted(k,reverse=True)
for i in k:
    print(i)
