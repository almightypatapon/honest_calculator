class HonestCalc:
    msg = {
            0: "Enter an equation",
            1: "Do you even know what numbers are? Stay focused!",
            2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            3: "Yeah... division by zero. Smart move...",
            4: "Do you want to store the result? (y / n):",
            5: "Do you want to continue calculations? (y / n):",
            6: " ... lazy",
            7: " ... very lazy",
            8: " ... very, very lazy",
            9: "You are",
            10: "Are you sure? It is only one digit! (y / n)",
            11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
            12: "Last chance! Do you really want to embarrass yourself? (y / n)"}

    operations = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    def __init__(self):
        self.memory = 0
        self.x, self.operation, self.y, self.result = None, None, None, None

    def read_inp(self):
        while True:
            try:
                print(self.msg[0])
                x, operation, y = input().split()
                x = self.memory if x == 'M' else float(x)
                y = self.memory if y == 'M' else float(y)
                self.x, self.operation, self.y = x, operation, y
                self.lazy_msg()
                if operation not in self.operations:
                    print(self.msg[2])
                elif operation == '/' and not y:
                    print(self.msg[3])
                else:
                    break
            except ValueError:
                print(self.msg[1])
                continue

    def evaluate(self):
        self.result = self.operations[self.operation](self.x, self.y)
        print(self.result)
        if input(f'{self.msg[4]}\n') == 'y':
            self.store_msg()

    def lazy_msg(self):
        msg = ""
        if self.is_one_digit(self.x) and self.is_one_digit(self.y):
            msg += self.msg[6]
        if (self.x == 1 or self.y == 1) and self.operation == '*':
            msg += self.msg[7]
        if (not self.x or not self.y) and self.operation in '+-*':
            msg += self.msg[8]
        if msg:
            print(self.msg[9] + msg)

    def store_msg(self):
        if self.is_one_digit(self.result):
            if input(f'{self.msg[10]}\n') == 'y':
                if input(f'{self.msg[11]}\n') == 'y':
                    if input(f'{self.msg[12]}\n') == 'y':
                        self.memory = self.result
        else:
            self.memory = self.result

    @staticmethod
    def is_one_digit(v):
        return -10 < v < 10 and not v % 1

    def main(self):
        while True:
            self.read_inp()
            self.evaluate()
            if input(f'{self.msg[5]}\n') != 'y':
                break


if __name__ == '__main__':
    hc = HonestCalc()
    hc.main()
