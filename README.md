The frontend for this project is [here](https://github.com/Ashutosh652/crop_predict_frontend/edit/main/README.md).

Note: This report is converted from pdf to githuub markdown format using [this](https://github.com/jzillmann/pdf-to-markdown). Some editing and the addition of pictures were done later. There may be some errors in this markdown.


Project Report on
**Crop Yield Prediction Using Machine Learning**


**Abstract**

This is a report on the ‘Crop Yield Prediction’ project. This is a project to create a
web application that utilizes machine learning techniques to predict crop
production of paddy, wheat, maize, millet, and barley in Nepal. The application
predicts the production of these crops based on various environmental and
weather data using a machine learning model. The machine learning model is then
integrated into a web interface, allowing users to input their own data and receive
predictions for crop productions. The system will leverage the power of machine
learning to improve crop production predictions and support better decision-
making for farmers and agricultural stakeholders in Nepal.

**Keywords:** machine learning, crops, crop yield, crop production, prediction,
Nepal, web application.



# Introduction

Agriculture is a vital sector in Nepal and plays a significant role in the country's
economy. However, crop productions in Nepal are affected by various factors
such as weather patterns, temperature, precipitation, rainfall, atmospheric pressure
and various other factors. Accurate prediction of crop production is crucial for
farmers and agricultural stakeholders to make informed decisions and improve
crop productivity.

Machine learning has shown promising results in various applications, including
crop yield prediction. The ability of machine learning models to process large
amounts of data and identify complex patterns can provide more accurate
predictions than traditional methods. This project creates a web application that
utilizes machine learning techniques to predict crop production of popular crops
like paddy, wheat, maize, millet and barley in Nepal.

The machine learning model is trained from historical crop production data and
different environmental data. The model is then integrated into a web interface,
allowing users to input their own data and receive predictions for crop
productions. The web application is simple and user-friendly and it will be easily
accessible to farmers and other stakeholders in Nepal.

The system aims to leverage the power of machine learning to improve crop
production predictions and support better decision-making for farmers and
agricultural stakeholders in Nepal. With this project, we hope to contribute to the
sustainable development of the agricultural sector in Nepal and improve the
livelihoods of farmers and their families.

# Problem Statement

The agricultural sector in Nepal plays a significant role in the country's economy,
but crop production is affected by various factors such as weather patterns, soil
quality, and pest infestations. Accurate prediction of crop production is crucial for
farmers and agricultural stakeholders to make informed decisions and improve
crop productivity. Typically, the estimation of crop production took a more
traditional approach in Nepal combining sample crop cutting data with field
surveys, and field verification reports from the District Agricultural Development
Offices (DADOs). Based on the information gathered through these processes,
and additional field verifications and consultations, the Ministry of Agricultural
Development (MoAD), World Food Program (WFP) and the Food and
Agriculture Organization of the United Nations (FAO) releases crop situation
updates twice a year, after the summer and winter harvests. While a new method
known as CCAFS Regional Agriculture Forecasting Toolbox (CRAFT) is being
used now, it is still time consuming and cumbersome compared to Machine
Learning models which can predict crop yields in advance with high accuracy.
Many factors influence the production of a crop which can make it difficult to
predict its production long time beforehand which in turn makes it difficult to
prepare for the future and make plans on both farmer level and national level.

# Aim

The aim of this project is to develop a web application that utilizes machine
learning techniques to predict crop production of different crops like paddy,
maize, wheat, millet and barley in Nepal. The system predicts crop production
based on historical crop yield data, as well as relevant environmental and weather
data.

# Objectives

The objectives of this project can be summarized onto the following points.

```
To train a machine learning model using the collected data to predict crop
production.
```
```
To compare the results of different machine learning algorithms and
choose the one with highest accuracy.
```
```
To develop a web application using web frameworks, such as Django and
ReactJS, that allows farmers and other agricultural stakeholders to input
their own data and receive predictions for crop productions.
```
```
To help the farmers and government to plan ahead based on the predicted
crop production data.
```
```
To study the effects of various metrics such as temperature, precipitation in the
production of crops.
```

# Motivation

The motivation for this project is to improve crop production predictions in Nepal,
which can have a significant impact on the agricultural sector and the livelihoods
of farmers. Accurate crop production predictions can help farmers make informed
decisions about planting and harvesting crops, leading to increased productivity
and more sustainable agricultural practices. Additionally, the project can also
support decision-making for other agricultural stakeholders, such as government
agencies and agribusinesses, to better plan and allocate resources for the sector's
development.

Additionally, creating a web application for crop yield prediction makes the
system more accessible to farmers and other agricultural stakeholders in Nepal,
which could potentially increase its impact and adoption.

# Application

The system for predicting crop production in Nepal using machine learning could
be applicable to a wide range of stakeholders in the agricultural sector, including:

```
i. Farmers: The system could provide valuable information for farmers to
make more informed decisions about planting and harvesting crops,
leading to increased productivity and more sustainable agricultural
practices.
```

```
ii. Government agencies: The system could provide valuable information
for government agencies to plan and allocate resources for the
development of the agricultural sector in Nepal.
```
```
iii. Agribusinesses: The system could provide valuable information for
agribusinesses to plan and allocate resources for the development of
the agricultural sector in Nepal.
```
```
iv. Crop insurance companies: The system could be used to provide crop
insurance companies with better predictions of crop yields, which can
help to improve the design of insurance products and reduce the risk of
financial losses.
```
```
v. Agricultural researchers: The system could be used to support
agricultural research by providing more accurate and up-to-date
information on crop yields.
```
```
vi. Food security stakeholders: The system can be used to improve food
security in Nepal by providing accurate predictions of crop yields to
ensure that there is sufficient food for the population.
```
```
vii. Non-governmental organizations: The system can be used by non-
governmental organizations to support sustainable development and
poverty reduction in rural areas.
```
```
viii. International organizations: The system can be used by international
organizations to support sustainable development and poverty
reduction in Nepal.
```
```
ix. Policymakers: The system can be used by policymakers to make more
informed decisions about the agricultural sector in Nepal.
```


# System Design
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/e33b853b-3990-43b1-8009-52b6f35931cb)


## System Diagram

This is a basic architecture of the system which gives only the general view of
how the system works. The user can interact with the webapp and see the
historical data of crop production as well as view the prediction of the crop
productions. The user can also choose a crop and his/her district and area for
planting crop and view the historical as well as predicted production of the
selected crop. The user can also view various graphs in which the change in
production of a selected crop can be viewed against a selected feature. The
webapp interacts with the server which contains the machine learning model used
to predict the crop yield. The admin manages the webapp and the server.

When the user enters the required input and clicks the submit button, the inputs
are sent to the server that hosts the trained model. The model then makes a
prediction of crop production based on those inputs and the server sends the result
back to the frontend where the user can view the result.


## Modules

### User Module

This module is used by the user to enter the inputs in the web-app to make
prediction, view the predicted output, and view historical climate and crop
production data and view graphs of features against crop productions.

### Prediction Module

The regression task is implemented in this module. The best model among all the
trained models is selected for this process. This module makes predictions based
on the inputs given by the user.

## Use Case Diagram

![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/fb800e68-8332-4223-b697-26f7e90db22a)

The above diagram has two primary actors i.e. User and Admin. User can view
historical and predicted data on crop production, filter historical data based on
district, crop and year, and view graphs of features against production values
predicted by the model. The admin manages the web-app and the server where the
trained model resides.

## Flow Diagram

![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/e13ca930-45de-4bec-8885-8009095c7c6a)

A flow diagram is a type of diagram that represents an algorithm, workflow or
process, showing the steps as boxes of various kinds, and their order by
connecting them with arrows.

When someone uses our system through the web-app, he/she will first land on the
home page of the web-app. There, the user is required to enter various inputs such
as district name, crop name, year, temperature range, area, precipitation, specific
humidity, surface pressure and relative humidity required to make a prediction by
our model. When the user enters the inputs, it is then sent to the backend server
that hosts the trained model which sends its prediction back to the frontend. The
prediction is then shown to the user. The user can also navigate to the page where
he/she can view historical climate and crop production data. The user can also
filter the historical data based on district, crop and year. There is another page that
the user can navigate to where the user can view various graphs. The user has to
first select which graph he/she wants to see. The graphs that can be selected
include the graph of every input feature except district and year against the
production value predicted by our model. For example, if the user selects the
option to see the graph of precipitation vs production, then he/she has to enter
every input except precipitation and click on the submit button. Then a number of
requests are made to the backend server with multiple precipitation values but
keeping all the other inputs the same. Then a number of predictions of production
is sent back to the frontend and the graph of change in production with respect to
change in precipitation is shown to the user. The user can select to see the graph
of any feature against the predictions made by the model.


# Implementation and Discussion

![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/f8063cbc-5c37-4a8e-a1b6-7a10bb77418c)

## Data Collection

We collected various crop and climate data of Nepal from different sources.

### Crop Data

The district wise data on crop production of paddy, wheat, maize, millet and
barley from fiscal year 1979/80 to 2013/14 was obtained from the website of
International Center for Integrated Mountain Development (ICIMOD). [7] The
dataset includes the production (in mt), area (in ha) and yield (in kg/ha) of the
mentioned crops for each district for each year. This data was collected by
ICIMOD from Ministry of Agricultural Development, Nepal for the purpose of
developing the online agricultural atlas of Nepal. This data is publicly available.
This is what the initial data looks like.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/ddccdaa0-bc04-4190-8243-2f8554bfa130)

### Initial Climate Data

The daily district wise climate data of Nepal was obtained from Open Data Nepal.
[8] This dataset includes the daily data from 1981 to 2019 on precipitation, surface
pressure, specific humidity, relative humidity, temperature and wind speed. This
dataset was obtained from NASA Langley Research Center (LaRC) POWER
Project funded through the NASA Earth Science/Applied Science Program and
extracted using NASA's power access API. This dataset only contains the data of
62 districts of Nepal. So, we extracted the data of the remaining 13 districts using
NASA’s power access API. This is what the initial data looks like.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/12e2da38-f45e-42bb-9d14-587fefba28f5)

### Problems Faced.........................................................................

The reason for collecting daily climate data instead of yearly data directly is
because the crop data is in fiscal year. A fiscal year in Nepal starts from July 16
and ends on July 15 of the next year. But the yearly data that can be found is in
normal year averages and accumulations depending on the parameter. We also
couldn’t collect monthly climate data because in order to convert that monthly
data into fiscal yearly data, we would need to make the distinction of the data of
the month of July before and after its 15th day which is not possible. The only way
we could accomplish that was by collecting daily climate data and convert it into
fiscal yearly data. Also many of the crop data is nonsensical. For example, one
row says that wheat was planted in an area of 24000ha and the production is only
4.32mt making the yield 0.18kg/ha which is 0.18kg of wheat per 10000 square
meter of land. These might be mistakes made by MoAD, Nepal or due to some
natural disaster or actual data with no mistakes. We have no way to find out.
There are many instances of these types of cases.


## Analysis and Pre-processing of Data...............................................................

### Modifying Climate Dataset.....................................................................

First, the initial climate data was changed into suitable form to make it suitable for
merging with the crop data. The steps performed during this are mentioned below.

```
i) Some of the names of districts in the crop data and climate data were
inconsistent. So, the names of those districts in the climate dataset
were changed to make them consistent with the names of the districts
in the crop dataset.
```
```
ii) Then, the initial climate dataset obtained from Open Data Nepal[8] had
the data of only 62 districts and the data of the remaining 13 districts of
Nepal was extracted from NASA’s Power Access api. Then the data of
the 13 districts were also added to the climate dataset.
```
```
iii) Then, the climate dataset was checked for any null values and no null
values were found.
```
```
iv) Then the daily climate data was converted into fiscal yearly data
because the crop data is in fiscal year. A fiscal year in Nepal starts
from July 16 of this year and ends in July 15 of next year. So, all the
columns in the climate data were aggregated. The values in a column
from July 15 of one year to July 16 of next year were aggregated and
the minimum, maximum, sum and mean were calculated for each
column. Then suitable values for each column were selected. For
example, the sum of precipitation was selected whereas the mean for
the temperature was selected. Similarly, suitable aggregation was
selected for each column and the rest of the columns were dropped.
```
The modified climate data looks like this.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/830570e4-e90b-4380-b19a-bd9138432c2b)

### Modifying Crop Dataset..........................................................................

Then the crop data was modified to merge it with the climate data. The steps
performed for this are below.

```
i) First, the initial crop data was transposed. The transposed dataset is
below.
```
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/30f54bb1-9863-4065-9702-724b37a24dd2)

```
ii) Then the crop name, stat type and year were separated from the ‘Year’
column from the above dataset. For example, PD_P_197980 means
that row has production(P) of paddy(PD) in the year 1979/80. The year
was separated into a column named Year, stat type in to a column
named Stat_Type and crop name into a column named Crop.
```
```
iii) Then all the columns except ‘Year’, ‘Crop’, and ‘Stat_Type’ were
changed into values of a single column and all corresponding values in
a column in a single column named ‘Value’. The crop dataset now
looks like this.
```
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/c2596c35-b53b-4540-b25b-37cf4d467a5c)

```
iv) Then each value of ‘Stat_Type’ was separated into a column with
‘Year’, ‘District’ and ‘Crop’ as index and the values in the column
‘Value’ as values. The modified crop data looks like this.
```
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/aba98763-114f-4f48-948c-2730c08a24b0)

### Merging Crop and Climate Dataset.........................................................

Next, both the modified crop and climate data were merged to obtain the
following dataset. The rows of crop and climate data were merged if the ‘Year’
and ‘District’ columns of both crop and climate data were the same. The merged
data looks like this.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/53d6636a-533c-41fa-ab9d-815c6f6c676f)

### Additional Pre-processing.......................................................................

Some more processing was performed in the dataset.

```
i) The dataset was checked for any null values. None were found.
```
```
ii) Then the Year column was changed into containing only the first of the
fiscal year. For example, the year 1982/83 was now 1982 only.
```
```
iii) Then OneHot Encoding was used to convert the Crop column from
categorical data to numerical data. OneHotEncoding is a method of
converting categorical data into numerical data. With one-hot, we
convert each categorical value into a new categorical column and
assign a binary value of 1 or 0 to those columns. Each integer value is
represented as a binary vector. All the values are zero, and the index is
marked with a 1.
```
```
iv) Then the ‘Area’ and ‘Production’ columns were checked for any zero
values. There were many of those. All of them were removed. If a crop
is not planted at all in a district in a particular year, then the Area for
that is zero. Since we are trying to predict the production of a crop
when planted in a specific area, we do not need such rows. There were
233 such rows.
```
```
v) There were also some nonsensical data like the production of a crop
was 0.18 kilograms per 10,000 meter square. But this data was
collected by MoAD, Nepal and we have no way of verifying it. So,
such data were left as they are. The data after this looked like this.
```
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/ce398ce2-ce06-46c2-9726-e1325507134c)
```
vi) Next, the data was analyzed with the help of various diagrams and
graphs such as distribution plots, correlation matrix, box plots etc.
```

### 4.2.5. Exploratory Data Analysis.......................................................................

```
Now the data was explored and its patterns were analyzed.
```
#### Data Description..............................................................................

Here is a simple description of the features of the dataset.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/caed3748-9343-4a2d-927c-35749670ec15)

#### Distribution of Production for each Crop........................................

Let’s first look at how the production values for each crop are distributed. The x
axis of the graphs show a range of production amount and the y axis shows the
number of times the production in a data entry falls in the specific range of
production.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/69922c84-4e09-4f09-ba23-6223a6361f96)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/f58578a7-8b09-4c01-b527-63473d888889)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/f37c1b20-81ab-451b-95d0-1e2064f8a3ab)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/cd79efa7-3a6a-449d-8bc9-3ab87f0c30db)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/60de2e11-50c0-499f-9407-8ed8378d7c16)

From these plots, we can see that there are many lower values of production in the
dataset whereas as the number of data entries for higher amount of production
values decreases. This may show hints of outliers.

#### Correlation Matrix for each crop.....................................................
Now, let’s take a look at the correlation matrix for each crop for the selected
features.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/e1243d8f-c616-44db-9af3-ac6093130a09)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/5e6f4b20-0aca-4adf-9c82-3e746ed65f64)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/4c6cd5be-3fa4-411d-8ccc-8dd35032a5af)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/40c21779-9806-4831-bb68-4b2b93f6e8e8)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/9b4be1f5-850e-4f00-bb97-14e8ba0e14a9)

A correlation matrix is a tabular representation of the correlation coefficients
between multiple variables in a dataset. It provides a comprehensive overview of
the pairwise correlations among variables, allowing you to understand the strength
and direction of their relationships.
In a correlation matrix, each row and column represent a variable in the dataset.
The cells of the matrix contain the correlation coefficients, which quantify the
degree of linear association between pairs of variables. The correlation
coefficients range from -1 to 1, where -1 indicates a perfect negative correlation, 1
indicates a perfect positive correlation, and 0 indicates no linear correlation.

The correlation matrices above show that the correlation between area and
production is consistently positively high for every crop which makes sense
because the more area the crop is planted on, the more will be the production. The
correlation of other variables also vary for each crop.

#### Box Plot for each crop.....................................................................
A box plot, also known as a box-and-whisker plot, is a statistical visualization that
provides a concise summary of the distribution of a continuous variable. It
displays key statistical measures and identifies potential outliers in the data.
A box plot represents the following statistical measures:
Median (Q2): The horizontal line inside the box represents the median, which is
the middle value that divides the data into two equal halves.
Interquartile Range (IQR): The box in the plot represents the interquartile range,
which is the range between the first quartile (Q1) and the third quartile (Q3). It
contains the central 50% of the data. The length of the box represents the spread
or variability of the data.
Whiskers: The vertical lines, called whiskers, extend from the box to the
minimum and maximum values within a certain range. The range of the whiskers
is typically determined by a predefined factor (often 1.5 times the IQR) or can be
adjusted based on the data and the specific criteria used for outlier detection.
Outliers: Individual data points that fall outside the range of the whiskers are
represented as points beyond the whiskers and are considered potential outliers.
Outliers are points that significantly deviate from the majority of the data.
Below are the box plots for each of the five crops.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/6872d6b2-777a-4404-9fa4-a3ca3b762c3c)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/15a640cc-02c2-40ca-a3d3-33b494cd0a57)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/cf30914d-ec6d-471f-a05c-8f0c63321f40)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/7f46dd54-7b0a-4448-8393-2debf78b8ced)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/9d014a63-1363-4b10-9588-9663c6d9c166)

The middle line inside the colored box in the box plot is the median of the
production for that crop, the left side of the box is lower quartile and the right side
of the box is the upper quartile. The values at which the horizontal lines stop are
the maximum and minimum production values. The dots to the right of the
maximum value show the outliers in the dataset.
We considered removing the outliers but we noticed that the outliers are
consistently showing up in a few districts every year. The districts are different for
each crop but they are noticeably repeating. For barley, outliers with consistently
repeating districts are Rautahat, Jumla, Rolpa, Bajhang, Surkhet, etc. For maize,
the districts are Chitwan, Syangja, Illam, Jhapa, Tanahu. For millet, Kaski,
Syangja, Gorkha, Khotang, Nuwakot, etc. were giving outliers consistently. For
paddy, consistent outliers giving districts were Bara, Jhapa, Morang, Nawalparasi,
erc. And for wheat, the districts were Bara, Rupandehi, Surkhet, Sunsari, Sarlahi,
etc. Since we saw that there were a few consistent districts with high amount of
production every year, we saw it fit to keep the outliers in the data.

## Model Selection...............................................................................................

### Trained and Tested Models.....................................................................

Seven different models were trained and tested on the processed and cleaned data.
The seven models are Linear Regression, Xtreme Gradient Boost (XGBoost),
Random Forest Regression, Gradient Boosted Tree Regression, Support Vector
Regression, Ridge Regression and Lasso Regression.

#### Linear Regression............................................................................

It is a statistical method that is used for predictive analysis. Linear regression
makes predictions for continuous/real or numeric variables such as sales, salary,
age, product price, etc. Linear regression algorithm shows a linear relationship
between a dependent (y) and one or more independent (y) variables, hence called
as linear regression. Since linear regression shows the linear relationship, which
means it finds how the value of the dependent variable is changing according to
the value of the independent variable. The linear regression model provides a
sloped straight line representing the relationship between the variables.
Mathematically, we can represent a linear regression as:

y= a0+a1x+ ε

Here,

Y= Dependent Variable (Target Variable)

X= Independent Variable (predictor Variable)

a0= intercept of the line (Gives an additional degree of freedom)

a1 = Linear regression coefficient (scale factor to each input value).

ε = random error

The values for x and y variables are training datasets for Linear Regression model
representation.

#### Extreme Gradient Boost (XGBoost)

XGBoost is an optimized distributed gradient boosting library designed for
efficient and scalable training of machine learning models. It is an ensemble
learning method that combines the predictions of multiple weak models to
produce a stronger prediction. XGBoost stands for “Extreme Gradient Boosting”
and it has become one of the most popular and widely used machine learning
algorithms due to its ability to handle large datasets and its ability to achieve state-
of-the-art performance in many machine learning tasks such as classification and
regression.

One of the key features of XGBoost is its efficient handling of missing values,
which allows it to handle real-world data with missing values without requiring
significant pre-processing. Additionally, XGBoost has built-in support for parallel
processing, making it possible to train models on large datasets in a reasonable
amount of time.

XGBoost can be used in a variety of applications, including Kaggle competitions,
recommendation systems, and click-through rate prediction, among others. It is
also highly customizable and allows for fine-tuning of various model parameters
to optimize performance.

XGBoost stands for Extreme Gradient Boosting, which was proposed by the
researchers at the University of Washington.

#### Random Forest Regression..............................................................

Random Forest Regression is a supervised learning algorithm that uses ensemble
learning method for regression. Ensemble learning method is a technique that
combines predictions from multiple machine learning algorithms to make a more
accurate prediction than a single model.


The diagram above shows the structure of a Random Forest. You can notice that
the trees run in parallel with no interaction amongst them. A Random Forest
operates by constructing several decision trees during training time and outputting
the mean of the classes as the prediction of all the trees.

A Random Forest Regression model is powerful and accurate. It usually performs
great on many problems, including features with non-linear relationships.
Disadvantages, however, include the following: there is no interpretability,
overfitting may easily occur, we must choose the number of trees to include in the
model.

Random Forest Regression is a supervised machine learning algorithm that
combines the concepts of ensemble learning and decision trees for regression
tasks. It is an extension of the Random Forest algorithm, originally designed for
classification.

In Random Forest Regression, an ensemble of decision trees is built to predict
continuous numerical values rather than discrete class labels. The algorithm
constructs multiple decision trees using different subsets of the training data and
features. Each decision tree independently predicts the target variable, and the
final prediction is obtained by averaging (or taking the median) of the predictions
from all the trees.

Here's a step-by-step overview of how Random Forest Regression works:

Random sampling with replacement: From the original training dataset, random
subsets of the data (bootstrapped samples) are created by sampling with
replacement. Each subset has the same size as the original dataset but may contain
duplicate instances.

Random feature selection: For each decision tree, a random subset of features is
selected as candidates for splitting at each node. This helps to introduce diversity
and reduce the correlation between trees.

Building decision trees: Multiple decision trees are constructed using the
bootstrapped samples and random feature subsets. The trees are grown recursively
by recursively partitioning the data based on the selected features.

Prediction: Once the ensemble of decision trees is built, predictions are made by
aggregating the individual predictions from all the trees. For regression tasks, the
average (or median) of the tree predictions is commonly used as the final
prediction.

Random Forest Regression offers several advantages:

a. Robustness: Random Forest Regression is less prone to overfitting compared to
individual decision trees since it combines multiple trees and reduces variance.

b. Handling non-linear relationships: Random Forest Regression can capture
complex non-linear relationships between the features and the target variable,
making it suitable for a wide range of regression problems.


c. Feature importance: The algorithm provides a measure of feature importance
based on how much each feature contributes to the predictive performance of the
model.

#### Gradient Boosted Tree Regression..................................................

Gradient boosting is a machine learning technique used in regression and
classification tasks, among others. It gives a prediction model in the form of an
ensemble of weak prediction models, which are typically decision trees. When a
decision tree is the weak learner, the resulting algorithm is called gradient-boosted
trees; it usually outperforms random forest. A gradient-boosted trees model is
built in a stage-wise fashion as in other boosting methods, but it generalizes the
other methods by allowing optimization of an arbitrary differentiable loss
function. Like other boosting methods, gradient boosting combines weak
"learners" into a single strong learner in an iterative fashion. It is easiest to explain
in the least-squares regression setting, where the goal is to "teach" a model F to
predict values of the form y’ = F ( x ) by minimizing the mean squared error (1/n)
∑( y’i − yi )^2, where i indexes over some training set of size n of actual values of
the output variable y:

y’i = the predicted value F(xi)

yi = the observed value

n = the number of samples in y

#### Support Vector Regression..............................................................

Support Vector Regression (SVR) is a supervised machine learning algorithm
used for regression tasks. It is a variant of Support Vector Machines (SVMs) that
are primarily used for classification. SVR extends the concepts of SVM to predict
continuous output values instead of discrete class labels.

The goal of SVR is to find a function that approximates the mapping from the
input variables to the target variable by constructing a hyperplane in a high-
dimensional feature space. This hyperplane is chosen to have a maximum margin
from the closest data points, called support vectors. SVR aims to minimize the
error between the predicted and actual target values while maintaining a balance
between accuracy and generalization.

SVR uses a hinge loss function that penalizes the errors exceeding a specified
threshold, called the margin. The margin defines a tube around the regression line
within which errors are ignored. Data points that fall outside this tube contribute
to the loss function. The width of the tube is determined by the hyperparameter
epsilon (ε).

SVR is also influenced by a regularization parameter, C, which controls the trade-
off between minimizing the error and allowing more errors within the margin. A
smaller C value allows for more errors, while a larger C value enforces stricter
fitting.

To solve the SVR optimization problem, various techniques such as quadratic
programming or gradient descent can be used. The kernel trick, which maps the
input variables into a higher-dimensional feature space, can also be employed to
handle nonlinear regression problems.

Overall, SVR is a powerful algorithm for regression tasks as it can handle both
linear and nonlinear relationships between variables. It is particularly effective
when dealing with datasets containing complex patterns and outliers.

#### Ridge Regression.............................................................................

Ridge regression is a regularization technique used in linear regression to mitigate
overfitting and improve the stability of the model. It is particularly useful when
dealing with multicollinearity, which occurs when the predictor variables are
highly correlated with each other.

In ordinary linear regression, the goal is to minimize the sum of squared residuals
between the predicted values and the actual target values. However, in ridge
regression, an additional term is added to the cost function, known as the L2
regularization term. This term introduces a penalty for large coefficient values and
helps to reduce the impact of collinearity.

The ridge regression cost function can be expressed as:

Cost = Sum of squared residuals + λ * (sum of squared coefficients)

In the equation, λ (lambda) is the regularization parameter that controls the
amount of shrinkage applied to the coefficients. A higher λ value leads to greater
shrinkage, resulting in smaller coefficient values and a simpler model.

By adding the regularization term, ridge regression encourages the model to
distribute the coefficients across all predictors rather than assigning a large weight
to a single predictor. This helps to reduce the model's sensitivity to the specific
values of the predictor variables and improves its generalization ability.

Ridge regression can be solved using various optimization techniques, such as
closed-form solution (analytical solution) or iterative methods like gradient
descent. It is important to note that ridge regression assumes that the predictor
variables are standardized or normalized to have zero mean and unit variance to
ensure fair comparison and prevent undue influence of variables with different
scales. Overall, ridge regression is a valuable technique for handling
multicollinearity and reducing overfitting in linear regression models, providing a
good balance between bias and variance.

#### Lasso Regression..............................................................................

Lasso regression, short for Least Absolute Shrinkage and Selection Operator, is a
regularization technique used in linear regression. Similar to ridge regression,
lasso regression helps to mitigate overfitting and improve the stability of the
model. However, lasso regression differs in terms of the type of regularization it
applies.

In lasso regression, instead of adding the sum of squared coefficients to the cost
function as in ridge regression, it adds the sum of the absolute values of the
coefficients, multiplied by a regularization parameter (α) to the cost function. This
is known as L1 regularization.

The lasso regression cost function can be expressed as:

Cost = Sum of squared residuals + α * (sum of absolute values of coefficients)

L1 regularization has a unique property that encourages sparsity in the model,
meaning it tends to force some of the coefficients to become exactly zero. This
property makes lasso regression useful for feature selection, as it can
automatically identify and exclude irrelevant or less important features by setting
their corresponding coefficients to zero. This is in contrast to ridge regression,
which can only shrink the coefficients towards zero but cannot force them to
exactly become zero.

The choice of the regularization parameter (α) in lasso regression determines the
amount of shrinkage applied to the coefficients. Larger α values result in more
shrinkage, potentially leading to more coefficients being set to zero.

### Feature Selection.....................................................................................

Using random forest model, the feature importance of all the features available
was calculated. According to random forest, the features in descending order of
their importance are area, year, temperature range, specific humidity, surface
pressure, wet bulb temperature, relative humidity, max wind speed 10m above
surface, precipitation, wind speed range 50m above surface, wind speed range
10m above surface, wind speed 10m above surface, max temperature, min wind
speed 10m above surface, min temperature, max wind speed 50m above surface,
min wind speed 50m above surface, earth skin temperature, temperature, wind
speed 50m above surface. Among these some of the features with the higher
importance were selected for model training. The selected features are area, year,
temperature range, specific humidity, surface pressure, relative humidity and
precipitation.

### Train/Test Split

The data was split into training and testing data. 80% of the data was used for
training and the remaining 20% for the testing. Considering that it is a time series
problem, the data was split sequentially and not randomly.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/5f298059-6832-4b0f-8304-19c0b6706e14)
Similar approach of splitting data is used for cross validation where the same data
is divided into multiple sets of training and testing data sequentially.

## Overview of Work Done.................................................................................

The following tasks have been done.

i) Collected required crop production data and climate data from various sources.

ii) Preprocessed the data to make it suitable for machine learning model training.

iii) Trained various machine learning models and compared their results to select
the best one.

iv) Developed a webapp where people can use the trained model to predict crop
production and view graphs of various features against the production values.

## Output Obtained..............................................................................................

The final output obtained from this project is a trained machine learning model
and a webapp where users can enter various climate data and obtain a prediction
of the production of crop in metric tons for each district of Nepal. Users can also
view the historic climate and crop production data of all the districts of Nepal.
They can also view the various graphs which show the different features against
the production predicted by the model.

### Comparative Results of Trained Models.................................................

Various machine learning models were trained and evaluated based on different
performance metrics. The models that were evaluated are linear regression,
random forest, extreme gradient boost, gradient boosted tree, support vector
regression, lasso regression and ridge regression. The result of each of these
metrics are given in the table below.

#### Initial Trained Models and their Result

First, all the seven models were trained and evaluated without any optimization
and tuning to see which model performs the best. The result is shown in the table
below.
| |R-squared score|Mean Absolute Error|Root Mean Squared Error|Explained Variance Error|Mean Absolute Percentage Error|
|-|---------------|-------------------|-----------------------|------------------------|------------------------------|
|Linear Regression|0.846|7489.836|16527.442|0.846|2403.202|
|XGBoost|0.889|4856.294|14038.226|0.889|152.469|
|Random Forest|0.885|4855.828|14258.163|0.886|40.914|
|Gradient Boosted Tree|0.896|5331.786|13588.555|0.896|478.788|
|Support Vector|-0.412|20554.671|45059.659|0.030|3429.191|
|Ridge Regression|0.846|7489.713|16527.675|0.846|2402.457|
|Lasso Regression|0.846|7488.812|16527.755|0.846|2401.094|

#### Tuned Models and their Result

Then the models were tuned and optimized using techniques like Grid Search and
Bayesian Optimization.

**Grid Search**

This technique exhaustively searches through a predefined grid of hyperparameter
values and evaluates the model's performance using cross-validation.
GridSearchCV is a scikit-learn class that implements grid search for
hyperparameter tuning and it was used for tuning hyperparameters.


**Bayesian Optimization**

Bayesian optimization techniques use probabilistic models to select the most
promising hyperparameters to evaluate. The algorithm adapts and focuses the
search based on the evaluation results, gradually converging to the optimal set of
hyperparameters. There are various third-party libraries available in Python, such
as scikit-optimize (skopt) or Optuna, that can be used for Bayesian optimization
with scikit-learn models. But for this project, the hyperopt library was used to
perform Bayesian Optimization.

**Result of Tuning and Optimization**

The evaluation metrics for the tuned models are given below.
| |R-squared score|Mean Absolute Error|Root Mean Squared Error|Explained Variance Error|Mean Absolute Percentage Error|
|-|---------------|-------------------|-----------------------|------------------------|------------------------------|
|Linear Regression|0.901|5097.301|10764.765|0.899|1063.590|
|XGBoost|0.969|2168.645|6000.966|0.969|106.916|
|Random Forest|0.965|2112.388|6334.369|0.962|19.435|
|Gradient Boosted Tree|0.966|2746.69|6150.332|0.965|350.772|
|Support Vector|0.880|4720.613|11924.640|0.880|262.644|
|Ridge Regression|0.900|5398.432|10765.694|0.900|1066.46|
|Lasso Regression|0.921|5169.103|9898.374|0.921|834.332|

From the above data, we can see that Random Forest, XGBoost and Gradient
Boosted Tree have the highest r-squared and explained variance score while
having low error metrics such as RMSE and MAPE comparatively. Random
Forest has the lowest MAPE value.

The descriptions of the above used performance metrics and what they mean is
mentioned below.

#### Performance Metrics and their Meanings

The evaluation metrics that are used to evaluate the trained models are mentioned
below.

**4.5.1.3.1. R-squared score**

R-Squared (R²) is a statistical measure used to determine the proportion of
variance in a dependent variable that can be predicted or explained by an
independent variable. In other words, R-Squared shows how well a regression
model (independent variable) predicts the outcome of observed data (dependent
variable). R-Squared is also commonly known as the coefficient of determination.
It is a goodness of fit model for linear regression analysis. An R-Squared value
shows how well the model predicts the outcome of the dependent variable. R-
Squared values range from 0 to 1. An R-Squared value of 0 means that the model
explains or predicts 0% of the relationship between the dependent and
independent variables. A value of 1 indicates that the model predicts 100% of the
relationship, and a value of 0.5 indicates that the model predicts 50%, and so on.

#### Adjusted R-squared score

Adjusted R2 is a corrected goodness-of-fit (model accuracy) measure for linear
models. It identifies the percentage of variance in the target field that is explained
by the input or inputs. R2 tends to optimistically estimate the fit of the linear
regression. It always increases as the number of effects are included in the model.
Adjusted R2 attempts to correct for this overestimation. Adjusted R2 might
decrease if a specific effect does not improve the model. Adjusted R squared is
calculated by dividing the residual mean square error by the total mean square
error (which is the sample variance of the target field). The result is then
subtracted from 1. Adjusted R2 is always less than or equal to R2. A value of 1
indicates a model that perfectly predicts values in the target field. A value that is
less than or equal to 0 indicates a model that has no predictive value.

#### Mean Absolute Error (MAE)

The mean absolute error (MAE) is a metric used to evaluate the performance of a
regression model. It is defined as the average absolute difference between the
predicted values of the model and the true values of the data. The MAE is a
measure of the average magnitude of the errors made by the model in its
predictions, and is a useful metric for evaluating the performance of a model when
the errors are evenly distributed across the data. It is particularly useful when the
errors are symmetrically distributed and there are no extreme outliers, since it is
not sensitive to the presence of outliers.

#### Root Mean Squared Error (RMSE)

The root mean square error (RMSE) measures the average difference between a
statistical model’s predicted values and the actual values. Mathematically, it is the
standard deviation of the residuals. Residuals represent the distance between the
regression line and the data points. RMSE values can range from zero to positive
infinity and use the same units as the dependent (outcome) variable. A value of 0
means that the predicted values perfectly match the actual values, but you’ll never
see that in practice. Low RMSE values indicate that the model fits the data well
and has more precise predictions. Conversely, higher values suggest more error
and less precise predictions.

#### Explained Variance Score

Explained variance (sometimes called “explained variation”) refers to the variance
in the response variable in a model that can be explained by the predictor
variable(s) in the model. The higher the explained variance of a model, the more
the model is able to explain the variation in the data. In regression models, it is
used to quantify the relationship between one or more predictor variables and a
response variable. It is very similar to R-squared value. A value of 0 indicates that
the response variable cannot be explained by the predictor variable(s) at all. A
value of 1 indicates that the response variable can be perfectly explained without
error by the predictor variable(s).

#### Mean Absolute Percentage Error (MAPE)

The mean absolute percentage error (MAPE) measures accuracy of a forecast
system. It measures this accuracy as a percentage, and can be calculated as the
average absolute percent error for each time period minus actual values divided by
actual values. The mean absolute percentage error (MAPE) is the most common
measure used to forecast error, probably because the variable’s units are scaled to
percentage units, which makes it easier to understand. Mean absolute percentage
error measures the average magnitude of error produced by a model, or how far
off predictions are on average. A MAPE value of 20% means that the average
absolute percentage difference between the predictions and the actual values is
20%.

### Learning Curves

A learning curve is a graphical representation that illustrates the relationship
between the performance of a machine learning model and the amount of training
data used to train the model. It plots the model's performance (e.g., accuracy,
error, or any other evaluation metric) on the y-axis against the size of the training
dataset on the x-axis.

The purpose of a learning curve is to help understand how a model's performance
evolves as more data is provided for training. It provides insights into whether a
model would benefit from additional training examples or if it has reached its
optimal performance given the available data.

Below are the learning curves of all the models that were trained.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/8c854f60-475c-470a-9854-287de6ab6953)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/a1f5a0a2-e05a-4066-87c3-b70cb753c439)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/6231d33a-be5e-4cd8-b818-7cf063d5a3db)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/8ef3fbc7-87c7-4803-af7a-a50070db1847)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/df1a7a49-5577-457e-9c99-9d027d2bd399)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/781790fd-005d-428b-bf7a-2b3f174e4a60)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/311f75e1-e8ed-42f7-b16e-3a2730bf631b)

In the learning curves above, the green line is the validation loss and the red line is
the training loss. The shaded area around the lines show range of standard
deviation. The loss function for scoring used is the mean squared error. We can
see that both the training loss and the validation loss for random forest, xgboost
and gradient boost are the lowest. The deviation is also decreasing as the number
of training examples increases. Considering that random forest has low error
metrics as well, the random forest model was selected for implementing in the
web app.

### Actual vs Predicted Values (Training Data)

Below are the graphs of actual values against the predicted values for the training
data.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/15cfd2b3-cb78-44c8-98e6-93042d50e284)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/76753164-e5cc-425d-b1eb-062b5c4538e5)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/9e1d57a4-c2d8-4c1d-9509-53e2e00d60c6)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/7525f024-febc-4d62-b863-34d782cfc545)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/5d8204a0-20bb-4f2f-86a0-0b04186ef1de)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/b144541a-fd56-4005-b222-56a3342077aa)

### Actual vs Predicted Values (Testing Data)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/38c18787-2e4c-412f-8c9b-174afc8c92f9)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/ecbbb7d2-dd96-4046-8388-8418e9d19c29)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/09c95fd0-0847-431d-bc64-9812168d0c4c)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/5dee9d33-3219-4190-beb3-1219a538ffbb)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/6a5eb782-5708-4ea1-bfbc-ec9507bf7e5e)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/86ef0835-375f-4756-95e9-fd3307951355)

After seeing all these metrics and graphs, Random Forest model was chosen and
implemented in the web app because of its high r squared value low error metrics
and low MAPE and good actual vs predicted graph.

### Web App

A simple web app was then built to input the features and get the prediction using
the trained random forest model. Users can select a crop, a district, an area in
hectares where the crop is planted, total precipitation in millimeters of a fiscal
year, the average temperature range in Celsius of that fiscal year, relative
humidity, specific humidity and surface pressure and get a prediction of the
production in metric tons of that crop in a fiscal year. The users can also view the
historical data of crop production in different districts of Nepal. A graph of every
parameter against the production keeping all the other parameter constant can also
be viewed in the web app. This allows the users to analyze hoe the change in one
parameter changes the production of a specific crop. The web app looks like this.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/22fcb91b-7de5-4f3d-9beb-6be8dc06bccd)

This is the home page of the web app where the users can enter their input and get
a prediction for the production of the selected crop.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/2ed323d3-177b-496f-a856-5fd86d3b8194)

This is the page where the users can view the historical data of climate and crop
production. They can also filter the data based on Year, District and Crop.
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/1812db1b-ee71-4d26-9e28-ce7c4ba1e173)

This is the page where the users can see various graphs of different features
against the production values predicted by our model when all other features are
kept constant. This allows the user to see the change in production when one of
the feature changes and all other features are kept constant.


# Analysis and Evaluation

## Analysis of the Output Obtained

Looking at the various metrics that were obtained after training different models,
we narrowed down our attention to three models. They are random forest, extreme
gradient boost and gradient boosted tree. All of them had a similar r-squared value
of around 0.96. The MAE value went back and forth among them with random
forest having the lowest MAE and XGBoost having the lowest RMSE. But
overall, the values were pretty similar to one another. But the MAPE value for
XGBoost and Gradient Boosted Tree were higher compared to Random Forest
which was 19.435%. The lower the MAPE value, the better it is and 19.435% was
the lowest MAPE of them all. A MAPE value above 10% but less than 25% is
generally considered a low but acceptable accuracy in forecasting. Random forest
also had good actual vs predicted graph. Due to these reasons, random forest was
chosen as the model to be implemented in the web app.


# Conclusion

In conclusion, the system is a web-based application that predicts crop production
for crops like paddy, wheat, maize, millet, and barley in Nepal using machine
learning techniques. The system takes in data on crop productions, weather, and
other environmental factors, and uses a random forest model to make predictions
about crop productions. Different machine learning models have been trained and
evaluated and the best one is integrated in the web app. The output is presented in
the form of a user-friendly web application that is easy to use and understand for
farmers and other agricultural stakeholders in Nepal. The system aims to improve
crop productivity, sustainable agricultural practices, and decision-making for
government agencies and agribusinesses, improved crop insurance products, and
improved food security.


# References

```
[1]M. H. Al-Adhaileh and T. H. A. author, "National Library for Medicine," 30
September 2022. [Online]. Available:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9575863/. [Accessed 22
January 2023].
```
```
[2]A. Venugopal, A. S, J. Mani, R. Mathew and P. V. Williams, "Crop Yield
Prediction using Machine Learning Algorithms," International Journal of
Engineering Research and Technology (IJERT), Kottayam, 2021.
```
```
[3]M. Champaneri, D. Chachpara, C. Chandvidkar and M. Rathod, "CROP
YIELD PREDICTION USING MACHINE LEARNING," International
Journal of Science and Research (IJSR), vol. 9, p. 2, 2020.
```
```
[4]L. P. Amgain, S. Adhikari and S. Pandit, "Multi-year Prediction of Rice Yield
under the Changing Climatic Scenarios in Nepal Central Terai Using DSSAT
Crop Model," Journal of Nepal Agriculture Research Council, vol. 8, pp. 88-
100, 2022.
```
```
[5]Y. Liu, S. Wang, J. Chen, B. Chen, X. Wang, D. Hao and L. Sun, "Rice Yield
Prediction and Model Interpretation Based on Satellite and Climatic Indicators
Using a Transformer Method," Remote Sensing, vol. 19, p. 5045, 2022.
```
```
[6]T. v. Klompenburg, A. Kassahun and C. Catal, "Crop yield prediction using
machine learning: A systematic literature review," Computers and Electronics
in Agriculture, vol. 177, p. 105709, 2020.
```
```
[7]"International Center for Integrated Mountain Development," [Online].
Available: https://www.icimod.org/. [Accessed 30 January 2023].
```
```
[8]"Open Data Nepal," [Online]. Available:
https://opendatanepal.com/dataset/district-wise-daily-climate-data-for-nepal.
[Accessed 30 January 2023].
```
```
[9]"NASA Prediction of WorldWide Energy Resources," [Online]. Available:
https://power.larc.nasa.gov/. [Accessed 30 January 2023].
```

# Appendix
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/1c81c432-413f-401d-b7c2-1734ddf0ade7)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/f3fd8981-a56a-4ae4-9c92-9e03f329d003)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/e652710e-f7b5-49b1-af18-424f866bd053)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/84716cec-768e-4bbc-835d-0e39dba4627f)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/6a50431b-d6d0-4e91-9283-0878048a2457)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/056239e5-ac57-4e59-8a9a-294b91a05473)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/6ad86804-06ae-431e-b0cb-493a748fce8d)
![image](https://github.com/Ashutosh652/Crop-Yield-Prediction-Data-Preprocessing/assets/79498496/faba4a6d-87fd-4940-82c6-a3d27e5f6bed)





#Screenshots:
![image](https://github.com/Ashutosh652/crop_predict_frontend/assets/79498496/956f817c-85f7-4d84-a856-bed281158d11)
![image](https://github.com/Ashutosh652/crop_predict_frontend/assets/79498496/5ecd5d49-b6f3-4da4-b116-ddcdf50455da)
![image](https://github.com/Ashutosh652/crop_predict_frontend/assets/79498496/c8f0f676-8d9c-4abe-958e-d90a9acbea33)
![image](https://github.com/Ashutosh652/crop_predict_frontend/assets/79498496/97c1d250-2c23-4352-a2ba-0e849528eaff)
![image](https://github.com/Ashutosh652/crop_predict_frontend/assets/79498496/bf49f7a2-2751-49d6-bc78-892ab55dc24a)
