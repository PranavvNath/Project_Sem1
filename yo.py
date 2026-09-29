user_input = input("Enter integers separated by spaces or commas: ")

numbers = [int(x) for x in user_input.replace(",", " ").split()]

cubed_list = [num ** 3 for num in numbers]

print("Cubed list:", cubed_list)