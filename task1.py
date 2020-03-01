from itertools import combinations, product


def read_int(file) -> int:
    """Read int function.

    Args:
        file: A file where the next line will be read.

	Returns:
		Int: A line stripped and converted to an integer.

    """
    return int(file.readline().rstrip())


def parse_file(filepath: str) -> dict:
    """Parse file function.

    Args:
        filepath: The filepath to the test input file.

	Returns:
		d: A dictionary with the test input data.

    """
    d = {}
    with open(filepath, 'r') as file:
        cases = read_int(file)
        for case in range(cases):
            # Pattern is [\nCase1, \nCase2, etc.] So we readline once at the beginning of each case
            file.readline()
            d[case] = {'amount': 0, 'flavours': [], 'options': []}
            d[case]['amount'] = read_int(file)
            d[case]['flavours'] = [int(file.readline().split(' ')[1])
                                   for _ in range(read_int(file))]
            d[case]['options'] = [int(file.readline().split(' ')[1])
                                  for _ in range(read_int(file))]
    return d


def closest_price(d: dict) -> 'txt file':
    """Closest price function.

    Args:
        d: The dictionary with the test input data.

    """
    with open('task1-output.txt', 'w') as file:
        for case in d.keys():
            options = d[case]['options']
            options_combined = combinations(options, 2)
            all_options = set([x+y for x, y in options_combined] + options)
            all_options.add(0)

            flavours = set(d[case]['flavours'])
            prices_product = product(flavours, all_options)
            all_prices = [x+y for x, y in prices_product]
            all_prices.sort()

            closest_price = min(
                all_prices, key=lambda price: abs(price-d[case]['amount']))
            file.write(f'Case #{case+1}: ' + str(closest_price) + '\n')


data = parse_file('task1-test-input.txt')
closest_price(data)