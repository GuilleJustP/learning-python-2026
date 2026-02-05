def menu():

    print("=== STATISTICS CALCULATOR ===")
    print("1. Calculate average")
    print("2. Find max and min")
    print("3. Calculate sum")
    print("4. Exit")

def calculate_average(data):
    average = sum(data) / len(data)
    return average

def find_max_min(data):
    maximum = max(data)
    minimum = min(data)
    return maximum, minimum

def calculate_sum(data):
    total = sum(data)
    return total


numbers = []
print("Enter 5 numbers:")
for i in range(5):
    numbers.append(float(input(f"Number {i+1}: ")))
    
while True:
    menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        avg = calculate_average(numbers)
        print(f"Average: {avg}")
    elif choice == '2':
        maximum, minimum = find_max_min(numbers)
        print(f"Max: {maximum}, Min: {minimum}")
    elif choice == '3':
        total = calculate_sum(numbers)
        print(f"Sum: {total}")
    elif choice == '4':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")