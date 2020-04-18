def procedure(lines):
    def paragraph(line):
        prefix = '** '
        if line.startswith(prefix):
            return line[len(prefix):]

        return line

    return list(map(paragraph, lines))
