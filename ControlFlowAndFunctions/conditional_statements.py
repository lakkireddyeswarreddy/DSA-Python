 
"""
While wriring the if elif else blocks write the most specific condition at the top.
Write the most occuring cases at the top, as it will save the computation time.
Precompute the conditions if they are complex and stored them in a variable.

"""

#Ternary operator
num=int(input("Enter any number : "))
print(f"{num} is an even number") if num % 2 == 0 else print(f"{num} is an odd number")

 
# """
# program for finding an number is odd or number
# """

# while True:
#     input_number=int(input("Enter any number : "))
#     if input_number % 2 ==0:
#         print(f"{input_number} is an even number")
#     elif input_number < 0:
#         print(f"{input_number} is not valid number, please enter positive number.")
#     else:
#         print(f"{input_number} is an odd number")
        
        
# """
# Program for finding an month in the english calendar based on the month number using macth 
# """
# while True:
#     month_number = int(input("Enter the month number from 1 to 12 to find the english month : "))

#     match month_number:
#         case 1:
#             print(f"{month_number} month in the english calendar is JANUARY")
#         case 2:
#             print(f"{month_number} month in the english calendar is FEBRUARY")
#         case 3:
#             print(f"{month_number} month in the english calendar is MARCH")
#         case 4:
#             print(f"{month_number} month in the english calendar is APRIL")
#         case 5:
#             print(f"{month_number} month in the english calendar is MAY")
#         case 6:
#             print(f"{month_number} month in the english calendar is JUNE")
#         case 7:
#             print(f"{month_number} month in the english calendar is JULY")
#         case 8:
#             print(f"{month_number} month in the english calendar is AUGUST")
#         case 9:
#             print(f"{month_number} month in the english calendar is SEPTEMBER")
#         case 10:
#             print(f"{month_number} month in the english calendar is OCTOBER")
#         case 11:
#             print(f"{month_number} month in the english calendar is NOVEMBER")
#         case 12:
#             print(f"{month_number} month in the english calendar is DECEMBER")
#         case _:
#             print(f"{month_number} IS NOT A VALID NUMBER, ENTER BETWEEN 1-12, THERE ARE ONLY 12 MONTHS IN THE ENGLISH CALENDAR")