def get_division_bounds(lines, division_name):
    line_len = len(lines)
    start = None
    for line_index in range(line_len):
        if lines[line_index] == f'{division_name} DIVISION':
            start = line_index
            break

    if start == None:
        raise Exception(f'No {division_name} division.')

    end = len(lines)
    for line_index in range(line_index + 1, line_len):
        if lines[line_index].endswith('DIVISION'):
            end = line_index
            break

    return (start, end)
