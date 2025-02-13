''' Create a function that writes the Fibonacci series up to n numbers.'''
def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series[:n]
