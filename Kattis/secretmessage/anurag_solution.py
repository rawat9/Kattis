import math

class Encrypt:
    def rotate(self, matrix):
        matrix = list(map(list, zip(*reversed(matrix))))
        return matrix

    def next_square(self, n):
        if math.sqrt(n)**2 == n:
            return n
        else:
            return int(math.pow(math.floor(math.sqrt(n)) + 1, 2))

    def create_table(self, message):
        M = len(message)
        padded = message + "*" * (self.next_square(M) - M)
        k = int(math.sqrt(self.next_square(M)))

        return [list(padded[i:i+k]) for i in range(0, len(padded), k)]

    def getSecret(self, table):
        result = ""
        secret = self.rotate(table)
        for s in secret:
            result += "".join(list(filter(lambda x: x != '*', s)))
        
        return result

if __name__ == "__main__":
    e = Encrypt()
    n = int(input())
    for _ in range(n):
        message = input()
        table = e.create_table(message)
        print(e.getSecret(table))
