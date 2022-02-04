people_num = int(input())
# For文によって指定した回数inputする
boll_num = [int(input()) for i in range(people_num)]
pass_num = int(input())

boll_pass = []
for i in range(pass_num):
    sublist = []
    sublist = list(map(int, input().split()))
    boll_pass.append(sublist)


# ネストしたforループからbreak
a,b = input().split()
a_num = int(a) * 100
b_num = int(b)

for i in range(1,10):
    a_number = i *10
    for j in range(1,10):
        i_number = j
        dt_1 = (a_number + i_number) * i_number
        dt_2 = a_num + b_num + a_number
        if dt_1 == dt_2:
            print(i,j)
            break
        elif i == 9 & j == 9:
            print("No")
        else:
            pass
    else:
        continue
    break


# スペースのある入力値をint形式でinputする
H,W,K = map(int, input().split())
dt = [input() for i in range(H)]


# if内の条件の複数指定
N, X, Y = map(int, input().split())
for i in range(1,N+1):
    if i%X==0 and i%Y==0:
        print("AB")
    elif i%X==0:
        print("A")
    elif i%Y==0:
        print("B")
    else:
        print("N")


# 特定の文字列をカウントする
input_line = input().split('+')
dt = 0
for i in range(len(input_line)):
    dt += input_line[i].count('<')*10 + input_line[i].count('/')
    
print(dt)

