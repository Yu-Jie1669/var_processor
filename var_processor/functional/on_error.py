from typing import Union
import pdb

from var_processor.collector import VarCollector
from var_processor.saver import VarSaver


def save_on_error(*, vars: Union[tuple, list, str] = None, save_dir: str = "./save_on_error", collect_all=False):
    """
    auto saving specific variables on error
    """

    if collect_all:
        assert vars is None, "If `collect_all` set to True, don't set `vars`"
    else:
        assert vars is not None, "Please set `vars` or set `collect_all` to True"

    collector = VarCollector([vars] if isinstance(vars, str) else vars)
    saver = VarSaver(save_dir)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                collector.collect_on_error(e)
                saver.save(collector.collected_vars)
                raise e

        return wrapper

    return decorator


def pdb_on_error():
    """
    auto begin pdb on error
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                pdb.post_mortem()
                raise e

        return wrapper

    return decorator
