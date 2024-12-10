import click


@click.command()
@click.argument("input", type=click.File("rb"))
@click.option("-c")
def main(): ...


def count_bytes(fp):
    totalbytes = 0
    while True:
        chunk = fp.read(1024)
        if not chunk:
            break
        totalbytes += len(chunk)
    return totalbytes


def count_lines(fp):
    return sum(1 for _ in fp)


def count_words(fp):
    return sum(len(line.split()) for line in fp)


if __name__ == "__main__":
    main()
