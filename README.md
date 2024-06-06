# Var_procesor

Var_procesor is a Python decorator that automatically saves specified local variables to a file when a function raises an error, facilitating post-mortem debugging.

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
    d = a / 0

if __name__ == "__main__":
    main()
```




