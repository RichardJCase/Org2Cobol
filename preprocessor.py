#!/usr/bin/python3

from data import data
from procedure import procedure
from identification import identification
from environment import environment

def strip_comments(lines):
    def strip(line):
        prefix = '** COMMENT'
        if line.startswith(prefix):
            return '*>' + line[len(prefix):]

        return line
    
    return list(map(strip, lines))

def form_divisions(lines):
    def divisionize(line):
        prefix = '* '
        if line.startswith(prefix):
            return line[len(prefix):] + ' DIVISION'
        
        return line

    return list(map(divisionize, lines))

def delimit(lines):
    def dot(line):
        if line != '':
            line += '.'

        return line

    return list(map(dot, lines))

rules = [strip_comments, form_divisions, identification, environment, data, procedure, delimit]

def preprocess(filename):
    lines = open(filename).read().split('\n')
    for rule in rules:
        lines = rule(lines)

    lines.append('STOP RUN.')
    data = '\n'.join(lines)
    print(data)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Org2COBOL preprocessor')
    parser.add_argument('file', help='File to preprocess')
    args = parser.parse_args()

    preprocess(args.file)

if __name__ == '__main__':
    main()
