import os
from typing import Union
from datetime import datetime
from .utils import SAVING_RULES


class VarCollector:
    def __init__(self, var_names: Union[tuple, list], save_dir: str) -> None:
        """
        Initialize the VarCollector with a list of variable names and a path to save them.
        """

        assert len(var_names) > 0, "The length of `vars` must be greater than 0"

        now = datetime.now()
        time_str = now.strftime("%Y%m%d%H%M%S")

        self.save_dir = os.path.join(save_dir, time_str)
        os.makedirs(self.save_dir, exist_ok=True)
        self.vars2collect = var_names

    def save_vars(self, local_vars: dict):
        """
        Save the specified variables from the local scope to files.
        """

        missing_vars = []
        saved_vars = {}
        for var_name in self.vars2collect:
            if var_name in local_vars:
                saved_vars[var_name] = local_vars[var_name]
            else:
                missing_vars.append(var_name)

        for var_name, var_val in saved_vars.items():
            try:
                saver = SAVING_RULES[type(var_val).__name__]()
                saver.save(os.path.join(self.save_dir, var_name), var_val)
            except Exception as e:
                print(f"Error saving variable {var_name}: {e}")

        if missing_vars:
            print(f"Warning: The following variables were not found: {missing_vars}")


def save_on_error(*, vars: Union[tuple, list], path: str = "./local_saver"):

    collector = VarCollector(vars, path)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                local_vars = {}
                tb = e.__traceback__
                while tb.tb_next:
                    tb = tb.tb_next
                    frame = tb.tb_frame
                    local_vars.update(frame.f_locals)
                collector.save_vars(local_vars)
                raise e

        return wrapper

    return decorator


if __name__ == "__main__":

    @save_on_error(vars=("a", "b", "c", "xx"))
    def main():

        def aa():
            xx = 100
            a = 100

        def test():
            a = 10
            b = 20
            c = 30

            a = 100

            # raise a ZeroDivisionError
            x = []
            for i in range(100):
                result = a / (5 - i)
                x.append(result)
            print(result)

        aa()
        test()

    main()
