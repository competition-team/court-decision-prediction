"""DepthLogger class.

Log running level of processes.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>

from base_project.common.timer import *


class DepthManager(contextlib.ContextDecorator):
    """Code Depth Manager.

    Attributes:
        depth (int): Current depth of code
        depths (dict): Depths of codes
    """
    depth  = 1
    depths = defaultdict(lambda: 1)

    @classmethod
    def __enter__(cls):
        cls.depth += 1
        return cls

    @classmethod
    def __exit__(cls, *exc):
        cls.depths[cls.depth] = 1   # 다시 level을 1로 초기화
        cls.depth -= 1
        cls.depths[cls.depth] += 1
        return False


def D(fn):
    """Depth logging decorator.

    Example:
        >>> @D
        >>> def f():
        ...     # Depth: 1
        ...     g()
        >>> @D
        >>> def g():
        ...     # Depth: 2
        ...     # do something
    """
    def print_fn(name, args, fn):
        """Print depth of code.

        Args:
            name (str): Function name
            args (tuple): Arguments of the function
            fn (callable): Function
        """
        logs = f"{(DepthManager.depth - 1) * ' ' + name:15}| "
        if len(args) > 0 and isinstance(args[0], object):
            logs = f"{logs}{fn.__module__.split('.')[-1]}."
        log(f"{logs}{fn.__name__}()")

    @wraps(fn)
    def _log(*args, **kwargs):
        """Print depth of code.

        Args:
            args (tuple): Arguments of the function
            kwargs (dict): Keyword arguments of the function

        Returns:
            Return value of the function
        """
        name = f"{'.'.join([str(DepthManager.depths[l]) for l in range(1, DepthManager.depth + 1)]):<10}"
        print_fn(name, args, fn)

        with DepthManager():
            with Timer(name):
                rst = fn(*args, **kwargs)

        return rst

    return _log
