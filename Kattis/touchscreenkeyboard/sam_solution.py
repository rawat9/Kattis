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

    for rows in keyboard:
        y+=1
        for string in rows:
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
    return w2, d


def solution(k1,k2,typed_w1,typed_w2,sc_words1,sc_words2):
    for i in range(int(k1)):
        w2, d = distance_w_to_w(typed_w1,sc_words1[i])
        print(w2,d)
    for i in range(int(k2)):
        w2, d = distance_w_to_w(typed_w2,sc_words2[i])
        print(w2,d)


if __name__ == '__main__':
    keyboard = [['qwertyuiop'],
                ['asdfghjkl'],
                ['zxcvbnm']]
    n = input()
    typed_w1, k1 = input().split()
    sc_words1 = []
    for i in range(int(k1)):
       sc_words1.append(input())
    typed_w2, k2 = input().split()
    sc_words2 = []
    for i in range(int(k2)):
        sc_words2.append(input())
    solution(k1, k2, typed_w1, typed_w2, sc_words1, sc_words2)

'''
PRESENT OUTPUT: (still has to be sorted in ascending order... HELP!)
iopc 7
icpc 3
gcpc 7
wsx 3
edc 0
rfv 3
plm 17
qed 4
'''
            
