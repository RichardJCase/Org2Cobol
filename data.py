def data(lines):
    def sections(line):
        if line.startswith('** '):
            line += ' SECTION'

        return line
    
    def primatives(line):
        prim_map = {
            '=': 'VALUE',
            'STRING(': 'PIC X(',
            'CHAR': 'PIC X',
            'SHORT': 'PIC S9(4) USAGE IS BINARY',
            'USHORT': 'PIC 9(4) USAGE IS BINARY',
            'INT': 'PIC S9(9) USAGE IS BINARY',
            'UINT': 'PIC 9(9) USAGE IS BINARY',
            'FLOAT': 'COMP-1',
            'DOUBLE': 'COMP-2'
        }

        for key, value in prim_map.items():
            line = line.replace(key, value)

        return line
    
    transformations = [sections, primatives]
    for transformation in transformations:
        lines = map(transformation, lines)

    return list(lines)
    
