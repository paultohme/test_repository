import math
def number1(a):
    try:
        result=math.sqrt(a)
        print(result)
    except:
        if a<0:
            print("opreration can't be executed, input a positivinteger \n or positive float")
            return None
        a=int(input("enter a positive integer of float:-"))
        print(number1,result)
        



