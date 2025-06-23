#Lesson 18 homework 

# Task 
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\Python lessons\\tackoverflow_qa.csv')
df.head()
#1 Find all questions created before 2014

# Convertion creationdate to datetime
df['creationdate'] = pd.to_datetime(df['creationdate'])

# Filter rows where creationdate is before 2014
before_2014 = df[df['creationdate'] < '2014-01-01']
print(before_2014)
#2 Find all questions with a score more than 50

score_above_50 = df[df['score'] > 50]
print(score_above_50)
#3 Find all questions with a score between 50 and 100

score_50_to_100 = df[(df['score']>= 50) & (df['score'] <= 100)]
print(score_50_to_100)

#4 Find all questions answered by Scott Boston

answered_by_scott = df[df['ans_name']== 'Scott Boston']
print(answered_by_scott)

#5 Find all questions answered by the following 5 users

users = ['Scott Boston', 'unutbu', 'Mike Pennington', 'jezrael', 'Warren Weckesser']
answered_by_users = df[df['ans_name'].isin(users)]
print(answered_by_users)

#6.Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

filtered = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu')& 
    (df['score'] < 5)
    ]
print(filtered)

#7.Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

score_of_view = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]
print(score_of_view)

#8.Find all questions that are not answered by Scott Boston

not_scott = df[df['ans_name'] != 'Scott Boston']
print(not_scott)

# Task :Titanic data set, stored as CSV. 

import pandas as pd

# Loaning the dataset

titanic_df = pd.read_csv("C:\\Users\\User\\Desktop\\Python lessons\\titanic.csv")

# Preview the first 5 rows

print(titanic_df.head())

# 1.Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

female_class1_age20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) & (titanic_df['Age'] <= 30)
]

print(female_class1_age20_30)

#2.Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

fare_over_100 = titanic_df[titanic_df['Fare'] > 100]

print(fare_over_100)

#3.Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print(survived_alone)

#4.Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

embarked_c_fare_over_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

print(embarked_c_fare_over_50)

#5.Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

family_both_sides = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0) 
]

print(family_both_sides)

#6. Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

young_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

print(young_not_survived)

#7. Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

cabin_and_fare_over_200 = titanic_df[
    titanic_df['Cabin'].notnull() &
    (titanic_df['Fare'] > 200)
]
print(cabin_and_fare_over_200)

#8.Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]

print(odd_passenger_ids)

#9.Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

# Keeping tickets that appear only once

unique_tickets = titanic_df[
    titanic_df['Ticket'].duplicated(keep=False) == False
]

print(unique_tickets)

#10. Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

miss_in_class1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Name'].str.contains('Miss'))
]

print(miss_in_class1)

