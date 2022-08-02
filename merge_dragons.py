import argparse
import numpy as np


def main(args):
    print(f"Compute the number of an item of level {args.start_level} "
          f"needed to have the item at level {args.target_level}")
    print("=============================================================================")

    if args.unoptimized:
        print("Unoptimized way - Merges will only be done by 3")
        print("===============================================")

        powers = int(args.target_level) - np.arange(int(args.start_level), int(args.target_level), 1)
        bases = np.full(fill_value=3, shape=(len(powers),))

        print(f'{np.sum(np.power(bases, powers))} items needed to merge until level {args.target_level}')

    else:
        print("Optimized way - Merges will be done by 5")
        print("========================================")

        iterations = int(args.target_level) - int(args.start_level) - 1

        print(f'{int(np.sum(iter_fct_optimized_mode(3.0, iterations)))} '
              f'items needed to merge until level {args.target_level}')


def test_values(args):
    if args.target_level <= 0:
        raise ValueError("Target level must be greater than zero")
    if args.target_level < args.start_level:
        raise ValueError("Target level must be greater than start level")
    if args.start_level < 0:
        raise ValueError("Start level must be grater or equal than zero")


def iter_fct_optimized_mode(n, i):
    res = [n]

    if i > 0:
        i -= 1
        if n % 2 == 0:
            res += iter_fct_optimized_mode((n * 5 / 2), i)

        else:
            res += iter_fct_optimized_mode(((n - 1) * 5 / 2 + 3), i)

    return res


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Items calculator for Merge Dragons game")
    arg_parser.add_argument("--start_level", help="Level of elementary item, e.g item that farmed", default=0)
    arg_parser.add_argument("--target_level", required=True, help="Level of item wanted")
    arg_parser.add_argument("--unoptimized", help="Compute for merge by 3", default=False)

    main(arg_parser.parse_args())
