def get_numbers():
    ''' The function that allows to get the numbers to sort'''

    print("Please provide the numbers, one by one.")
    print("Hit enter to atfer type a number.")
    print("And send 's' to sort the list of numbers")

    numbers = []
    number = 0
    while True:
        try:
            number = input("Please provide a integer number and hit <enter>: ")
            number = int(number)
            numbers.append(number)
        except:
            if number == 's':
                break
    
    if len(numbers) == 0:
        raise Exception("You provided an empty list of numbers")

    return numbers

print(get_numbers())

