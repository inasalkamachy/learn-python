#Our finance department wants to know the price of the most expensive pair of shoes purchased. Save your answer to the variable most_expensive.

#Our fashion department wants to know how many different colors of shoes we are selling. Save your answer to the variable num_colors.


import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))
most_expensive = orders.price.max()
print(most_expensive)
num_colors = orders.shoe_color.nunique()
print(num_colors)


#Let’s return to our orders data from ShoeFly.com.

#In the previous exercise, our finance department wanted to know the most expensive shoe that we sold.

#Now, they want to know the most expensive shoe for each shoe_type (i.e., the most expensive boot, the most expensive ballet flat, etc.).

#Save your answer to the variable pricey_shoes.


import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head())

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))


#Modify your code from the previous exercise so that it ends with reset_index, which will change pricey_shoes into a DataFrame.

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))


#Once more, we’ll return to the data from ShoeFly.com. Our Marketing team says that it’s important to have some affordably priced shoes available for every color of shoe that we sell.

#Let’s calculate the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale. Save the data to the variable cheap_shoes.

#Note: Be sure to use reset_index() at the end of your query so that cheap_shoes is a DataFrame.

import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

print(cheap_shoes)


# At ShoeFly.com, our Purchasing team thinks that certain shoe_type/shoe_color combinations are particularly popular this year (for example, blue ballet flats are all the rage in Paris).

#Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.

#You should be able to do this using groupby and count().

#Note: When we’re using count(), it doesn’t really matter which column we perform the calculation on. You should use id in this example, but we would get the same answer if we used shoe_type or last_name.

import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

print(shoe_counts)
#Remember to use reset_index() at the end of your code!



import codecademylib
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())

click_source = user_visits.groupby('utm_source').id.count().reset_index()

print(click_source)

click_source_by_month = user_visits.groupby(['utm_source','month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(
  columns = 'month',
  index = 'utm_source',
  values = 'id').reset_index()
print(click_source_by_month_pivot)
