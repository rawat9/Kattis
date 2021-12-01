sentence = input()
words = sentence.split()

print("no" if len(words) != len(set(words)) else "yes")
