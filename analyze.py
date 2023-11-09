import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

## SOLUTION

# to access only the data from the Purchase Amount column, we create a separate dataframe 
purchase_amt_df = df['Purchase Amount (USD)']
# to calculate summary statistics on the Purchase Amount column all in one call, we utilize the .describe() function
print('Summary statistics on Purchase Amount (USD)')
print(purchase_amt_df.describe())

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

## SOLUTION

# Repeated methods in Purchase Amount issue
age_df = df['Age']
print('Summary statistics on Age')
print(age_df.describe())

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?

## SOLUTION 

# For every group, we create a separate dataframe and run .desribe() function on them 

winter_df = df[df['Season']=='Winter']['Purchase Amount (USD)']
print("Winter summary statistics on Purchase Amount (USD)")
print(winter_df.describe())

summer_df = df[df['Season']=='Summer']['Purchase Amount (USD)']
print("Summer summary statistics on Purchase Amount (USD)")
print(summer_df.describe())

spring_df = df[df['Season']=='Spring']['Purchase Amount (USD)']
print("Spring summary statistics on Purchase Amount (USD)")
print(spring_df.describe())

fall_df = df[df['Season']=='Fall']['Purchase Amount (USD)']
print("Fall summary statistics on Purchase Amount (USD)")
print(fall_df.describe())

# keep all columns except for "Customer", & "Discount Applied"
# TODO: is there a more efficient way to exclude columns in your dataset?

## SOLUTION 

# utilize the .drop() function to drop the "Customer", & "Discount Applied" columns and axis = 1 to specify dropping of columns instead of rows

modified_df = df.drop(['Customer', 'Discount Applied'], axis = 1)
print(modified_df)

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)
payment_methods = df['Payment Method'].unique()
ny = df[df.Location == "New York"]

most_frequent_method = {}

for method in payment_methods:
    most_frequent_method[method] = len(ny[ny['Payment Method'] == method])

print(most_frequent_method)

# to showcase the most frequent payment method in each state we create a separate dataframe that only consults data from the 'Location' and 'Payment Method'
desired_columns_df = df[['Location', 'Payment Method']]
# within the dataframe we run multiple pandas functions starting with .groupby() which allows all the locations to be split based off of the state 
grouped_by_location = desired_columns_df.groupby('Location')
# with the groupby object, we run the .value_counts() function on the Payment Method column to return the values of every payment method used within each location
payment_method_counts = grouped_by_location['Payment Method'].value_counts()
# combining .groupby() function with the previous .value.count() function and adding the .idxmax() function which will return the most frequent payment method count for each state
most_frequent_payment_methods = payment_method_counts.groupby('Location').idxmax()
print(most_frequent_payment_methods)


# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
