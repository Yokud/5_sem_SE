import matplotlib.pyplot as plt
x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [0.024, 0.170, 0.527, 1.476, 3.162, 5.463, 9.451, 14.027, 18.884, 26.829]
y2 = [0.014, 0.106, 0.386, 0.961, 2.055, 4.036, 6.788, 9.366, 14.120, 18.049]
y3 = [0.009, 0.075, 0.290, 0.642, 1.296, 2.314, 4.836, 5.860, 11.594, 13.348]
# Построение графика
plt.xlabel("Порядок матриц")
plt.ylabel("Время выполнения (в секундах)")
plt.plot(x, y1, label = "Стандартный")
plt.plot(x, y2, label = "Виноград")
plt.plot(x, y3, label = "Оптимизированный Виноград")
plt.legend()
plt.xticks(x)
plt.show()

