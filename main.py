# 1.	Write a program that will print the following to the console using the print() function

from random import random


# string_sequence = "#######"
# current_print = ''
# for char in string_sequence:
#     current_print += char
#     print(current_print)

# 2.	Write a program that will print the following to the console using the print() function. 
# Pay close attention to the spacing of the characters and try to match it exactly!

# string1 = ' # # # #'
# string2 = '# # # #'

# total_count = range(8)

# for num in total_count:
#     if (num%2):
#         print(string2)
#     else:
#         print(string1)

# 3.	Write a program that takes a number as input from the user, counts all of the digits in that number, 
#  and prints the digit count to the console.

# user_number = input('Please enter an integer number: ')
# digit_count = 0

# for digit in user_number:
#     digit_count += 1

# if digit_count > 1:
#     print(f'The number {user_number} has {digit_count} digits')
# else:
#     print(f'The number {user_number} has {digit_count} digit')

# 4.	Find the factorial of a given number. A factorial means to multiply all of 
# the numbers of a given number counting down to 1. 

# user_number = int(input('Please enter an integer number: '))
# factorial_range = range(int(user_number),0,-1)
# factorial_result = 1

# for num in factorial_range:
#     factorial_result *= num

# print(f'The factorial of {user_number} is {factorial_result}')



# 5.	Write a program that will allow a user to play a “guess the number” game. This program should only allow the user five guesses to guess the correct number, and display messages for the three following cases:
# a.	A correct guess (which should end the program)
# b.	An incorrect guess, but there are still guesses left
# c.	An incorrect guess, but there are no more guesses left and the program is over. This should also display the correct number to the user
# d.	BONUS: Offer a “hint” after three wrong guesses (could be a range of numbers that the number falls within, for instance)
# e.	BONUS: Generate the number randomly every time the program runs.

import random
lower_limit = 0
upper_limit = 250

correct_number = random.randint(lower_limit,upper_limit)
guess_is_wrong = True
total_guesses = 5
guess_count = 0
ask_hint_after_3 = True

print('Welcome to the Guessing Game Good Luck!')
print(f'You have a total of {total_guesses} guesses: ')
while(guess_is_wrong and guess_count < total_guesses):
    user_guess = upper_limit + 1
    while user_guess < lower_limit or user_guess > upper_limit:
        user_guess = int(input(f'Please enter a guess as an integer between {lower_limit} and {upper_limit}: '))
        if user_guess > upper_limit:
            print(f'Your guess is above {upper_limit}, try again')
        elif user_guess < lower_limit:
            print(f'Your guess is below {lower_limit}, try again')
        else:
            print(f'Your guess is {user_guess}')

    if user_guess == correct_number:
        guess_count += 1
        print('Correct!!') 
        print(f'The random number was {correct_number}')
        if guess_count == 1:
            print(f'Amazing!! You got the number correct on the first guess')
        elif guess_count == total_guesses:
            print(f'Cutting things close! You got it on the last guess')
        else:
            print(f'You got the number correct in {guess_count} guesses')
        print(f'You are a winner!!')
        if ask_hint_after_3:
            print('Amazing! You got the number right without a hint!')

        guess_is_wrong = False
    elif user_guess < correct_number:
        guess_count += 1
        lower_limit = user_guess
        print('Your guess is less than the unknown number')
        if guess_count == total_guesses - 1:
            print('Careful! You only have one guess remaining!')
            if ask_hint_after_3:
                user_response = input('Last chance! Do you want a hint? (Y or N)')
                if user_response.capitalize() == 'Y':
                    upper_limit = random.randint(correct_number+1,upper_limit)
                    lower_limit = random.randint(lower_limit,correct_number-1)
                    print(f'HINT: The number is between {lower_limit} and {upper_limit}')
                    ask_hint_after_3 = False
                else:
                    print('Wow you are stubborn! Good luck')    
        elif guess_count > 2 and guess_count < total_guesses and ask_hint_after_3:
            user_response = input(f'You have {guess_count} incorrect guess. Do you want a hint? (Y or N)')
            if user_response.capitalize() == 'Y':
                upper_limit = random.randint(correct_number+1,upper_limit)
                lower_limit = random.randint(lower_limit,correct_number-1)
                print(f'HINT: The number is between {lower_limit} and {upper_limit}')
                ask_hint_after_3 = False
            else:
                print('I like your determination. Good luck')    
        elif guess_count == total_guesses:
            print(f'So sorry! The correct answer was {correct_number}')
            print(f'You did not guess the correct answer in {total_guesses} guesses')
            print('You are a loser')
        else:
            print(f'You have {total_guesses - guess_count} guesses remaining')
    else:
        guess_count += 1
        upper_limit = user_guess
        print('Your guess is greater than the unknown number')
        if guess_count == total_guesses - 1:
            print('Careful! You only have one guess remaining!')
            if ask_hint_after_3:
                user_response = input('Last chance! Do you want a hint? (Y or N)')
                if user_response.capitalize() == 'Y':
                    upper_limit = random.randint(correct_number+1,upper_limit)
                    lower_limit = random.randint(lower_limit,correct_number-1)
                    print(f'HINT: The number is between {lower_limit} and {upper_limit}')
                    ask_hint_after_3 = False
                else:
                    print('Wow you are stubborn! Good luck')      
            
        elif guess_count > 2 and guess_count < total_guesses and ask_hint_after_3:
            user_response = input(f'You have {guess_count} incorrect guess. Do you want a hint? (Y or N)')
            if user_response.capitalize() == 'Y':
                upper_limit = random.randint(correct_number+1,upper_limit)
                lower_limit = random.randint(lower_limit,correct_number-1)
                print(f'HINT: The number is between {lower_limit} and {upper_limit}')
                ask_hint_after_3 = False
            else:
                print('I like your determination. Good luck')      
        elif guess_count == total_guesses:
            print(f'So sorry! The correct answer was {correct_number}')
            print(f'You did not guess the correct answer in {total_guesses} guesses')
            print('You are a loser')
        else:
            print(f'You have {total_guesses - guess_count} guesses remaining')

# 6.	Write a program that will take user input for the number of hours they have worked 
# this week and their payrate. The output should show their total pay for the week. Be sure to 
# account for overtime (if they work more than 40 weeks, for example, then any hours over 40 
# should be calculated at the standard pay rate multiplied by an overtime modifier).

# regular_work_week_hours = 40
# regular_pay_rate = 15.50
# over_time_multiplier = 1.5
# overtime_pay_rate = regular_pay_rate * over_time_multiplier
# grand_total_net_pay = 0
# grand_total_base_pay = 0
# grand_total_overtime_pay = 0
# grand_total_hours = 0
# grand_total_base_hours = 0
# grand_total_overtime_hours = 0
# week_count = 0
# keep_entering_data = True

# while(keep_entering_data):
#     user_input = input(f'Enter the total number of hours worked in Week {week_count+1} (Enter Q for Quit if done): ')
#     if user_input.capitalize() == 'Q':
#         keep_entering_data = False
#         if(week_count):
#             print(f'**** Summary for All Weeks ****')
#             print(f'Total number of weeks: {week_count}')
#             print(f'Total hours worked: {grand_total_hours}')
#             print(f'Total base hours worked: {grand_total_base_hours}')
#             print(f'Base pay rate: ${regular_pay_rate}')
#             print(f'Total base pay: ${grand_total_base_pay}')
#             print(f'Total overtime hours : {grand_total_overtime_hours}')
#             print(f'Overtime pay rate: ${overtime_pay_rate}')
#             print(f'Total overtime pay: ${grand_total_overtime_pay}')
#             print(f'Total pay over all weeks: ${grand_total_net_pay}')
#             print(f'Average hours per week = {(grand_total_hours/week_count):.1f}')
#             print(f'Average pay per week = ${(grand_total_net_pay/week_count):.2f}')
#     else:
#         week_count += 1
#         hours_worked_in_current_week = int(user_input)
#         print(f'You worked a total of {hours_worked_in_current_week} hours during Week {week_count}')

#         if hours_worked_in_current_week > regular_work_week_hours:
#             base_hours_in_current_week =  regular_work_week_hours
#             overtime_hours_in_current_week = hours_worked_in_current_week - regular_work_week_hours
                      
#         else:
#             base_hours_in_current_week = hours_worked_in_current_week
#             overtime_hours_in_current_week = 0
                    
        
#         base_pay_in_current_week = base_hours_in_current_week * regular_pay_rate
#         overtime_pay_in_current_week = overtime_hours_in_current_week * overtime_pay_rate
#         net_pay_in_current_week = base_pay_in_current_week + overtime_pay_in_current_week

#         print(f'---- Summary for Week {week_count} ----')
#         print(f'Total hours worked this week: {hours_worked_in_current_week}')
#         print(f'Base hours worked this week: {base_hours_in_current_week}')
#         print(f'Base pay rate: ${regular_pay_rate}')
#         print(f'Base pay this week: ${base_pay_in_current_week}')
#         print(f'Overtime hours worked this week: {overtime_hours_in_current_week}')
#         print(f'Overtime pay rate: ${overtime_pay_rate}')
#         print(f'Overtime pay this week: ${overtime_pay_in_current_week}')
#         print(f'Total pay this week: ${net_pay_in_current_week}')
                
#         grand_total_base_hours += base_hours_in_current_week
#         grand_total_overtime_hours += overtime_hours_in_current_week
#         grand_total_hours += hours_worked_in_current_week
#         grand_total_base_pay += base_pay_in_current_week
#         grand_total_overtime_pay += overtime_pay_in_current_week
#         grand_total_net_pay += net_pay_in_current_week










