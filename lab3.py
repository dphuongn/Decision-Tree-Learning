import pandas as pd
import numpy as np

# Make attributes for the data set
df = pd.read_csv("house-votes-84.data",
                  names=["Class", "handicapped-infants", "water-project-cost-sharing",
                         "adoption-of-the-budget-resolution", "physician-fee-freeze",
                         "el-salvador-aid", "religious-groups-in-schools", 'anti-satellite-test-ban',
                         "aid-to-nicaraguan-contras", "mx-missile", "immigration",
                         "synfuels-corporation-cutback", "education-spending", "superfund-right-to-use",
                         "crime", "duty-free-exports", "export-administration-act-south-africa"])

# convert to csv file
df.to_csv('house-votes-84.csv', index=False)

# random split the data set into 5 data sets of equal size: df1 -> df5
# random_state for reproduction purpose
shuffled = df.sample(frac=1, random_state=1)
result = np.array_split(shuffled, 5)

df1 = result[0]
df2 = result[1]
df3 = result[2]
df4 = result[3]
df5 = result[4]


# convert smaller data sets to csv files
i = 1
for part in result:
    part.to_csv('testing-%s.csv' % i, index=False)
    i += 1

# for df1 being test set, the rest is training set
training_set_1 = pd.concat([df2, df3, df4, df5])
training_set_1.to_csv('training-1.csv', index=False)

# for df2 being test set, the rest is training set
training_set_2 = pd.concat([df1, df3, df4, df5])
training_set_2.to_csv('training-2.csv', index=False)

# for df3 being test set, the rest is training set
training_set_3 = pd.concat([df1, df2, df4, df5])
training_set_3.to_csv('training-3.csv', index=False)

# for df4 being test set, the rest is training set
training_set_4 = pd.concat([df1, df2, df3, df5])
training_set_4.to_csv('training-4.csv', index=False)

# for df5 being test set, the rest is training set
training_set_5 = pd.concat([df1, df2, df3, df4])
training_set_5.to_csv('training-5.csv', index=False)

