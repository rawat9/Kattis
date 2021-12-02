# source: https://open.kattis.com/problems/touchscreenkeyboard
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


def create_dict(keyboard):
    coord_dict_l = {}
    x = -1
    y = -1

    for string in keyboard:
        y+=1
        for letter in string:
            x+=1
            if letter==string[0]:
                x=0
            coord_dict_l[letter] = x,y
    return coord_dict_l


def distance_l_to_l(l1, l2, keyboard):
    coord_dict_l = create_dict(keyboard)
    x1,y1 = coord_dict_l.get(l1)
    x2,y2 = coord_dict_l.get(l2)
    return abs(x1-x2)+abs(y1-y2) 


def distance_w_to_w(typed_w, w2):
    d = 0
    for i in range(len(typed_w)):
        d += distance_l_to_l(typed_w[i], w2[i], keyboard)
    return d, w2


def solution(k, typed_w, sc_words):
    lst = [distance_w_to_w(typed_w, sc_words[i]) for i in range(int(k))]
    for d,w2 in sorted(lst):
        print(f'{w2} {d}')


if __name__ == '__main__':
    keyboard = ['qwertyuiop',
                'asdfghjkl',
                'zxcvbnm']
    n = int(input())
    for _ in range(n):
        typed_w, k = input().split()
        sc_words = []
        for i in range(int(k)):
            sc_words.append(input())
        solution(k, typed_w, sc_words)
