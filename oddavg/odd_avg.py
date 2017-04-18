# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(list):
    average = []
    for n in range(len(list)):
        if list[n] % 2 !=0:
            average.append(list[n])

list = [2,4,6,8,10,12,14,16,18,20]

odd_average(list)
