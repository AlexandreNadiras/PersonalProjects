# Requirements:

pip install -r requirements.txt

If you are working with a 2.X version of python, you will have to install pysqlite.

pip install pysqlite

All this codes and the originale CSV Files must be in the same directory.


# UseCaseObjectives.py:


The only requirement for this code to run is that you have the origianl csv file in the same directory.
The code is very documented and pretty straight forward.


# BonusSQL.py:


This code only needs to be executed one and should return the result of 2 SQl Requests.

The first output is the result of the question: "What are the top 5 best wines below 10 USD?"

The second output is the result of the question: "What are the top 5 best wines below 30 USD from Chile 🗿"

The reason I used Sqlite3 is because I was familiar with it and also because the data I used were not that heavy and  resource consuming.

# BonusVisualisation.py:


This code only needs to be executed once and should return a visualisation of the curve representing the points given to each wine versus the price.

I chose to aggregate on the price's mean the clean dataset first in order to get a better visualisation than a scatter chart.

Given this data we can see a clear tendancy: the more expensive a wine is the better score it should get. 
It also appears that some wines between 200 and 300 are an exception to this. 

I don't think that it is pertinent to consider the wines that have a higher price than 1500. 
I think they are more likely to be outliers than variance in our data. 
What we can say however on those high price wines is that their supposed quality is not worth the price.
This can be explained but the nature of the score itself, each wines are tested by people that can get upset with a wine they paid a lot to taste and didn't fill their expectations. 
We also have to say that the dataset only gives us the wines that have a score above 80, and might not represent faithfully all the data.


# BonusMachineLearning.py:

In order to make a prediction, you need to run this code, it takes approximatively 4 secondes to execute, and then you can call the function make_pred() and give 2 arguments, the first one being the id of the country, and the second one being the price. 
Due to the nature of my algorithm, the answer is an integer. 
You can find here the corresponding number to each country here:

{'US': 1, 'France': 2, 'Italy': 3, 'Spain': 4, 'Portugal': 5, 'Chile': 6, 'Argentina': 7, 'Austria': 8, 'Australia': 9,
         'Germany': 10, 'New Zealand': 11, 'South Africa': 12, 'Israel': 13, 'Greece': 14, 'Canada': 15, 'Hungary': 16, 'Bulgaria': 17, 'Romania': 18, 'Uruguay': 19,
         'Turkey': 20, 'Slovenia': 21, 'Georgia': 22, 'England': 23, 'Croatia': 24, 'Mexico': 25, 'Moldova': 26, 'Brazil': 27, 'Lebanon': 28, 'Morocco': 29, 'Peru': 30,
         'Ukraine': 31, 'Serbia': 32, 'Macedonia': 33, 'Czech Republic': 34, 'Cyprus': 35, 'India': 36, 'Switzerland':37, 'Luxembourg': 38, 'Bosnia and Herzegovina': 39, 
         'Armenia': 40, 'Egypt': 41, 'Slovakia': 42, 'China': 43}

the methodology is used is the following:
	- test
	- rr
The methodology I used is the following:
	- 
	- Reading the original CSV into a pandas Dataframe
	- Cleaning the dataframe by droping all the NaN values and the features except price, points and country
	- Replacing each country name by an integer
	- Training and testing some predictors
	- Choosing the best one
	- Optimizing the predictor
	- Creating a function that allows the user to get a prediction by giving a country number and a price

The first thing to note here is that he have a categorical feature that does not take a numerical value.
This will be a problem when training our model so I will turn each country as a class and assign to each country a number.
One other problem that we have to deal with is the fact that our data are very unbalanced.
There are many ways to deal with this issue, either get more data, or manipulate our dataset by creating other artificial rows, also
given the time allowed to do this test, I might not ba able to handle this problem in the best way.
The problem I face for this test is a regression problem.
I will try different algorithms in order to solve this and make the best predictor possible:
    - RandomForest
    - Linear Regression


In this exercice, i got rid of a lot of code that were unnecessary for the execution but necessary for the training and optimisation of the model,
so I putted it in this Readme down bellow.

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

## Training each model and evaluating it on the training set:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

rf = RandomForestClassifier(n_estimators=51, random_state=42) 
rf.fit(X, y)
rf_score = cross_val_score(rf, X_train, y_train, cv=5, verbose=5)
print('Score on Validation Set : {}'.format(rf_score.mean()))


linear_reg = LinearRegression()
linear_reg.fit(X, y)
linear_score = cross_val_score(linear_reg, X_train, y_train, cv=5, verbose=5)
print('Score on Validation Set : {}'.format(linear_score.mean()))


## Evaluating the model's performance:

rf.fit(X_test, y_test)
rf = rf.predict(X_test)
rf_mse = mean_squared_error(y_test, rf)
rf_rmse = np.sqrt(rf_mse)
print(rf_rmse)

## Parameters optimisation:

param_to_opti = {
    'n_estimators' : [11, 51, 101],
    'criterion' : ['gini', 'entropy'],
    'max_depth' : [4, 8],
    'max_features' : ['auto', 'log2'],
}

rf_opti = RandomForestClassifier()
rf_opti_model = GridSearchCV(estimator=rf_opti, scoring='neg_mean_squared_error', param_grid=param_to_opti, cv=5)
rf_opti_model.fit(X_train, y_train)
print('Random Forest best hyperparameters : {}'.format(rf_opti_model.best_params_))

