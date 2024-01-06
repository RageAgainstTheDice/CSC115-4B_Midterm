print('Name: Arian Djahed')
print('Email: axd1587@miami.edu')
print('Course: CSC115-4B (Python Programming for Everyone)')
print('Major: Undecided')
# Now the actual program shall commence.
print()
starting_num = int(input('Enter starting number of organisms: '))
while starting_num < 0:
    print('The starting number cannot be negative. Please enter an appropriate value:', end=' ')
    starting_num = int(input())
# Here, I am simply defining the variable for the starting population and making sure that the value is nonnegative.
# If so, then the user is prompted to input another value.
pop_up = float(input('Enter average population increase (as a percentage): '))
while pop_up < 0 or pop_up > 100:
    print('The average population increase must be between 0 and 100. Please enter an appropriate value:', end=' ')
    pop_up = float(input())
# Now, I have done the same for the population rate; the while loop ensures that the program will not run unless
# the value is between 0 and 100 (inclusive).
days = int(input('Enter the number of days the population will be left to multiply: '))
while days < 0 or days > 30:
    print('The number of days must be between 0 and 30. Please enter an appropriate value:', end=' ')
    days = int(input())
# I repeat the same process one more time for the last variable that requires user input, now making sure that the value
# is between 0 and 30 (inclusive).
print()
print('Day Approximate    Population')
current_day = 1
spaces1 = '                  '
spaces2 = '                 '
# For formatting purposes, I printed a blank line so that the chart containing the values may be separate from the lines
# containing the inputs. I also defined two separate spaces variables to use in the upcoming while loop so that when the
# number of days reaches the double-digits, the associated population values will not be misaligned.
while current_day <= days:
    if current_day < 10:
        print(str(current_day) + str(spaces1) + str(starting_num))
    else:
        print(str(current_day) + str(spaces2) + str(starting_num))
    starting_num = starting_num + ((pop_up / 100) * starting_num)
    current_day += 1
# This is where the actual table of values gets printed; the while loop ensures that the program will continue to output
# lines of the data table as long as values past the user's desired number of days are not printed. The nested if-else
# statement then ensures that the table remains aligned.
# This thus concludes the program.
