def get_class_metrics(class_report, column, df):
    '''
    input: 
        - a class report (classification_report) from sklearn
        - str name of the column you want to create
        - a dataframe (specific to this project-- rows are the 9 genres + weighted avg.)

    example: get_class_metrics(baseline_rf_class_report, 'baseline_rf', scores_df)
    example output: Will add columns ['baseline_rf_recall', 'baseline_rf_precision', 'baseline_rf_f1-score']
    to the scores_df with the values for each genre and the weighted avg. 
    '''
    metrics = ['recall', 'f1-score', 'precision']
    for metric in metrics:
        values = []
        for genre in range(0, 9):
            genre = str(genre)
            values.append(class_report[genre][metric])
        if metric == 'recall':
            values.append(class_report['weighted avg']['recall'])
        elif metric == 'f1-score':
            values.append(class_report['weighted avg']['f1-score'])
        else:
            values.append(class_report['weighted avg']['precision'])
        df[column + '_' + metric] = values
    return None