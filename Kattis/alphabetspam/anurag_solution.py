s = input()

upper, lower, ws, symbol = 0,0,0,0

for letter in s:
    if letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1
    elif letter == '_':
        ws += 1
    else:
        symbol += 1

print(ws/len(s), lower/len(s), upper/len(s), symbol/len(s), sep='\n')

