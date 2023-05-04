# base-project: Base project structure for machine learning project

# Summary
### 1. Entrypoint
[`base_project/launch.py`](https://github.com/alchemine/base-project/blob/main/base_project/launch.py)

### 2. `common`: Commonly used package
`from base_project.common import *`

### 3. `configs.yaml`: Configuration

### 4. `poetry`: Package managing tool

---

# 1. Directory Structure
```bash
.
├── README.md
├── base_project
│   ├── common
│   │   ├── __init__.py
│   │   ├── env.py
│   │   ├── level_logging.py
│   │   ├── logging.py
│   │   ├── timer.py
│   │   └── utils.py
│   ├── configs.yaml
│   └── launch.py
├── poetry.lock
└── pyproject.toml
```

# 2. `common` Package
## 2.1 Import
```python
from base_project.common import *
```
See details in [base_project/common/\__init\__.py](https://github.com/alchemine/base-project/blob/main/base_project/common/__init__.py).

## 2.2 Module Dependency
```
     env.py      : Environment module (library importing, option setting)
       ↓
    utils.py     : Utility module (function, class)
       ↓
   logging.py    : Logging module
       ↓
    timer.py     : Timer module
       ↓
level_logging.py : Level logging module
```

## 2.3 Logging
- `log()`: log to `stdout`
- `dlog()`: log to `stdout` when development option is present
  - Development option: `--dev` \
   See details in [`base_project/launch.py`](https://github.com/alchemine/base-project/blob/main/base_project/launch.py).
- Log directory: `log_dir` in [`base_project/configs.yaml`](https://github.com/alchemine/base-project/blob/main/base_project/configs.yaml)

```python
from base_project.common.logging import log, dlog, initialize_logger
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--dev', action='store_true', help='Development mode or not')
parser.add_argument('--configs', default='configs.yaml', help='Configuration file path (yaml)')
args = parser.parse_args()

initialize_logger(args)

if args.dev:
    log("STDOUT O, FILE O")
    dlog("STDOUT O, FILE O")
else:
    log("STDOUT O, FILE O")
    dlog("STDOUT X, FILE O")
```

## 2.4 Timer
- Context manager
    - `Timer(name)`
        ```python
        from base_project.common.timer import Timer
      
        with Timer("Code1"):
            sleep(1)
        ```

        ```
        * Code1        | 1.00s (0.02m)
      ```
- Decorator
    - `@Timer(name)`
    - `@T`
      ```python
      from base_project.common.timer import Timer, T
        
      @Timer()
      def fn1():
          sleep(1)
            
      @T
      def fn2():
          sleep(1)
      
      fn1()
      fn2()
      ```

      ```
      * Elapsed time | 1.00s (0.02m)
      * Elapsed time | 1.00s (0.02m)
      ```

# 2.5 Level Logging
- Decorator: `@L`
    ```python
    from base_project.common.level_logging import L
      
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
        
    main()
    ```

    ```
    1              | main()
     1.1           | main1()
      1.1.1        | main11()
       1.1.1.1     | main111()
    * 1.1.1.1      | 0.00s (0.00m)
       1.1.1.2     | main112()
    * 1.1.1.2      | 0.00s (0.00m)
    * 1.1.1        | 0.00s (0.00m)
      1.1.2        | main12()
    * 1.1.2        | 0.00s (0.00m)
    * 1.1          | 0.00s (0.00m)
     1.2           | main2()
      1.2.3        | main21()
    * 1.2.3        | 0.00s (0.00m)
    * 1.2          | 0.00s (0.00m)
    * 1            | 0.00s (0.00m)
    ```
