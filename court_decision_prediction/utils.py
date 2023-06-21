from court_decision_prediction.common import *


class PATH:
    root   = abspath(dirname(dirname(__file__)))
    yaml   = join(root, 'court_decision_prediction/configs.yaml')
    train  = join(root, yaml2dict(yaml)['data_dir'], 'train.csv')
    test   = join(root, yaml2dict(yaml)['data_dir'], 'test.csv')
    submit = join(root, yaml2dict(yaml)['data_dir'], 'sample_submission.csv')
