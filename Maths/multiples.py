# Lists every third and fifth number between 0 and 1000.
range_three = list(range(0, 1000, 3))
range_five = list(range(0, 1000, 5))

# Adds every third and fifth number between 0 and 1000 together.
sum_three = int(sum(range_three))
sum_five = int(sum(range_five))

# Since multiples of fifteen are multiples of both three and five, they'll be double added.
# So we'll need to subtract all mutiples of fifteen from the total sum to not double count those numbers.
range_fifteen = list(range(0, 1000, 15))
sum_fifteen = int(sum(range_fifteen))

# Adds the above variables together.
three_and_five_sum = int(sum_three + sum_five)
# Subtracts sum of multiples of fifteen as earlier.
total_sum = int(three_and_five_sum - sum_fifteen)

# Prints the result.
print(f"The total sum of all multiples of 3 and 5 between 0 and 1000 is {total_sum}.")

# Based on some Googling, I'm pretty sure the correct answer is 233,168.