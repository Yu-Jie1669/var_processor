import numpy as np


class TypeSaver:
    def __init__(self, suffix=".bin") -> None:
        self.suffix = suffix

    def save(self, path, var):
        with open(path + self.suffix, "wb") as f:
            f.write(var)


class TextSaver(TypeSaver):
    def __init__(self, suffix=".txt") -> None:
        super().__init__(suffix)

    def save(self, path, var):
        with open(path + self.suffix, "w") as f:
            f.write(str(var))


class DictSaver(TypeSaver):
    def __init__(self, suffix=".json") -> None:
        super().__init__(suffix)

    def save(self, path, var):
        with open(path + self.suffix, "w") as f:
            f.write(var)


class NumpySaver(TypeSaver):
    def __init__(self, suffix=".npy") -> None:
        super().__init__(suffix)

    def save(self, path, var):
        np.save(path + self.suffix, var)


class ListSaver(TextSaver):
    def save(self, path, var):
        with open(path + self.suffix, "w") as f:
            f.write("\n".join([str(item) for item in var]))


class TensorSaver(NumpySaver):
    def save(self, path, var):
        var = var.cpu().numpy()
        return super().save(path, var)
