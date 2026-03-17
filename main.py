import pandas as pd

# зчитування даних
data = pd.read_csv("data.csv")

# стовпець з класом називається 'class'
class_0 = data[data['class'] == 0]
class_1 = data[data['class'] == 1]

print("Клас 0:")
print(class_0.head())

print("Клас 1:")
print(class_1.head())
