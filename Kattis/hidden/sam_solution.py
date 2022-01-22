# source: https://open.kattis.com/problems/hidden

def hidden(password, message):
    if len(password)==0:
        return 'PASS'
    else:
        any_other_letter = []
        if password[0] in message:
            char_index = message.index(password[0])
            for c in password[1:]:
                if any(c==i for i in message[0:char_index]):
                    any_other_letter.append(True)
                else:
                    any_other_letter.append(False)
            if any(any_other_letter):
                return 'FAIL'
            else:
                return hidden(password[1:], message[char_index+1:])
        else:
            return 'FAIL'


n = input().split(' ')
print(hidden(n[0], n[1]))

