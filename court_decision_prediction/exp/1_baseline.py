from court_decision_prediction.utils import *

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

EXP_NAME = Path(__file__).stem


def get_vector(vectorizer, df, train_mode):
    if train_mode:
        X_facts = vectorizer.fit_transform(df['facts'])
    else:
        X_facts = vectorizer.transform(df['facts'])
    X_party1 = vectorizer.transform(df['first_party'])
    X_party2 = vectorizer.transform(df['second_party'])

    X = np.concatenate([X_party1.todense(), X_party2.todense(), X_facts.todense()], axis=1)
    return np.asarray(X)

def main():
    # 1. Load data
    train = pd.read_csv(PATH.train)
    test  = pd.read_csv(PATH.test)


    # 2. Data Preprocessing
    vectorizer = TfidfVectorizer()
    X_train = get_vector(vectorizer, train, True)
    Y_train = train['first_party_winner']
    X_test  = get_vector(vectorizer, test, False)


    # 3. Define model & Train
    model = LogisticRegression()
    model.fit(X_train, Y_train)


    # 4. Inference & Submission
    submit = pd.read_csv(PATH.sample)
    submit['first_party_winner'] = model.predict(X_test)
    submit.to_csv(join(PATH.submit, f"{EXP_NAME}.csv"))
