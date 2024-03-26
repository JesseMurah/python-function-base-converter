"""
a. Write a program to convert a number from decimal notation to a number expressed in a number system whose base (radix) is a number between 2 and 9. 
The conversion is performed by repetitious divistion by the base to which a number is being converted and then taking the remainders of the division in the reverse order. 
For example, in converting to binary, the number 6 requires three such divisions: 6/2 = 3 remainder 0, 3/2 = 1 remainder 1, and finally, 1⁄2 = 0 remainder 1. 
The remainders 0, 1 and 1 are put in the reverse order so that the binary equivalent of 6 is equal to 110.


b. Modify the program so that it can perform a conversion in the case when the base is a number between 11 and 27. 
Number systems with bases greater than 10 require more symbols. Therefore, use capital letters. 
For example, a hexadecimal system requires 16 digits: 0, 1.......A, B, C, D, E, F. In this system, decimal number 26 is equal to 1A.
"""


#a. using the repitious division process between base 2 and base 9:

def decimalToBase(decimal_num, base):
    #Input validation
    if base < 2 or base > 9:
        return "Error: it must be between 2 and 9"
    
    if decimal_num == 0:
        return 'O'
    
    #repitious division process
    reminders = []
    while decimal_num:
        rem = decimal_num % base
        reminders.append(str(rem))
        decimal_num //= base

    #reverse the list of remainders and concatenate them
    converted_number = ''.join(reminders[::-1])
    return converted_number


decimal_num = 20
base = 5
converted_number = decimalToBase(decimal_num, base)
print(f"The decimal number {decimal_num} in base {base} is: {converted_number}")



"""
#b. by modifying the code in (a), we want to perform a converison between base 11 and 27
def decimalToBase(decimal_num, base):
    #Input validation
    if base < 11 or base > 27:
        return "Error: it must be between 11 and 27"
    
    if decimal_num == 0:
        return 'O'
    
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #repitious division process
    reminders = []
    while decimal_num:
        rem = decimal_num % base
        reminders.append(str(symbols[rem]))
        #reminders.append(str(rem))
        decimal_num //= base

    #reverse the list of remainders and concatenate them
    converted_number = ''.join(reminders[::-1])
    return converted_number


decimal_num = 10000000
base = 25
converted_number = decimalToBase(decimal_num, base)
print(f"The decimal number {decimal_num} in base {base} is: {converted_number}")

"""


