import numpy
a = int(input())
integers = numpy.arange(1, a+1)
result = numpy.arange(a).astype(str)
result = numpy.where(integers % 3 == 0, "Fizz", result)
result = numpy.where(integers % 5 == 0, "Buzz", result)
result = numpy.where(integers % 15 == 0, "FizzBuzz", result)
print(*result)