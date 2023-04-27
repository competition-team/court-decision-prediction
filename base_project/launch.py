from base_project.common import *


@L
def main(args):
    log("main1")
    main2()

@L
def main2():
    log("main2")



if __name__ == '__main__':
    # 1. Parsing
    parser = ArgumentParser()
    parser.add_argument('--debug', default=True, help='Debugging mode or not')
    parser.add_argument('--configs', default='configs.yaml', help='Configuration file path (yaml)')
    args = parser.parse_args()

    # 2. Set logger
    LoggerFactory.set(args)

    # 3. Start
    main(args)
