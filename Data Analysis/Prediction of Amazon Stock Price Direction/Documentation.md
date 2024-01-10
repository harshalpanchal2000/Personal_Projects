# Amazon Stock Price Prediction Project
## Problem Statement
The objective of this project is to forecast the directional movement (up or down) of Amazon.com, Inc. (AMZN) stock prices. Rather than predicting the exact price, the focus is on binary classification, determining whether the closing price on the next day will be higher than the opening price. This approach aims to guide decisions on buying or selling stocks based on price movement direction.

The dataset spans from 1997 to 2020, divided into training (1997-2016), validation (2016-2018), and testing (2018-2020) periods. The data is distributed across AMZN_train.csv, AMZN_val.csv, and AMZN_test.csv files for the respective timeframes.

## Technologies Used
- Python: The entire project is implemented using Python, leveraging its rich ecosystem of data science libraries and tools.

- Pandas: Used for data manipulation, loading datasets, and initial exploration.

- Matplotlib: Employed for data visualization, including plotting stock prices over time.

- Scikit-Learn: Utilized for implementing machine learning algorithms, hyperparameter tuning, and model evaluation.

- TensorFlow: Employed for building and training the deep learning model.

- Grid Search: Used for hyperparameter tuning of the Logistic Regression model.

## Data Exploration
In the initial exploration, Python libraries such as Pandas and Matplotlib were used to load the datasets and analyze data attributes. Visualization techniques were employed to detect trends and explore the possibility of feature engineering. The analysis involved plotting stock prices over time and ensuring that the datasets followed a similar distribution.

## Feature Engineering
Feature engineering was conducted to enhance predictive capabilities. Moving averages for 3 and 7 days, today's direction, and price range were calculated and added as features to capture trends and magnitudes of price changes.

## Machine Learning Models
Different machine learning algorithms commonly used for time series and stock price prediction were implemented, including Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting Ensemble. A function named test_model was defined to train, fit, and evaluate the datasets for these models.

## Deep Learning Model
A deep learning model using TensorFlow was trained to predict stock price movement. The model architecture included normalization, dense layers with ReLU activation, dropout, and a sigmoid output layer. Learning rate scheduling and early stopping callbacks were implemented to prevent overfitting.

## Conclusion
The Gradient Boosting Classifier and Logistic Regression performed best on the validation set, achieving an accuracy of 52.09%. The deep learning model did not outperform the baseline models. Evaluation on the test set confirmed the Gradient Boosting Classifier's performance.

## Hyperparameter Tuning
Hyperparameter tuning was performed for the Logistic Regression model using Grid Search. The best hyperparameters were obtained, but the accuracy did not significantly improve. Due to time constraints, the tuned model was not used.

## Overfitting
To identify overfitting, the model was evaluated on both the training and test sets, and learning curves were plotted. A significant gap between the curves indicated potential overfitting.

## Regularization
Regularization was applied to the Logistic Regression model to address overfitting, but the accuracy remained similar.

## Important Features for the model: 
Feature importance was visualized using a bar plot. The features contributing most to the predictive performance were identified which are displayed below :
<br/>
<br/>
![Important Features](https://github.com/harshalpanchal2000/Personal_Projects/blob/main/Data%20Analysis/Prediction%20of%20Amazon%20Stock%20Price%20Direction/Important%20Features.png)

