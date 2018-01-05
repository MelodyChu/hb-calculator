from arithmetic import *

print "instruction manual here"

while True:
    user_input = raw_input(">")
    input_list = user_input.split()
    x = int(input_list[1])
    y = int(input_list[2])

    #break the user input into a list ['+','2','3']
    # print input_list= int(input_list[2])
    if input_list[0] == "+":
        sum1 = 0
        for number in range(1,len(input_list)):
            sum1 += int(input_list[number])
        print sum1
    elif input_list[0] == "-" and len(input_list) == 3:
        subtration = subtract(int(input_list[1]), int(input_list[2]))
        print subtration
    elif input_list[0] == "*" and len(input_list) == 3:
        multiplication = multiply(int(input_list[1]), int(input_list[2]))
        print multiplication
    elif input_list[0] == "/" and len(input_list) == 3:
        division = divide(int(input_list[1]), int(input_list[2]))
        print division
    elif input_list[0] == "square" and len(input_list) == 2:
        squares = square(int(input_list[1]))
        print squaress
    elif input_list[0] == "cube" and len(input_list) == 2:
        cubed = cube(int(input_list[1]))
        print cubed
    elif input_list[0] == "pow" and len(input_list) == 3:
        power = pow(int(input_list[1]), int(input_list[2]))
        print power
    elif input_list[0] == "mod" and len(input_list) == 3:
        calcmod = mod(int(input_list[1]), int(input_list[2]))
        print calcmod
    elif user_input == 'q':
        break
    else:
        print "Enter valid calculation!"



# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         try:
#             initializer = next(it)
#         except StopIteration:
#             raise TypeError('reduce() of empty sequence with no initial value')
#     accum_value = initializer
#     for x in it:
#         accum_value = function(accum_value, x)
#     return accum_value

