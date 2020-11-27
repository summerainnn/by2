# 这是一个表达式文法
#
# [nonterminal]
# 	S L R
# [terminal]
# 	i * =
# [start]
# 	S’
# [production]
# 	S’ => S;
# 	S => L = R;
# 	S => R;
# 	L => * R;
# 	L => i;
# 	R => L;
# 对应关系
# 14	0
# 15	reduce L -> R
# 16	reduce R -> L
# 17	reduce L -> *R
# 18	reduce S -> R
# 19	reduce L -> i
# 20	reduce S -> L = R
# 21	s4
# 22	s5
# 23	s6
# 24	s11
# 25	s12
# 26	acc
# i	*	=	$	S	L	R
def index(word):
    if word == 'i':
        return 1
    elif word == '*':
        return 2
    elif word == '=':
        return 3
    elif word == '$':
        return 4
    elif word == 'S':
        return 5
    elif word == 'L':
        return 6
    elif word == 'R':
        return 7
    else:
        print('error input')
        return 0


def zt(s):
    next = LRList[s1_zt[len(s1_zt) - 1] + 1][index(s)]
    return next


with open("input.txt", 'r') as f:
    word = f.read()

with open("LR1.txt", 'r') as f:
    LR = f.readlines()

wordList = word.split(' ')
print("输入的串为： ",end='')
print(wordList)  # 输入的串
wordList.append('$')

LRList = []
for line in LR:
    LRList.append(line.split('\t'))

for line in LRList:
    line[-1] = line[-1][0:-1]
for i in range(len(LRList)):
    if i == 0:
        pass
    else:
        for j in range(len(LRList[i])):
            LRList[i][j] = int(LRList[i][j])
# 用python中的列表来实现栈操作，psuh为append，pop为pop（-1）
s1_zt = [0]
s2_word = ['$']
output = open('output.txt', 'w')
# for word in wordList:
while (1):
    x = s1_zt[len(s1_zt) - 1] + 1
    y = index(wordList[0])
    next = LRList[x][y]
    if next == 15:
        output.write('L -> R\n')
        s1_zt.pop(-1)
        s2_word.pop(-1)
        wordList.insert(0, 'R')
    elif next == 16:
        output.write('R -> L\n')
        s1_zt.pop(-1)
        s2_word.pop(-1)
        wordList.insert(0, 'R')
    elif next == 17:
        output.write('L -> *R\n')
        s1_zt.pop(-1)
        s1_zt.pop(-1)
        s2_word.pop(-1)
        s2_word.pop(-1)
        wordList.insert(0, 'L')
    elif next == 18:
        output.write('S -> R\n')
        s1_zt.pop(-1)
        s2_word.pop(-1)
        wordList.insert(0, 'S')
    elif next == 19:
        output.write('L -> i\n')
        s1_zt.pop(-1)
        s2_word.pop(-1)
        wordList.insert(0, 'L')
    elif next == 20:
        output.write('S -> L = R\n')
        s1_zt.pop(-1)
        s1_zt.pop(-1)
        s1_zt.pop(-1)
        s2_word.pop(-1)
        s2_word.pop(-1)
        s2_word.pop(-1)
        wordList.insert(0, 'S')
    elif next == 21:
        s1_zt.append(4)
        s2_word.append(wordList[0])
        wordList = wordList[1:]
    elif next == 22:
        s1_zt.append(5)
        s2_word.append(wordList[0])
        wordList = wordList[1:]
    elif next == 23:
        s1_zt.append(6)
        s2_word.append(wordList[0])
        wordList = wordList[1:]
    elif next == 24:
        s1_zt.append(11)
        s2_word.append(wordList[0])
        wordList = wordList[1:]
    elif next == 25:
        s1_zt.append(12)
        s2_word.append(wordList[0])
        wordList = wordList[1:]
    elif next == 26:
        output.write('acc')
        break
    else:
        s1_zt.append(int(next))
        s2_word.append(wordList[0])
        wordList = wordList[1:]
output.close()
with open("output.txt",'r') as f:
    resualt = f.readlines()
for r in resualt:
    print(r,end='')