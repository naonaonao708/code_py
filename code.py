people_num = int(input())
# For文によって指定した回数inputする
boll_num = [int(input()) for i in range(people_num)]
pass_num = int(input())

boll_pass = []
for i in range(pass_num):
    sublist = []
    sublist = list(map(int, input().split()))
    boll_pass.append(sublist)

