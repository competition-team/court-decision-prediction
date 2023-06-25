from court_decision_prediction.utils import *
from dacon_submit_api import dacon_submit_api


if __name__ == '__main__':
    exp_name = '2_party_group_only'
    result = dacon_submit_api.post_submission_file(
        join(PATH.submit, f"{exp_name}.csv"),
        os.environ['DACON_TOKEN'],
        '236112',
        'Alchem',
        exp_name)
