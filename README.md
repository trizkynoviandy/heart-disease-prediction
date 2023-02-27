# Heart Disease Classification

Heart disease is a serious health condition that affects millions of people worldwide. Early detection of heart disease can lead to more effective treatment and improved health outcomes. In this project, we aim to develop a machine learning model using the Decision Tree algorithm to predict the presence or absence of heart disease based on patient data and provide insight into the factors that contribute to the development of heart disease.

## Dataset

The heart disease dataset used to build the model was originally available in the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease), but in this project, I used preprocessed dataset from [Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci?resource=download). The dataset contains 297 instances and 14 attributes including age, sex, chest pain type, resting blood pressure, serum cholesterol levels, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise induced angina, ST depression induced by exercise relative to rest, slope of the peak exercise ST segment, number of major vessels colored by fluoroscopy, thallium stress test result, and the condition variable indicating the presence (disease) or absence of heart disease (no disease).

## Result

The results on the train and test set are shown below:

| Metric | Training Set | Testing Set |
| ------| ------------ | ----------- |
| Accuracy | 0.87 | 0.70 |
| Precision | 0.87 | 0.70 |
| Recall| 0.87 | 0.70 |
| F1-Score | 0.87 | 0.70 |

## Conclusion
In conclusion, this repository provides code and data to build a machine learning model for heart disease prediction using a Decision Tree algorithm. The model achieved a decent performance on the testing set, with an accuracy, precision, recall, and f1 score of 0.70.

## Requirements 

In order to run the python script and notebook, you will need to have the following packages installed:
* matplotlib
* numpy
* pandas
* scikit-learn
* seaborn

## Disclaimer

It is important to note that this machine learning model is not intended to replace medical diagnosis by a trained healthcare professional. This model should only be used as an additional tool to assist healthcare professionals in making accurate diagnoses and treatment decisions. It is highly recommended to seek medical advice from a licensed healthcare professional for any health concerns.
