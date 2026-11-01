import os 

os.chdir("D:\\employee")


with open("employee.txt","r") as fr,open("salary.txt","w")as fw:

    readData = fr.readlines()
    for i in readData:
        a = list(i.split())
        fw.write(f"{a[0]}  {a[-1]}\n")



    
