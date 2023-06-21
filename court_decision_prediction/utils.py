from court_decision_prediction.common import *


class PATH:
    root   = abspath(dirname(dirname(__file__)))
    yaml   = join(root, 'court_decision_prediction/configs.yaml')
    data   = join(root, yaml2dict(yaml)['data_dir'])
    train  = join(data, 'train.csv')
    test   = join(data, 'test.csv')
    submit = join(data, 'sample_submission.csv')
