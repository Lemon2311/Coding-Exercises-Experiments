# A generator function that yields numbers from 0 to n
def count_up_to(n):
    count = 0
    while count < n:
        yield count
        count += 1

#chose to iterate with for loop instead of using next() function which works as well
for number in count_up_to(5):
    print(number)  # Output: 0 1 2 3 4
