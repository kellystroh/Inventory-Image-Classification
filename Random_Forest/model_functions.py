import numpy as np
import pandas as pd


def pick_ylabels(column):
    df_test = pd.read_csv('data/test_labels.csv')
    df_train = pd.read_csv('data/train_labels.csv')
    y_train = df_train[column].copy().astype('category').cat.codes
    y_test = df_test[column].copy().astype('category').cat.codes
    return (y_train.values, y_test.values)
def multi_index_counts(col, col2):
    df_test = pd.read_csv('data/test_labels.csv')
    counts = df_test.groupby([col, col2]).count().id
    return counts

def category_codes(column):
    df_test = pd.read_csv('data/test_labels.csv')
    df_train = pd.read_csv('data/train_labels.csv')
    _, ytest = pick_ylabels(column)
    cat_codes = {}
    cat_code_list = []
    for i in range(len(df_test[column].value_counts().index)):
        s = i
        t = df_test[column].value_counts().index[i]
        cat_codes[s] = t
    return cat_codes

def test_counts_by_cat(column):
    df_test = pd.read_csv('data/test_labels.csv')
    df_train = pd.read_csv('data/train_labels.csv')
    _, ytest = pick_ylabels(column)
    test_counts_dict = {}
    test_counts = []
    for i in range(len(df_test[column].value_counts().index)):
        s = df_test[column].value_counts().values[i]
        t = df_test[column].value_counts().index[i]
        test_counts_dict[t] = s
        test_counts.append([t, s])
    return test_counts

def train_counts_by_cat(column):
    df_test = pd.read_csv('data/test_labels.csv')
    df_train = pd.read_csv('data/train_labels.csv')
    y_train = pick_ylabels(column)
    train_counts_dict = {}
    train_counts = []
    for i in range(len(df_test[column].value_counts().index)):
        s = df_train[column].value_counts().values[i]
        t = df_train[column].value_counts().index[i]
        train_counts_dict[t] = s
        train_counts.append([t, s])
    return test_counts

def class_weights(column):
    df_test = pd.read_csv('data/test_labels.csv')
    df_train = pd.read_csv('data/train_labels.csv')
    train_counts = train_counts_by_cat(column)
    counts_list = []
    ratio_list = []
    ratio_dict = {}
    for x in test_counts:
        counts_list.append(x[1])
    z = sum(counts_list)
    for x in counts_list:
        if np.round(x/z, 3) ==0:
            ratio_list.append(.001)
        else: 
            ratio_list.append(np.round(x/z, 2))
    for k, v in enumerate(ratio_list):
        ratio_dict[k] = v
    return ratio_dict
def model_results(model, column):
    yhat = model.predict(X_test)
    _ , ytest = pick_ylabels(column)
    accuracy = accuracy_score(ytest, yhat)
    print( 'Accuracy Score: ', accuracy )
    recall = recall_score(ytest, yhat, average='weighted')
    print( 'Recall Score: ', recall)
    y_proba = model.predict_proba(X_test)
    wrong_id_list = []
    pred_cat_list = []
    real_cat_list = []
    for row_idx in range(len(ytest)):
        if ytest[row_idx]!=yhat[row_idx]:
            wrong_id_list.append(row_idx)
            pred_cat_list.append(yhat[row_idx])
            real_cat_list.append(ytest[row_idx])

    arr = np.array([ real_cat_list, pred_cat_list])
    arr = arr.transpose()
    wrong_df = pd.DataFrame( arr, index= wrong_id_list, columns = ['actual', 'predicted'] )
    return (accuracy, recall, wrong_df)

