# base-project: Base project structure for machine learning project

# 1. Directory structure
```bash
.
├── README.md
├── base_project
│   ├── common
│   │   ├── __init__.py
│   │   ├── env.py
│   │   ├── level.py
│   │   ├── logging.py
│   │   ├── timer.py
│   │   └── utils.py
│   ├── configs.yaml
│   └── launch.py
├── poetry.lock
└── pyproject.toml
```

# 2. Poetry
[Poetry](https://alchemine.github.io/2023/04/07/poetry.html) 참고


# 3. `common` Dependency
```
env.py ── utils.py ── logging.py ── timer.py ── level.py
```


# 4. Logging
- `base_project.common.logging.log()`: Log for debugging/running mode
- `base_project.common.logging.dlog()`: Log for debugging mode
- Log directory: `configs.yaml`

```python
from base_project.common.logging import log, dlog

# args: see details in launch.py
if args.debug:
    log("STDOUT O, FILE O")
    dlog("STDOUT O, FILE O")
else:
    log("STDOUT O, FILE O")
    dlog("STDOUT X, FILE O")
```
