"""
Data Analyzer - Project #2
Analyzes numerical data and provides insights
Author: Guillermo Justiniano Poehlmann
Date: January 28, 2026
"""

def menu ():
    print("\n=== DATA ANALYZER MENU ===")
    print("1. Calculate mean")
    print("2. Calculate median")
    print("3. Calculate mode")
    print("4. Calculate range")
    print("5. Analize every data (1-4)")
    print("6. Exit")

def calculate_mean(data):
    mean = sum(data) / len(data)
    return mean
    
def calculate_median(data):
    median = sorted(data)
    n = len(median)
    mid = n // 2
    if n % 2 == 0:
        return (median[mid - 1] + median[mid]) / 2
    elif n % 2 != 0:
        return median[mid]
        
def calculate_mode(data):
    frecuency = {}
    for num in data:
        if num in frecuency:
            frecuency[num] += 1
        else:
            frecuency[num] = 1
            mode = max(frecuency, key=frecuency.get)
    return mode
        
def calculate_range(data):
    data_range = max(data) - min(data)
    return data_range
data = []
print("Enter 5 numbers:")
for i in range(5):    
    data.append(float(input(f"Number {i+1}: ")))

while True:
    menu()
    choice = input("Choose an option (1-6): ")
        
    if choice == '1':
            mean = calculate_mean(data)
            print(f"Mean: {mean}")
    elif choice == '2':
            median = calculate_median(data)
            print(f"Median: {median}")
    elif choice == '3':
            mode = calculate_mode(data)
            print(f"Mode: {mode}")
    elif choice == '4':
            data_range = calculate_range(data)
            print(f"Range: {data_range}")
    elif choice == '5':
            mean = calculate_mean(data)
            median = calculate_median(data)
            mode = calculate_mode(data)
            data_range = calculate_range(data)
            print(f"\nMean: {mean}")
            print(f"Median: {median}")
            print(f"Mode: {mode}")
            print(f"Range: {data_range}")
    elif choice == '6':
            print("Exiting the Data Analyzer. Goodbye!")
            break
    else:
            print("Invalid choice. Please select a valid option.")
