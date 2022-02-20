password, S = input().split()
is_valid = True

for char in S:
    if char in password:
        if password.index(char) != 0:
            is_valid = False
        else:
            password = password[1:]

if not is_valid and password:
    print('FAIL')
else:
    print('PASS')
