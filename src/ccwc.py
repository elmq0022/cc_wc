import click


@click.command()
@click.argument("input", type=click.File("rb"))
@click.option("-c", is_flag=True)
@click.option("-l", is_flag=True)
@click.option("-w", is_flag=True)
def main(): ...


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


if __name__ == "__main__":
    main()
