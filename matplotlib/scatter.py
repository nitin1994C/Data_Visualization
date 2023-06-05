import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 6, 1]

plt.scatter(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.scatter(x, y, marker='o', s=50, c='red', alpha=0.8)
plt.colorbar()


plt.show()
