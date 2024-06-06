import numpy as np


class BasePolicy:
    def __init__(self, suffix=None) -> None:
        self.suffix = suffix

    def save(self, path, var):
        pass


class BinPolicy(BasePolicy):
    def __init__(self, suffix=".bin") -> None:
        super().__init__(suffix=suffix)

    def save(self, path, var):
        with open(path + self.suffix, "wb") as f:
            f.write(var)


class DictPolicy(BasePolicy):
    def __init__(self, suffix=".json") -> None:
        super().__init__(suffix)

    def save(self, path, var):
        with open(path + self.suffix, "w") as f:
            f.write(var)


class TextPolicy(BasePolicy):
    def __init__(self, suffix=".txt") -> None:
        super().__init__(suffix)

    def save(self, path, var):
        with open(path + self.suffix, "w") as f:
            f.write(str(var))


class ListPolicy(TextPolicy):
    def save(self, path, var):
        with open(path + self.suffix, "w") as f:
            f.write("\n".join([str(item) for item in var]))


class NumpyPolicy(BasePolicy):
    def __init__(self, suffix=".npy") -> None:
        super().__init__(suffix)

    def save(self, path, var):
        np.save(path + self.suffix, var)


class TensorPolicy(NumpyPolicy):
    def save(self, path, var):
        var = var.cpu().numpy()
        return super().save(path, var)
