def procedure(lines):
    def paragraph(line):
        prefix = '** '
        if line.startswith(prefix):
            return line[len(prefix):]

        return line

    def substitute(line):
        substitutions = {
            '[[': 'CALL ',
            ']]': ' USING',
            '->': 'RETURNING'
        }

        for key, value in substitutions.items():
            line = line.replace(key, value)

        return line

    def compute(line):
        if line.contains('='):
            return 'COMPUTE ' + line

        return line
        

    transformations = [paragraph, substitute, compute]
    for transformation in transformations:
        lines = map(transformation, lines)

    return list(lines)
