import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from string import Template

if len(sys.argv) != 3:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    input_path = sys.argv[1]
    output_path= sys.argv[2]
    input_df = pd.read_csv(input_path, index_col=0)
    label_data = input_df.legendary
    label_sample = label_data.sample(5)
    feature_data = input_df.drop(['legendary', 'generation', 'total'], axis=1).select_dtypes(exclude=['object'])
    feature_sample = feature_data.sample(5)
    # split data into training_data and test_data
    train_X, test_X, train_y, test_y = train_test_split(feature_data, label_data, train_size=0.8, test_size=0.2,
                                                        random_state=0)
    #  create a random forest classifier
    rf_clf = RandomForestClassifier(n_jobs=2, random_state=0)
    # train the model with training_data
    rf_clf.fit(train_X, train_y)
    # predict testing data
    predicts_val = rf_clf.predict(test_X)

    # Generate a cm
    cm = confusion_matrix(test_y, predicts_val)
    # true positives (TP): These are cases in which we predicted yes (they have the disease), and they do have the disease.
    # true negatives (TN): We predicted no, and they don't have the disease.
    # false positives (FP): We predicted yes, but they don't actually have the disease. (Also known as a "Type I error.")
    # false negatives (FN): We predicted no, but they actually do have the disease. (Also known as a "Type II error.")
    # A CM print value like this:
    # TN, FP
    # FN, TP
    #
    # Generate a cr
    cr = classification_report(test_y, predicts_val)
    # Generate a feature_importance
    feature_importance=list(zip(train_X, rf_clf.feature_importances_))
    # Persist the random forest model with python built in persistent module pickle
    # filename = 'random_forest_pokemon_legendary_classifier.sav'
    # output_file=output_path + "/" + filename
    output_file=output_path
    pickle.dump(rf_clf, open(output_file, 'wb'))
    # load the model from saved file
    # loaded_model = pickle.load(open(output_file, 'rb'))
    # result = loaded_model.score(test_X, test_y)
    # print(result)
    result_str = '###################################################\n' \
                 'The sample of feature data looks like :\n' \
                 '$feature_sample\n' \
                 '###################################################\n' \
                 'The sample of label data looks like:\n' \
                 '$label_sample\n' \
                 '###################################################\n' \
                 'The Confusion Matrix of the random forest model is:\n' \
                 '$cm \n' \
                 '###################################################\n' \
                 'The Classification report of the random forest model is:\n' \
                 '$cr \n' \
                 '###################################################\n' \
                 'The Feature importance in the random forest model is:\n' \
                 '$feature_importance \n' \
                 '###################################################\n' \
                 'The he random forest model is saved in path:\n' \
                 '$output_file \n' \
                 '###################################################\n'
    temp_obj = Template(result_str)

    result = temp_obj.substitute(label_sample=label_sample, feature_sample=feature_sample, cm=cm, cr=cr,
                                 feature_importance=feature_importance,output_file=output_file)
    print(result)

# First arg is input csv file, 2nd arg is the output path of the ml model
# python LegendaryPokemonDT.py /tmp/pokemon-cleaned.csv /tmp/random_forest_pokemon_legendary_classifier.sav
