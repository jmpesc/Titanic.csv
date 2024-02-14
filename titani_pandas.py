import pandas as pd

# Задание 1
df = pd.read_csv("titanic.csv")

# Задание 2
selected_columns = ['Name', 'Age', 'Sex']
num_rows = 10
df_selected = pd.read_csv("titanic.csv", usecols=selected_columns, nrows=num_rows)

# Задание 3
print("DataFrame information:")
print(df.info())

# Задание 4
df.loc[df['Age'] < 18, 'Age'] = 'Child'

# Задание 5
df.rename(columns={'Sex': 'Gender'}, inplace=True)

# Задание 6
has_missing_values = df.isnull().values.any()

# Задание 7
columns_with_missing_values = df.columns[df.isnull().any()].tolist()
total_missing_values = df.isnull().sum().sum()

# Задание 8
df_missing_age = df[df['Age'].isnull()]

# Задание 9
df_filtered = df[(df['Age'] > 30) & (df['Sex'] == 'male')]

# Задание 10
df_age_range = df[(df['Age'] >= 30) & (df['Age'] <= 40)]

# Задание 11
df_every_20th_row = df.iloc[::20][['Age', 'Name', 'Survived']]

# Задание 12
import matplotlib.pyplot as plt

survived_by_gender = df.groupby(['Survived', 'Sex']).size().unstack()
survived_by_gender.plot(kind='bar', stacked=True)
plt.title('Survival of Titanic passengers by gender')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks([0, 1], ['No', 'Yes'], rotation=0)
plt.show()
