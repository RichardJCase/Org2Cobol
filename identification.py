from datetime import date
import division

def identification(lines):
    (start, end) = division.get_division_bounds(lines, 'IDENTIFICATION')

    data = [f'DATE-WRITTEN. {date.today()}']

    return lines[0:start+1] + data + lines[start+1:len(lines)]
