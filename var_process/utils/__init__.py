from collections import defaultdict

from .save_policy import BinPolicy, TextPolicy, ListPolicy, DictPolicy, NumpyPolicy, TensorPolicy


SAVING_RULES = defaultdict(
    lambda: BinPolicy,
    {
        "default": BinPolicy,
        "int": TextPolicy,
        "float": TextPolicy,
        "str": TextPolicy,
        "list": ListPolicy,
        "dict": DictPolicy,
        "ndarray": NumpyPolicy,
        "Tensor": TensorPolicy,
    },
)
