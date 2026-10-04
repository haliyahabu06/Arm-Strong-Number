num = int(input("enter a number: "))

# Convert number to string to easily count digits and iterate over them
num_str = str(num)
num_digits = len(num_str)

running_sum = 0

# Loop through each digit to calculate the sum of powers
for digit in num_str:
    running_sum += int(digit) ** num_digits
    
    # Optional early optimization: break if the sum already exceeds the number
    if running_sum > num:
        print(f"{num} is not an Armstrong number")
        break
else:
    # This executes only if the loop finishes without breaking
    if running_sum == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
