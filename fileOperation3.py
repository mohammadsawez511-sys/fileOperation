import os
os.chdir("D:\\product")


with open("product.txt","a+")as f:
    f.seek(0)
    pname = input("enter product name :")
    pID = int(input("enter product id :"))
    qty = int(input("enter qty : "))
    price = int(input("enter price :"))
    f.write(f"{pname},{pID},{qty},{price}\n")
    f.seek(0)
    print(f.read())
