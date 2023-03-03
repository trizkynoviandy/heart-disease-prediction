import joblib
import pandas as pd

def input_data(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13):
    input_data = [[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]]
    new_data = pd.DataFrame(input_data, columns = ['age', 'sex', 'cp',	'trestbps', 'chol',	'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    return new_data

def prediction(model, data):
    result = model.predict(data)
    return result[0]

if __name__ == "__main__" :
    loaded_model = joblib.load("model/heart_disease_model.sav")
    print('\n----------------Heart Disease Prediction----------------\n')
    print('Heart Disease Prediction\n')
    print('Please input the variables: ')
    var_1 = input('1. age : ')
    var_2 = input('2. sex : ')
    var_3 = input('3. cp : ')
    var_4 = input('4. trestbps : ')
    var_5 = input('5. chol : ')
    var_6 = input('6. fbs : ')
    var_7 = input('7. restecg : ')
    var_8 = input('8. thalach : ')
    var_9 = input('9. exang : ')
    var_10 = input('10. oldpeak : ')
    var_11 = input('11. slope : ')
    var_12 = input('12. ca : ')
    var_13 = input('13. thal : ')
    new_data = input_data(var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10, var_11, var_12, var_13)
    predict = prediction(loaded_model, new_data)
    print('\Heart Disease Prediction Prediction :', predict)