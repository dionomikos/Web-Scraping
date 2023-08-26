import pandas as pd

# Lists are necessary for data scraping because we store all our data there
# Sometimes we need to put related lists into a dictionary with key - value pairs
states = ["California", "Texas", "Florida", "New York"]
population = [39051000, 29000000, 21480000, 8804000]

dict_states = {
    'States': states,
    'Population': population
}

# print(states[0])
# print(states[3])

# If the state is Florida then print it. Then otherwise DON'T
# for state in states:
#     if state == "Florida":
#         print(state)

# Export data in Python


# First way
# open() takes a file name and a method
# Using the with open method we have the advantage that we close also the file automatically
# with open('test.txt', 'w') as file:
#     file.write("Data successfully scraped!!!!")


# Second way
# For the second way we have to install the pandas library
# To create a data frame with pandas i write:
# We can also save this data frame to a csv file!!!! After extracting it!!!
df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)

# In case i don't want the index details to be showed into my csv file i set index to false (False)
df_states.to_csv('states.csv', index=False)