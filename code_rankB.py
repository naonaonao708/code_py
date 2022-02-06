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
