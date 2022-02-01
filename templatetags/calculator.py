from cmath import cos, sin
from django import template
import math
ERROR_MESSAGE = "Cast string to float Exception ... !"
register = template.Library()

def SinAngle(value):
    try:
       number = float(value)
       answer = sin(number)
       return answer
    except:
        raise ValueError(ERROR_MESSAGE) 
def CosAngle(value):
    try:
        number = float(value)
        answer = cos(number)
        return answer
    except:
        raise ValueError(ERROR_MESSAGE)             
def TanAngle(value):
    try:
        number = float(value)
        answer = SinAngle(number) / CosAngle(number)
        return answer
    except:
          raise ValueError(ERROR_MESSAGE)   

def Sqrt(value):
    try:
        number_to_root = float(value)
        root = math.sqrt(number_to_root)
        return root
    except:
        raise ValueError(ERROR_MESSAGE)   

def Power(value,args):
    try:
        first_number = float(value)
        power_number = float(args)
        answer = math.pow(first_number,power_number)
        return answer
    except:
        raise ValueError(ERROR_MESSAGE)    

def sum(value,args):
    try:
        first_number = float(value)
        second_number = float(args)
        answer = first_number + second_number
        return answer
    except:
        raise ValueError(ERROR_MESSAGE)  
def Minuse(value,args):
    try:
        first_number = float(value)
        second_number = float(args)
        answer = first_number - second_number
        return answer
    except:
        raise ValueError(ERROR_MESSAGE)
def Multiple(value,args):
    try:
        first_number = float(value)
        second_number = float(args)
        answer = first_number * second_number
        return answer
    except:
        raise ValueError(ERROR_MESSAGE)  
def Divide(value,args):
    try:
        first_number = float(value)
        second_number = float(args)
        answer = first_number / second_number
        return answer
    except:
        raise ValueError(ERROR_MESSAGE)                
register.filter("sum",sum)
register.filter("min",Minuse)
register.filter("mul",Multiple)
register.filter("div",Divide)
register.filter("pow",Power)
register.filter("sqrt",Sqrt)
register.filter("sin",SinAngle)
register.filter("cos",CosAngle)
register.filter("tan",TanAngle)

