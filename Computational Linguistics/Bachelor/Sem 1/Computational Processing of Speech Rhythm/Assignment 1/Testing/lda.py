import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

path = "/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv"
data = pd.read_csv(path)

features = data[["nPVI_C_tier1", "nPVI_V_tier1", "varcoC_tier1", "varcoV_tier1"]]
target = data['dialect']
encoder = LabelEncoder()
target_encoded = encoder.fit_transform(target)

X_train, X_test, y_train, y_test = train_test_split(features, target_encoded, test_size=0.2, random_state=0)

lda_model = LinearDiscriminantAnalysis()
lda_model.fit(X_train, y_train)
y_pred = lda_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
