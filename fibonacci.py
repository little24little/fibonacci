class Fibonacci(object):
    def generate(self, length):
        sequence = []
        for index in range(length):
            if index < 2:
                sequence.append(index)
            else:
                sequence.append(sequence[index - 1] + sequence[index - 2])
        return sequence