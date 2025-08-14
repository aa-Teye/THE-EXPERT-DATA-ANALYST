import random

def generate_numbers(count, lower, upper):
    """Generate a list of random numbers."""
    return [random.randint(lower, upper) for _ in range(count)]

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def find_max_min(numbers):
    """Find the maximum and minimum in a list."""
    return max(numbers), min(numbers)

def main():
    print("Random Number Analysis Program")
    count = 10
    lower = 1
    upper = 100

    numbers = generate_numbers(count, lower, upper)
    print(f"Generated numbers: {numbers}")

    avg = calculate_average(numbers)
    print(f"Average: {avg:.2f}")

    maximum, minimum = find_max_min(numbers)
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

    sorted_numbers = sorted(numbers)
    print(f"Sorted numbers: {sorted_numbers}")

    print("Numbers greater than average:")
    for num in numbers:
        if num > avg:
            print(num)

if __name__ == "__main__":
    main()