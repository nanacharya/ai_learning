with open("newtextfile.txt", "w") as file:
    file.write("hello, world")
    file.writelines(["Line 1" , "Line 2", "Line 3"])
    file.writelines(["Line 1" , "Line 2", "Line 3"])


print("----------------")

with open("newtextfile.txt", "r") as readingfile:
    contnet = readingfile.read()
    print(contnet)
    print("read ----------------")
    
    content = readingfile.readline()

    print(contnet)
    print("readline ----------------")
    
    
    content = readingfile.readlines()

    print(contnet)
    print("readlines ----------------") 
    

try:    
    with open("newtextfiles.txt", "r") as readingfile:
        contnet = readingfile.read()
        print(contnet)
        print("read ----------------")
        
        content = readingfile.readline()

        print(contnet)
        print("readline ----------------")
        
        
        content = readingfile.readlines()

        print(contnet)
        print("readlines ----------------") 
except:
    print("file not found")