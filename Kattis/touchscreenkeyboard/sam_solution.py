# source: https://open.kattis.com/problems/touchscreenkeyboard

def l_coordinates(word, counter):
    if counter == len(word):
        return letters_coordinates
    else:
        letter = word[counter]
        if letter in keyboard[0]:  # row 1
            letters_coordinates.append((0, keyboard[0].find(letter)))
        if letter in keyboard[1]:  # row 2
            letters_coordinates.append((1, keyboard[0].find(letter)))
        if letter in keyboard[2]:  # row 3
            letters_coordinates.append((2, keyboard[0].find(letter)))
        return l_coordinates(word, counter+1)


def distance_w_to_w(typed_w, w2):
    # distance = 0
    print(l_coordinates(w2, 0))
    print(l_coordinates(typed_w, 0))
    for p1, p2 in zip(l_coordinates(w2, 0), l_coordinates(typed_w, 0)):
        print(p1, p2)


# def solution(k, typed_w, sc_words):
#     lst = [distance_w_to_w(typed_w, sc_words[i]) for i in range(int(k))]
#     for d, w2 in sorted(lst):
#         print(f'{w2} {d}')


if __name__ == '__main__':
    keyboard = 'qwertyuiop asdfghjkl zxcvbnm'.split()
    print(keyboard)
    print('DISTANCE:', distance_w_to_w('epc', 'sci'))

    # n = input()
    # for _ in range(int(n)):
    #     typed_w, k = input().split()
    #     sc_words = []
    #     for _ in range(int(k)):
    #         sc_words.append(input())
    #     solution(k, typed_w, sc_words)

'''
INPUT:
2
ifpv 3
iopc
icpc
gcpc
edc 5
wsx
edc
rfv
plm
qed

'''