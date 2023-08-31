"""
@Author :: K HARI HARA KUMAR
Program about :: a div(dividend, divisor) function with 2 decorators
Date created :: 11-03-2023
Date modified :: 12-03-2023
modules used :: logging
subtasks : 1. create a decorator which checks for divisor (0)
              if yes, print invalid
           2. a decorator that logs the messages (logging module)
           3. creating div(arg1,arg2) and decorate it

"""


import logging


def divisor1(func):

    def div_b(a, b):
        if b == 0:
            print("invalid")
            return
        return func(a, b)
    return div_b


def logger(func):

    def basiclog(a, b):
        logging.basicConfig(filename='111.log', filemode="a+", format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info("starting function div1")
        if b != 0:
            logging.info("passed")
        else:
            logging.warning("invalid")
        return func(a, b)
    return basiclog


@logger
@divisor1
def div1(a, b):
    print(a / b)


if __name__ == "__main__":
    div1(12, 2)
    div1(10, 0)
    div1(11, 0)
    div1(14, 7)

"""
div1 function which is decorated by two decorators divisor1() and logger() 
using syntax 
@divisor1
@logger
In divisor1 there is a nested function which checks for the main function's 2nd value 
whether it is 0 or not
divisor1 takes main function as argument 
