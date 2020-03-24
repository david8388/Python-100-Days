import pandas as pd
import random

url = 'https://dts.twse.com.tw/opendata/t187ap03_L.csv'

df = pd.read_csv(url)

all = df['公司簡稱']


def intersection(list1, list2):
    return set(list1) & set(list2)

strage1 = random.choices(all, k=100)

strage2 = random.choices(all, k=50)

print(intersection(strage1, strage2))
