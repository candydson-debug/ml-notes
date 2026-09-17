"""生成多因子房价预测数据集 house_price.csv

特征：
    area       房屋面积 (平方米)
    bedrooms   卧室数量 (间)
    bathrooms  卫生间数量 (间)
    age        房龄 (年)
    distance   距市中心距离 (公里)
    school     学区评分 (1~10)
目标：
    price      房价 (万元)

真实生成关系（含噪声，供与模型估计系数对比）：
    price = 50 + 0.8*area + 15*bedrooms + 20*bathrooms
            - 1.2*age - 3*distance + 10*school + N(0, 25)
"""
import csv
import random

random.seed(2026)  # 固定种子，结果可复现

N = 500
rows = []
for _ in range(N):
    area = round(random.uniform(50, 250), 1)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    age = round(random.uniform(0, 30), 1)
    distance = round(random.uniform(1, 25), 1)
    school = random.randint(1, 10)
    noise = random.gauss(0, 25)
    price = round(50 + 0.8 * area + 15 * bedrooms + 20 * bathrooms
                  - 1.2 * age - 3 * distance + 10 * school + noise, 2)
    rows.append([area, bedrooms, bathrooms, age, distance, school, price])

header = ["area", "bedrooms", "bathrooms", "age", "distance", "school", "price"]
with open("house_price.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"已生成 {N} 行数据 -> house_price.csv")
print("真实系数: 截距=50, area=0.8, bedrooms=15, bathrooms=20, age=-1.2, distance=-3, school=10, 噪声σ=25")
