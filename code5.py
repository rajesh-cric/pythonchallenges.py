print("ROOM ALLOTMENT ON THE BASIS OF YOUR FIRST LETTER OF NAME:")
name=input("enter your first name: ")
if name1[0].capitalize()=="A" or name1[0].capitalize()=="B":
    print(name1.capitalize(),'should be in room AB')
elif name1[0].capitalize()=="C":
    print(name1.capitalize(),'should be in room CD')
else:
    name2=input("enter your last name: ")
    if name2[0].capitalize()=="Z":
        print(name1.capitalize(),name2.capitalize(),'should be in room Z')
    else:
        print(name1.capitalize(),name2.capitalize(),'should be in room OTHER')
    
