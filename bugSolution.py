def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return sum(numbers) / len(numbers)