import matplotlib.pyplot as plt

subjects=['Computer', 'English', 'Physics', 'Chemistry', 'Biology', 'Maths', 'History']

student1_mark=[88, 70,60,65,99,88,77]

student2_mark=[72,80,80, 70, 85, 70, 80]

student3_mark=[55,77,65, 80, 70, 75, 90]


plt.plot(subjects, student1_mark, label='Student1 Mark')
plt.plot(subjects, student2_mark, label='Student2 Marks')
plt.plot(subjects, student3_mark, label='Student3 Marks')

plt.xlabel('Subjects')
plt.ylabel('Marks')

plt.title('Marks Comparison')
plt.legend()
plt.show()