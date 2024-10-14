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

numbers = get_numbers()

for index_to_verify, number_to_verify in enumerate(numbers):
    index_to_compare = index_to_verify + 1
    if index_to_compare == len(numbers):
        break

    while index_to_compare < len(numbers):
        if numbers[index_to_compare] < numbers[index_to_verify]:
            numbers[index_to_verify], numbers[index_to_compare] = numbers[index_to_compare], numbers[index_to_verify]
        index_to_compare += 1

print(numbers)

