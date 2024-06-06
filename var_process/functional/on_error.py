from typing import Union
from var_process.collector import VarCollector
from var_process.saver import VarSaver


def save_on_error(*, vars: Union[tuple, list], save_dir: str = "./save_on_error", collect_all=False):

    collector = VarCollector(vars, collect_all=collect_all)
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
