from base_project.common import *


@L
def main(args):
    main1()
    main2()
@L
def main1():
    main11()
    main12()
@L
def main11():
    main111()
    main112()
@L
def main111():
    return
@L
def main112():
    return
@L
def main12():
    return
@L
def main2():
    main21()
@L
def main21():
    return


if __name__ == '__main__':
    # 1. Parsing
    parser = ArgumentParser()
    parser.add_argument('--dev', action='store_true', help='Development mode or not')
    parser.add_argument('--configs', default='configs.yaml', help='Configuration file path (yaml)')
    args = parser.parse_args()

    # 2. Set logger
    LoggerFactory.set(args)

    # 3. Start
    main(args)


