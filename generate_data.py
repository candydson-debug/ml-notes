"""生成简单线性回归数据 generated_data.csv（只有 x, y 两列）

真实关系（供与模型估计对比）：
    y = 5 + 3*x + noise
    噪声 noise ~ N(0, 20)
"""
import csv
import random

random.seed(42)  # 固定种子，结果可复现

N = 200
rows = []
for _ in range(N):
    x = round(random.uniform(0, 100), 2)
    noise = random.gauss(0, 20)
    y = round(5 + 3 * x + noise, 2)
    rows.append([x, y])

with open("generated_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    writer.writerows(rows)

print(f"已生成 {N} 行数据 -> generated_data.csv")
print("真实关系: y = 5 + 3*x + N(0, 20)")
