def count(fp):
    total_lines = 0
    total_words = 0
    total_bytes = 0
    total_chars = 0
    for line in fp:
        total_lines += 1
        total_words += len(line.split())
        total_bytes += len(line)
        total_chars += len(line.decode())
    return total_lines, total_words, total_chars, total_bytes
