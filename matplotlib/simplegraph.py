import matplotlib.pyplot as plt


categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [25, 40, 30, 35]

plt.bar(categories, values)


plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')


plt.show()
