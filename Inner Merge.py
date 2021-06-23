#mege two csv file::
import pandas as pd

X1 = pd.read_csv('X1.csv')
X2 = pd.read_csv('X2.csv')
X3 = pd.read_csv('X3.csv')

T1 = pd.merge(X1, X2)  // megre two csv file 

T1 = X1.merge(X2) /
       .merge(X3)
  
# Make condition to the table::

T2 = T1[T1.column_name < T1.column_name1]

#make condition for more than one table 

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

# if we want to merge two table having the same name of id columns : 
#use rename to merge two DataFrames whose columns don’t match.
orders_products = pd.merge(orders, products.rename(
  columns = {'id': 'product_id'}
))

#use the keywords left_on and right_on to specify which columns we want to perform the merge on
orders_products = pd.merge(
	orders,
	products,
	left_on = 'product_id',
	right_on = 'id',
	suffixes = ['_orders', '_products']
)

