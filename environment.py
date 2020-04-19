def environment(lines):
    def sections(line):
        if line.startswith('** '):
            line += ' SECTION'

        return line

    return list(map(sections, line))
