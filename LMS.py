f=open("LMS.txt", "r+")
name=f.readlines()
name=[x.strip() for x in name] ## removes white spaces
##name = ["physics","chemistry","maths","edc","ect"]

def ret(back):
    ##f.append(back) ## cannot use append in r+ cannot use read in a+ >.<
    for item in name:
        f.write("%s\n" %item)  ## writes the full list each time i open it >.<

ir = eval(input("Do you want to issue or return a book? 1 or 2 "))
if (ir==1):
    book=input("Enter the name of the book you want ")
    print(" Available books are: ")
    for x in name:
        print(x)
    if (book in name):
        print(" here is your book  ")
        ##name.pop(book)
    else:
        print(" the book you want is issued to someone else please come back later ")
    
elif (ir==2):
    back=input(" name of the book being returned  ")
    ret(back)
    
    print(" the books available are:")
    for x in name:
        print(x)


        