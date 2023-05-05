from base_project.common import *


@D
def main(args):
    main1()
    main2()
@D
def main1():
    main11()
    main12()
@D
def main11():
    main111()
    main112()
@D
def main111():
    return
@D
def main112():
    return
@D
def main12():
    return
@D
def main2():
    main21()
@D
def main21():
    return


if __name__ == '__main__':
    # 1. Parsing
    parser = ArgumentParser()
    parser.add_argument('--dev', action='store_true', help='Development mode or not')
    parser.add_argument('--configs', default='base_project/configs.yaml', help='Configuration file path (yaml)')
    args = parser.parse_args()

    # 2. Initialize logger
    initialize_logger(args)

    # 3. Start
    main(args)
