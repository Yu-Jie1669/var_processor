from collections import defaultdict
from .type_saver import TypeSaver, TextSaver, DictSaver, ListSaver, NumpySaver, TensorSaver


SAVING_RULES = defaultdict(
    lambda: TypeSaver,
    {
        "int": TextSaver,
        "float": TextSaver,
        "str": TextSaver,
        "list": ListSaver,
        "dict": DictSaver,
        "ndarray": NumpySaver,
        "Tensor": TensorSaver,
    },
)


if __name__ == "__main__":
    print(SAVING_RULES["a"])
    print(SAVING_RULES["list"])
