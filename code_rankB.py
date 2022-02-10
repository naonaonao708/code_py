# Bランクのコード


# データクレンジング
# 実行で一つエラーを吐いた おそらくfloatからintに変更する際の数値のずれだと思われる

import pandas as pd
import numpy as np
N, M = map(int,input().split())
data = []

for i in range(N):
    sublist = []
    sublist = list(input().split())
    data.append(sublist)

df = pd.DataFrame(data)
# 数値に変換できない値をNanにする 
# 「pandas.DataFrame で数値以外の要素の抽出」　　https://qiita.com/kusmoto/items/058abc5b97ebfe77cf01 
pic = df.apply(lambda s:pd.to_numeric(s, errors='coerce')).isnull()
df = df[~pic].astype(float)
pic_2 = df.apply(lambda x: x < 0) | df.apply(lambda x: x > 100)
df = df[~pic_2].astype(float)

for i in range(M):
    try:
        # このタイミングでintに変えたのがまずそう　　平均取る前にintにしたい→Nanはfloatのままじゃないと計算できない
        print(int(df.iloc[:, i].mean()))
    except ValueError:
        print(0)



# カブトムシ問題 Error 原因は不明

N = int(input())
red, gleen ,blue = map(int, input().split())
R_col = ['R','Y','M','W']
G_col = ['G','Y','C','W']
B_col = ['B','M','C','W']

n=0
for i in range(N):
    if red == gleen and gleen == blue:
        print(red)
        break
    else:
        direction,color = input().split()
        if direction == 'L':
            if color in R_col:
                red -= 1
            if color in G_col:
                gleen -= 1
            if color in B_col:
                blue -= 1
        elif direction == 'R':
            if color in R_col:
                red += 1
            if color in G_col:
                gleen += 1
            if color in B_col:
                blue += 1
    if i == N-1:
        print("no")


# カラオケ大会 最後に一つエラー吐いた
# 解決→ifの最初のイージーミス

N, M = map(int,input().split())
sample_data = [int(input()) for j in range(M)]
test_data = []
for i in range(N):
    sublist = []
    sublist = [int(input()) for j in range(M)]
    test_data.append(sublist)
 
def scoring(x):
    x = abs(x)
    if x < 5:
        return 0
    elif x <= 10:
        return 1
    elif 10 < x <= 20:
        return 2
    elif 20 < x <= 30:
        return 3
    else:
        return 5

score_list = []
for i in range(N):
    score = 100
    count = 0
    for j in range(M):
        if count < M-1:
            dt = sample_data[j] - test_data[i][j]
            score -= scoring(dt)
            count += 1
        else:
            dt = sample_data[j] - test_data[i][j]
            score -= scoring(dt)
            if score > 0:
                score_list.append(score)
            elif score < 0:
                score = 0
                score_list.append(score)
            
print(max(score_list))


# チョコの分割

H, W = map(int,input().split())

return_list = []
for i in range(H):
    raw_data = input().split()
    # リストの型をint型へ変換　内包表記で行う
    raw_data = [int(i) for i in raw_data]
    for j in range(W):
        # リスト内で和が等しくなる場合の抽出
        if sum(raw_data[0:j+1]) == sum(raw_data[j+1:W]):
            return_list.append("A"*(j+1) + "B"*(W-j-1))
        else:
            pass

if len(return_list) == H:
    print("Yes")
    for i in range(H):
        print(return_list[i])
else:
    print("No")



# 台風の接近

import collections

N,M = map(int,input().split())
rain_data = []
for i in range(N):
    raw_data = input().split()
    raw_data = [int(i) for i in raw_data]
    rain_data.append(raw_data)

root = []
for i in range(N):
    for j in range(N):
        if rain_data[i][j] < M:
            root.append(j+1)
        else:
            pass


# collections.Counterによってリスト内の要素の個数を辞書型化
c = collections.Counter(root)
# 辞書型をリスト内包表記とitemsメソッドによって指定した値と等しいキーを出力
keys = [k for k, v in c.items() if v == N]

if len(keys) > 0:
    # リストの要素をスペース区切りで出力する
    print(*keys)
else:
    print("wait")