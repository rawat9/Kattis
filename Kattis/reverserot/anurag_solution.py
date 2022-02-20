s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_." * 2

while True:
    inp = input()

    if inp == "0":
         break

    N, string = inp.split()

    res = ""
    for i in string[::-1]:
        index = s.find(i)
        res += s[index + int(N)]
    print(res)
