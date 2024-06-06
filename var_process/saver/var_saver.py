from datetime import datetime
import os
from var_process.utils import SAVING_RULES


class VarSaver:
    def __init__(self, save_dir: str) -> None:
        """
        Initialize the VarSaver with a path to save vars
        """

        now = datetime.now()
        time_str = now.strftime("%Y%m%d%H%M%S")

        self.save_dir = os.path.join(save_dir, time_str)
        os.makedirs(self.save_dir, exist_ok=True)

    def save(self, local_vars: dict):
        for var_name, var_val in local_vars.items():
            try:
                save_policy = SAVING_RULES[type(var_val).__name__]()
                save_policy.save(os.path.join(self.save_dir, var_name), var_val)
            except Exception as e:
                print(f"Error saving variable {var_name}: {e}")
