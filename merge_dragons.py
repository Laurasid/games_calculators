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

        res = unoptimized_computation(args.start_level, args.target_level)

        print(f'{res} items needed to merge until level {args.target_level} '
              f'from items level {args.start_level}')

    else:
        print("Optimized way - Merges will be done by 5")
        print("========================================")

        res = optimized_computation(args.start_level, args.target_level)

        print(f'{res} items needed to merge until level {args.target_level} '
              f'from items level {args.start_level}')

    if args.s:
        simulation(args.start_level, args.target_level)


def test_values(args):
    if int(args.target_level) <= 0:
        raise ValueError("Target level must be greater than zero")
    if int(args.target_level) < int(args.start_level):
        raise ValueError("Target level must be greater than start level")
    if int(args.start_level) < 0:
        raise ValueError("Start level must be grater or equal than zero")


def unoptimized_computation(start_level, target_level, short_answer=True):
    powers = target_level - np.arange(start_level, target_level, 1)
    bases = np.full(fill_value=3, shape=(len(powers),))

    if short_answer:
        return np.sum(np.power(bases, powers))
    else:
        return np.power(bases, powers)


def optimized_computation(start_level, target_level, short_answer=True):
    iterations = target_level - start_level - 1
    res = iter_fct_optimized_mode(3.0, iterations)

    if short_answer:
        return np.sum(res)
    else:
        return res


def iter_fct_optimized_mode(n, i):
    # TODO : try to make ALL merge by 5 with a counter of remains of division
    res = [int(n)]

    if i > 0:
        i -= 1
        if n % 2 == 0:
            res += iter_fct_optimized_mode((n * 5 / 2), i)

        else:
            res += iter_fct_optimized_mode(((n - 1) * 5 / 2 + 3), i)

    return res


def simulation(start_level, target_level):
    axe = np.arange(start_level + 1, target_level, 1)
    values_opti = [np.sum(optimized_computation(start_level, target, short_answer=False)) for target in axe]
    values_unopti = [np.sum(unoptimized_computation(start_level, target, short_answer=False)) for target in axe]

    plt.figure()
    plt.subplot(211)
    # ============== Plot config ==============
    plt.title("Evolution of item cost. (log)")
    plt.xlim([0, len(axe) + 1])
    plt.ylabel("Number of base items needed")
    # ========================================

    plt.semilogy(axe, values_opti, color="green", label="Optimized")
    plt.semilogy(axe, values_unopti, color="red", label="Unoptimized")

    plt.legend()

    plt.subplot(212)
    # ============== Plot config ==============
    plt.title("Evolution of item cost. (lin)")
    plt.xlabel("Item level")
    plt.xlim([0, len(axe) + 1])
    plt.ylabel("Number of base items needed")
    # ========================================

    plt.plot(axe, values_opti, color="green", label="Optimized")
    plt.plot(axe, values_unopti, color="red", label="Unoptimized")

    plt.legend()

    plt.show()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Items calculator for Merge Dragons game")
    arg_parser.add_argument("--start_level", help="Level of elementary item, e.g item that farmed", default=0, type=int)
    arg_parser.add_argument("--target_level", required=True, help="Level of item wanted", type=int)
    arg_parser.add_argument("--unoptimized", help="Compute for merge by 3", default=False, type=bool)
    arg_parser.add_argument("-s", help="Active simulation graphs", action="store_true")

    main(arg_parser.parse_args())
