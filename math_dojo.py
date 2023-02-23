# Write the add method and test it by calling it 3 times, with different numbers of arguments each time
# Make sure you are able to chain methods as demonstrated above

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result +=num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

        # create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
x = md.add(5).add(2, 4, 7, 9, 5).subtract(3, 2, 3, 7, 8).result
x = md.add(9).add(1, 2, 3, 4, 5, 6).subtract(10, 11).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!
