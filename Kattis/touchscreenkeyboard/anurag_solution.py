keys = "qwertyuiop asdfghjkl zxcvbnm"
keyboard = keys.split()


def find_distance(word):
    distances = []
    for letter in word:
        if letter in keyboard[0]:  # row 1
            distances.append((0, keyboard[0].find(letter)))
        elif letter in keyboard[1]:  # row 2
            distances.append((1, keyboard[1].find(letter)))
        else:
            distances.append((2, keyboard[2].find(letter)))  # row 3

    return distances


def calc(proposed, typed):
    distance = 0
    for p1, p2 in zip(find_distance(proposed), find_distance(typed)):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


t = int(input())
ht = {}
for _ in range(t):
    typed, entries = input().split()
    words = []
    for _ in range(int(entries)):
        proposed = input()
        words.append((calc(proposed, typed), proposed))

    for distance, word in sorted(words):
        print(word, distance)
