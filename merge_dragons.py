import argparse
import numpy as np
import matplotlib.pyplot as plt


def main(args):
    test_values(args)

    print(f"Compute the number of an item of level {args.start_level} "
          f"needed to have the item at level {args.target_level}")
    print("=============================================================================")

    if args.unoptimized:
        print("Unoptimized way - Merges will only be done by 3")
        print("===============================================")

        res = unoptimized_computation(int(args.start_level), int(args.target_level))

        print(f'{res} items needed to merge until level {args.target_level} '
              f'from items level {args.start_level}')

    else:
        print("Optimized way - Merges will be done by 5")
        print("========================================")

        res = optimized_computation(int(args.start_level), int(args.target_level))

        print(f'{res} items needed to merge until level {args.target_level} '
              f'from items level {args.start_level}')


def test_values(args):
    if int(args.target_level) <= 0:
        raise ValueError("Target level must be greater than zero")
    if int(args.target_level) < int(args.start_level):
        raise ValueError("Target level must be greater than start level")
    if int(args.start_level) < 0:
        raise ValueError("Start level must be grater or equal than zero")


def unoptimized_computation(start_level, target_level):
    powers = target_level - np.arange(start_level, target_level, 1)
    bases = np.full(fill_value=3, shape=(len(powers),))

    return np.sum(np.power(bases, powers))


def optimized_computation(start_level, target_level):
    iterations = target_level - start_level - 1
    res = iter_fct_optimized_mode(3.0, iterations)

    return int(np.sum(res))


def iter_fct_optimized_mode(n, i):
    # TODO : try to make ALL merge by 5 with a counter of remains of division
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
