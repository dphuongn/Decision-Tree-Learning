# Decision-Tree-Learning


## Data Set

We will use the following data set from the UC Irvine Machine Learning Repository:

* Congressional Voting Records Data Set at
(https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records).
Note that the dataset has missing values.

## What we do


1. Learn a Decision Tree classifiers on the data set (for example, using J48 in Weka). Visualize
the tree constructed by the decision tree algorithm. (Food for thought: Are there some
interesting rules that make sense based on what you understand about the data?)

2. Report the accuracy of the Decision Tree classifier using 5-fold cross-validation (Most of ML
packages including Weka have utility function for performing Cross-validation). Report 95%
confidence interval.

3. Report the accuracy of the Decision Tree classifier using 5-fold cross-validation (Most of ML packages including Weka have utility function for performing Cross-validation). Report 95% confidence interval.

    a. Randomly split the dataset into 5 data sets of (roughly) equal size D<sub>1</sub>, D<sub>2</sub>,..., D<sub>5</sub>.  

    b. For i = 1, 2,..., 5, each time use D<sub>i</sub> as test data and the rest as training data to learn a decision tree and measure its accuracy p<sub>i</sub>.

    c. Visualize the five trees constructed. Do the five trees differ with each other and with the tree constructed using all the data (in part 1)? How much do their accuracies differ?


# Specification

Language used: 

* Python 3.8

Additional packages used: 

* numpy 1.18.2

* pandas 1.0.3

# How to run in command line

* Download **house-vote-84.data** file into the working folder.

* Navigate Mac terminal (or Window prompt) to the directory and run lab3.py to get csv files to use with Weka.:
```
$ python lab3.py
```

* Part 1 and 2: Use **house-vote-84.csv** as input (training set) and use 5-fold cross validation.

* Part 3: 
    - i = 1: use training_1.csv as training set and testing_1.csv as testing set.
	- i = 2: use training_2.csv as training set and testing_2.csv as testing set.
	- i = 3: use training_3.csv as training set and testing_3.csv as testing set.
	- i = 4: use training_4.csv as training set and testing_4.csv as testing set.
	- i = 5: use training_5.csv as training set and testing_5.csv as testing set.