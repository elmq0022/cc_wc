import click

from .cc_wc import count

help_text = """
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
printable characters delimited by white space.

With no FILE, or when FILE is -, read standard input.
"""


@click.command(help=help_text)
@click.argument("files", nargs=-1, type=click.File("rb"))
@click.option(
    "-c",
    "--bytes",
    "count_bytes",
    is_flag=True,
    help="print the byte counts",
)
@click.option(
    "-l",
    "--lines",
    "count_lines",
    is_flag=True,
    help="print the line counts",
)
@click.option(
    "-w",
    "--words",
    "count_words",
    is_flag=True,
    help="print the word counts",
)
@click.option(
    "-m",
    "--characters",
    "count_characters",
    is_flag=True,
    help="print the character counts",
)
def app(files, count_bytes, count_lines, count_words, count_characters):
    for file in files:
        result = ""
        lines, words, bytes_, chars = count(file)
        if not (count_bytes or count_lines or count_words or count_characters):
            result = f"{lines}\t{words}\t{bytes_}\t{chars}"
        else:
            if count_lines:
                result += f"{lines}\t"
            if count_words:
                result += f"{words}\t"
            if count_bytes:
                result += f"{bytes_}\t"
            if count_characters:
                result += f"{chars}"

        click.echo(result)


if __name__ == "__main__":
    app()
