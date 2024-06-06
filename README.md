# Var_procesor

Var_processor is a Python library that can automatically handle common variable operations in projects.

Now it supports automatic saving of specified variables when project exceptions or errors occur.

The project is currently under development, so let's look forward to more wonderful things together.

## Features

- Automatically saves specified local variables to a file.
- Support all types of variables.
- Support variables with the same name in different functions.

## Installation

Install using `pip`:

```sh
pip install var_processor --index-url https://pypi.org/simple  
```

## Usage
```python
from var_processor.functional import save_on_error

@save_on_error(vars=["a", "b", "c"])
def main():
    a = 10
    b = 20.0
    c = {}

    # Raise ZeroDivisionError
    # Variables `a`, `b`, `c` will be automatically saved.
    d = a / 0

if __name__ == "__main__":
    main()
```


