"""Level class.

Log running level of processes.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>

from base_project.common.timer import *


class Level:
    """Code의 level(깊이)을 저장하는 class

    :cvar int val: Code의 깊이
    :cvar defaultdict vals: 각 code의 깊이마다 진행도를 저장하는 dict
    """
    val = 1
    vals = defaultdict(lambda: 1)

    @classmethod
    def step_into(cls):
        """Code 깊이 증가
        """
        cls.val += 1

    @classmethod
    def step_out(cls):
        """Code 깊이 감소
        """
        cls.val -= 1
        cls.vals[cls.val] += 1


def L(fn):
    """Code의 level을 관리하는 decorator

    Example:
        >>> @L
        >>> def f():
        ...     ## Level: 1
        ...     g()
        >>> @L
        >>> def g():
        ...     ## Level: 2
        ...     # do something
    """
    def print_fn(name, args, fn):
        """Code의 level을 출력

        Args:
            name (str): Code level에 해당하는 이름
            args (tuple): 함수의 arguments
            fn (callable): 함수
        """
        logs = f"> {name}| "
        if len(args) > 0 and isinstance(args[0], object):
            logs = f"{logs}{fn.__module__.split('.')[-1]}."
        log(f"{logs}{fn.__name__}()")

    @wraps(fn)
    def _log(*args, **kwargs):
        """Code의 level을 출력

        Args:
            args (tuple): 함수의 arguments
            kwargs (dict): 함수의 keyword arguments

        Returns:
            함수의 return value
        """
        name = f"{'.'.join([str(Level.vals[l]) for l in range(1, Level.val + 1)]):<10}"

        print_fn(name, args, fn)
        Level.step_into()

        with Timer(name):
            rst = fn(*args, **kwargs)

        Level.step_out()
        return rst

    return _log
