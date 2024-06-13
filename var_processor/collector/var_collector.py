import os
from typing import Union


class VarCollector:
    def __init__(self, vars2collect: Union[tuple, list] = None) -> None:
        """
        Initialize the VarCollector with a list of variable names.
        """
        self.vars2collect = vars2collect
        self.local_vars = {}

    def collect_on_error(self, e: Exception):
        tb = e.__traceback__
        while tb.tb_next:
            tb = tb.tb_next
            frame = tb.tb_frame

            if self.vars2collect is None:
                self.local_vars.update(frame.f_locals)
            else:
                for name, val in frame.f_locals.items():
                    if name in self.vars2collect:
                        full_name = f"{os.path.basename(frame.f_code.co_filename)}-{frame.f_code.co_name}-{tb.tb_lineno}-{name}"
                        self.local_vars[full_name] = val

    @property
    def collected_vars(self):
        return self.local_vars
