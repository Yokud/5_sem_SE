import matplotlib.pyplot as plt
x = [6, 8, 10, 12, 14, 16, 18]
y1 = [1.31, 3.79, 19.92, 106.72, 571.67, 3128.63, 17262.44]
y2 = [0.30, 0.41, 0.66, 0.82, 1.13, 1.50, 1.73]
y3 = [0.28, 0.38, 0.63, 0.81, 1.06, 1.30, 1.59]
y4 = [0.79, 4.34, 23.21, 122.97, 654.56, 3609.66, 20235.26]
y5 = [0.31, 0.47, 0.66, 1.02, 1.27, 1.76, 2.43]
# Построение графика
plt.xlabel("Суммарный размер строк")
plt.ylabel("Время выполнения (в микросекундах)")
plt.plot(x, y1, label = "Лев. Рек.")
plt.plot(x, y2, label = "Лев. Матр.")
plt.plot(x, y3, label = "Лев. 2 Стр.")
plt.plot(x, y4, label = "Дам.-Лев. Рек.")
plt.plot(x, y5, label = "Дам.-Лев. Матр.")
plt.axis([6, 18, 0, 25000])
plt.legend()
plt.show()
