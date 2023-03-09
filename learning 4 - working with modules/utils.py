class Comparison:

    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        max = self.numbers[0]
        for number in self.numbers:
            if number > max:
                max = number
        return max

    def find_lowest(self):
        lowest = self.numbers[0]
        for number in self.numbers:
            if number < lowest:
                lowest = number
        return lowest
