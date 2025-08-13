
'''
Caching Expensive Calculations
You are optimizing performance for a system that frequently repeats the same heavy calculations (e.g., a backend system or a financial calculator).
Tasks:
Create a decorator called cache_results:
Use a dictionary to store past results based on arguments.
If the same arguments are passed again, return the cached result.
Otherwise, compute the result, cache it, and return the new value.
Apply it to a function multiply(a, b):
It simply returns the product of two integers.
The decorated function should:
Return "Computed: result" for new computations.
Return "From Cache: result" for repeated calls with the same arguments.
'''

def cache_results(func):
    cache = {}

    def wrapper(a, b):
        key = (a, b)
        if key in cache:
            return f"From Cache: {cache[key]}"
        else:
            result = func(a, b)
            cache[key] = result
            return f"Computed: {result}"

    return wrapper

@cache_results
def multiply(a: int, b: int) -> int:
    return a * b
