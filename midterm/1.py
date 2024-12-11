import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
base_suction_kPa = np.logspace(-2, 3, num=50)  # 基质吸力，从0.01到1000 kPa
seepage_rate_mday = 1e-01 * np.exp(-base_suction_kPa)  # 渗透率，模拟数据

# 创建图表
plt.figure(figsize=(6, 6))

# 绘制数据点
plt.plot(base_suction_kPa, seepage_rate_mday, 'k.', markersize=5)

# 设置对数刻度
plt.xscale('log')
plt.yscale('log')

# 添加标签和标题
plt.xlabel('Base Suction / kPa')
plt.ylabel('Seepage Rate / (m/day)')
plt.title('Seepage Rate vs Base Suction')

# 显示网格
plt.grid(True, which="both", ls="--")

# 显示图表
plt.show()