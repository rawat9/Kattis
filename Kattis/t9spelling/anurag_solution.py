keypad = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z'],
}

tc = int(input())

for _ in range(tc):
    message = input()
    
    for k, v in keypad.items():
        for m in message:
            if m in v:
                print(v.index(m))
