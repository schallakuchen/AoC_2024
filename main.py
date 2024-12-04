import importlib

DAY = 4


def main():
    run_day(DAY)


def run_day(x):
    package_name = "days"
    module_name = f"{package_name}.d{x:02d}"
    function_name = f"d{x:02d}"

    module = importlib.import_module(module_name)

    day_to_run = getattr(module, function_name)
    day_to_run()


if __name__ == '__main__':
    main()
