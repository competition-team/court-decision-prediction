from court_decision_prediction.common import *
from sklearn.preprocessing import OneHotEncoder


class PATH:
    root   = abspath(dirname(dirname(__file__)))
    yaml   = join(root, 'court_decision_prediction/configs.yaml')
    data   = join(root, yaml2dict(yaml)['data_dir'])
    train  = join(data, 'train.csv')
    test   = join(data, 'test.csv')
    sample = join(data, 'sample_submission.csv')
    submit = join(root, 'submission')


def append_party_group(data):
    states = list(map(str.lower,
                      ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                       'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
                       'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                       'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                       'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']))
    cities = ['new york', 'los angeles', 'chicago', 'houston', 'phoenix', 'philadelphia', 'san antonio', 'san diego',
              'dallas', 'san francisco', 'oakland', 'austin', 'jacksonville', 'san jose', 'california', 'indianapolis',
              'seattle', 'denver', 'washington', 'boston', 'el paso', 'nashville', 'detroit', 'oklahoma', 'portland',
              'las vegas', 'memphis', 'louisville', 'baltimore', 'milwaukee', 'albuquerque', 'tucson', 'fresno', 'mesa',
              'sacramento', 'atlanta', 'kansas city', 'colorado springs', 'omaha', 'raleigh', 'miami', 'long beach',
              'virginia beach', 'oakland', 'minneapolis', 'tulsa', 'tampa', 'arlington', 'new orleans', 'wichita',
              'cleveland', 'bakersfield', 'aurora', 'anaheim', 'honolulu', 'santa ana', 'riverside', 'corpus christi',
              'lexington', 'stockton', 'anchorage', 'st. paul', 'newark', 'buffalo', 'plano', 'henderson', 'fort wayne',
              'greensboro', 'lincoln', 'glendale', 'chandler', 'st. petersburg', 'jersey city', 'scottsdale', 'norfolk',
              'madison', 'orlando', 'birmingham', 'baton rouge', 'durham', 'laredo', 'garland', 'chula vista',
              'riverside', 'hialeah', 'lubbock', 'reno', 'north las vegas', 'akron', 'gilbert', 'rochester', 'boise',
              'spokane']
    def generate_fn(col):
        def fn(row):
            party = row[col].lower()

            keywords1 = ['united states', 'federal', 'commision', 'commodity', 'national']
            keywords2 = states + cities + ['school board', 'city', 'republic', 'region', 'district', 'county']
            keywords3 = ['corporation', 'inc', 'company', 'bank', 'association', 'llc', 'co.', 'hospital', 'usa', 'school', 'group', 'office', 'department']
            keywords4 = [',', 'et al']

            for grp, keywords in zip(['united states', 'states', 'group1', 'group2'],
                                    [keywords1, keywords2, keywords3, keywords4]):
                for key in keywords:
                    if key in party:
                        return grp
            return 'indiv'
        return fn

    data['first_party_grp']  = data.apply(generate_fn('first_party'), axis=1)
    data['second_party_grp'] = data.apply(generate_fn('second_party'), axis=1)
    data.drop(columns=['first_party', 'second_party'], inplace=True)


def get_vector(vectorizer, df, train_mode):
    if train_mode:
        X_facts = vectorizer.fit_transform(df['facts'])
    else:
        X_facts = vectorizer.transform(df['facts'])
    X_party1 = vectorizer.transform(df['first_party'])
    X_party2 = vectorizer.transform(df['second_party'])

    X = np.concatenate([X_party1.todense(), X_party2.todense(), X_facts.todense()], axis=1)
    return np.asarray(X)
