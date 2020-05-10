# Regression Task, assumption is that the data is in the right directory
# data can be taken from https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
import os
import ml_automation


if __name__ == '__main__':

    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    f_train = os.path.join(data_dir, 'train.csv')
    f_test = os.path.join(data_dir, 'test.csv')
    
    #training
    ml_automation.automate(path=f_train,
                    ignore_cols=['Id'],
                    out_dir='model')
    
    #predictions
    preds = ml_automation.predict(f_test, model_dir='model')
    print(preds)
