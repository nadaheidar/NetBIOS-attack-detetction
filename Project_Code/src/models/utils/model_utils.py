from sklearn import metrics
def load_data(dataframe):
    """ Drop all string-based features

        Args: dataframe (raw)
        
        Returns: dataframe with removed columns that contain string-based features
    """
    # Only use discrete values
    dataframe.drop(columns=['longest_word','sld'], axis=1, inplace=True,
                   errors='ignore')
    return dataframe
def metrics_calculations(y_test, y_pred):
    """ Calculate accuracy, f score, recall and precision and prints all values
        then return values in a dictionary
        
        Args: resulting y_test and y_pred values from models
        
        Returns: data_log containing the accuracy, f score, recall, and precision
    """
    accuracy = metrics.accuracy_score(y_test, y_pred)
    f1score = metrics.f1_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)

    data_log = {'accuracy': accuracy,
                'f1score': f1score,
                'recall': recall,
                'precision': precision,
                'runtime': 0
                }
    return data_log
