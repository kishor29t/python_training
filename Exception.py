# list = ["one","two","three"]
# print(list[0])
# try:
#     print(list[5])
# except Exception as e:
#     print("error in array")    
# print("this is the last line")
# num=input("enter num 1:")
# num2=input("enter num 2:")
# try:

#    if num.isnumeric()==False:
#        raise("num is not number")
#    elif num2.isnumeric()==False:
#        raise("num2 is not number")
#    else:
#         res = int(num)+int(num2)
#         print(str(res)) 
# except Exception as e:
#     print(e)

# num=int(input("enter number:"))
# try:
   
#     if num>100:
#         raise("number is greater than 100")
#     else: 
#         print("ok...")        
# except Exception as e:
#          print(e)  
#  
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
 try:

    if a.isnumeric()==False:
       raise("a is not number")
    elif b.isnumeric()==False:
       raise("b is not number")
    elif c.isnumeric()==False:  
        raise("c is not number")
   else:
       largest = max(a, b, c)
        print("The largest number is:", largest)

    except Exception as e:
     print(e)