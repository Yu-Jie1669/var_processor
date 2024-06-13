from var_processor.functional import save_on_error, pdb_on_error


@pdb_on_error()
def main():
    a = "s"
    b = 1

    def a():
        a = "gg"
        tt = 1 / 0

    a()
    b = 1 / 0
    print("ss")


if __name__ == "__main__":
    main()
