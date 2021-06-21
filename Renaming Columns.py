import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

print(df)


#OR//

df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
