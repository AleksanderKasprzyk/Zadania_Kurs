import time

cache = {}

def timing_decorator(function):
    def wrapper(element):
        if element in cache:
            result = cache[element]
            operation_time = 0
        else:
            start_time = time.time()
            result = function(element)
            end_time = time.time()
            operation_time = end_time - start_time
            cache[element] = result
        return result, operation_time
    return wrapper

@timing_decorator
def silnia(number):
    if number == 0:
        return 1
    else:
        return number * silnia(number - 1)

values_to_check = [1, 9, 27, 88, 175, 299, 512, 1000, 1024, 1200, 1500]

with open("calculation_results.txt", mode="w") as file_stream:
    for value in values_to_check:
        result, operation_time = silnia(value)
        file_stream.write(f"The calculation time of the silnia for value {value} is {operation_time:.6f} seconds.\n")
        print(f"Value: {value}, Time: {operation_time}")

print("Results recorded in calculation_results.txt")
