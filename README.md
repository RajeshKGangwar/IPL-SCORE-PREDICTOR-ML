# IPL Teams Score Predictor Using Python, Flask and Machine Learning.
![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![numpy](https://img.shields.io/badge/numpy-1.9.2-lightgrey) ![pandas](https://img.shields.io/badge/pandas-0.19-red) ![scikin-learn](https://img.shields.io/badge/scikit--learn-0.18-green)

## Table of Content
  * [Application Demo](#Application-demo)
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Credits](#credits)


• A DEMO of this web app:

 ![GIF](ipl-score-prediction.gif)


## Overview
This is an Elementry App for Predicting IPL Scores using Historical IPL Data. The App has been Designed using Python, Flask and Machine Learning which takes the following inputs:
• __Batting Team__ <br>
• __Bowling Team__ <br>
• __Venue__: Where the match is being Played. <br>
• __Overs__: Current Over is required in this field. Any value greater than 5 overs is considered over here. for eg: 7.1. <br>
• __Current Runs of Batting Team__ <br>
• __Current Wickets__ <br>
• __Runs scored in last 5 overs__ <br>
• __Fall of wickets in last 5 overs.__ <br>



## Technical Aspect
This App is divided into two part:
1. __main.py__ : This file is responsible for creating an UI for end-user using Flask.

2. __PredictionModel.py__: This file is responsible for preprocessing and model building on the dataset. 
    - Techniques like feature Engineering, feature selection, EDA are applied on the dataset. 
    - __Decision Tree Regressor__ and __Random forest__  are used for model building.

## Installation
The IPL Score Predictor App is coded in python version 3.6. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). Upgrade using pip package if you are using any lower version. The dependencies are mentioned in the requirements.txt file. Go with the below mentioned command for installing them in one go.
```bash
pip install -r requirements.txt
```

## Bug / Feature Request

If you find some bug/defect or if you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/RajeshKGangwar/IPL-SCORE-PREDICTOR-ML/issues).

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank"></a>  <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="numpy" width="150" height="150"/> <img src="https://www.vectorlogo.zone/logos/usepanda/usepanda-ar21.svg" alt="numpy" width="150" height="150"/> 


## Credits
- [Kaggle](https://www.kaggle.com/search?q=ipl+dataset). The ipl dataset is available at Kaggle. It ranges from 1st edition of the ipl till 10th edition.



