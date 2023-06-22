from court_decision_prediction.utils import *
from dacon_submit_api import dacon_submit_api


if __name__ == '__main__':
    # 1. Initialize logger
    initialize_logger(PATH.yaml)

    # 2. Predict
    exp_name = '1_baseline'
    main = import_module(f"court_decision_prediction.exp.{exp_name}").main
    main()
    # exp_name = '2_ones'
    #
    # file = pd.read_csv(join(PATH.submit, f"{exp_name}.csv"))
    # file = file.iloc[:, 1:]
    # file.to_csv(join(PATH.submit, f"{exp_name}-tmp.csv"), index=False)

    # 3. Submission
    result = dacon_submit_api.post_submission_file(
        join(PATH.submit, f"{exp_name}-tmp.csv"),
        os.environ['DACON_TOKEN'],
        '236112',
        'Alchem',
        '2_ones')