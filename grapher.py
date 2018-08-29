import matplotlib.pyplot as plt


def index_within_error(list, target, error):
    for index, val in enumerate(list):
        if abs(target - val) < error:
            return index

    raise ValueError("No elements within error bound of target")


def find_cycle(rate_const, initial_val, acceptable_error):
    prevs = [initial_val]

    while True:
        new = rate_const * prevs[-1] * (1 - prevs[-1])

        try:
            cycle_begin_index = index_within_error(prevs, new, acceptable_error)
            break  # only reached if cycle is found
        except ValueError:
            prevs.append(new)

    return prevs[cycle_begin_index:]


def graph_cycles_in_range(initial_val, start, end, step, err):
    x_vals = []
    y_vals = []
    x = start

    while x < end:
        cycle = find_cycle(x, initial_val, err)
        x_vals += [x for _ in cycle]
        y_vals += cycle
        x += step

    plt.scatter(x_vals, y_vals, s=0.1)
    plt.show()

graph_cycles_in_range(0.5, 0, 4, 0.001, 0.00001)
