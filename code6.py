
print("PRINTING YOUR NAME ON THE JERSEY OF HOCKEY TEAM")
fname=input("enter your first name: ")
lname=input("enter your last name: ")
a=len(fname)
b=len(lname)
c=fname[0].capitalize()
d=lname[0].capitalize()
e=fname.capitalize()
g=lname.capitalize()
if (a<10 and b<10):
    print(e,"",g)
if (a>=10 and b<10):
    print(c,".",g)
if (a<10 and b>=10):
    print(e,"",d,".")
if (a>=10 and b>=10):
    print(g)
