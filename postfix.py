#Postfix Calculator Lab by Zion Choi

class postfix():

    #initializes with one input, in the future could use args for empty constructor
    #but this works in the meantime, reverses the input to consider order of operations
    def __init__(self, input):
        self.input = [i for i in input.split()][::-1]

    #setter for user input
    def set_input(self, input):
        self.input = [i for i in input.split()][::-1]

    #tests if something is a number (float)
    def is_number(self, test):
        try:
            float(test)
            return True
        except:
            return False

    #tests if something is an operation
    def is_operation(self, test):
        if test not in ['+', '-', '*', '/']:
            return False
        return True

    #tests if two numbers are consecutive, essentially lets the program know when to do
    #an operation.
    def is_consecutive(self, test):
        if self.is_operation(test[0]) and self.is_number(test[1]) and self.is_number(test[2]):
            return True
        return False

    #does the operation for the given list of three characters
    def operation(self, test):
        if test[0] == '+':
            return float(test[2]) + float(test[1])
        if test[0] == '-':
            return float(test[2]) - float(test[1])
        if test[0] == '*':
            return float(test[2]) * float(test[1])
        if test[0] == '/':
            return float(test[2]) / float(test[1])

    #calculate method returns the correct answer. As a recursive function, it will stop
    #when there is only the result left. While the length is greater than 1, it will grab
    #the last three indexes until it finds a consecutive pair => then it does the operation
    def calculate(self):
        if len(self.input) == 1:
            return self.input[0]
        for i in range(0, len(self.input)):
            test = [self.input[i], self.input[i+1], self.input[i+2]]
            if self.is_consecutive(test):
                self.input[i] = str(self.operation(test))
                del self.input[i+1]
                del self.input[i+1]
                return self.calculate()
        return self.calculate()