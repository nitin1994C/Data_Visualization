import matplotlib.pyplot as plt

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [25, 40, 30, 35]

plt.pie(values, labels=categories)

colors = ['red', 'blue', 'green', 'orange']
explode = [0.1, 0, 0, 0]
plt.pie(values, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%')

plt.title('Pie Chart')

plt.legend()

plt.show()
