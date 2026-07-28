from pathlib import Path
import os

def createfile():
    try:
        name = input("Enter the name of the file you want to create:")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("Enter the data you want to write in the file:")
                fs.write(data)
            print("File created successfully")
        else:
            print("ERROR file name already exists")   
    except Exception as err:
        print(f"an error occured as {err}")           


def readfile():
    try:
        name = input("Enter the name of the file you want to read:")
        path = Path(name)
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(f"Your file content is:\n{content}")
        else:
            print("ERROR file name does not exists")
    except Exception as err:
        print(f"an error occured as {err}")

def updatefile():
    try:
        name = input("Enter the name of the file you want to update:")
        path = Path(name)
        if path.exists():
            print("Operations")
            print("1.Renaming the file")
            print("2.Appending the content")
            print("3.Overwriting the file")
            choice = int(input("Enter your option:"))
            if choice == 1:
                newname = input("Enter your new file name:- ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename (new_path)
                    print("File renamed successfully")
                else:
                    print("ERROR file name already exists")
            elif choice == 2:
                with open(path,"a") as fs:
                    data = input("Enter the data you want to append in the file:")
                    fs.write(" \n" + data) 
                print("File appended successfully") 
            elif choice == 3:
                with open(path,"w") as fs:
                    data = input("What do you want to overwrite?:- ")
                    fs.write(" \n"+data) 
                print("Successfully Overwritten")
    except Exception as err:
        print(f"an error occured as {err}")
                            

def deletefile():
    try:
        name=input("Enter the nameof your file:- ")
        path=Path(name)
        if path.exist():
            path.unlink()
            print("File deleted successfully")    
        else:
            print("Error file does not exists")
    except Exception as err:
        print(f"an error occured as {err}")       
         

   
 
print("Press 1 for Creating a file:")
print("Press 2 for Reading a file:")
print("Press 3 for Updating a file:")
print("Press 4 for Deleting a file:")

a = int(input("\nTell your response:- "))
if a == 1:
    createfile()
if a == 2:    
    readfile()
if a == 3:
    updatefile()
if a == 4:
    deletefile()