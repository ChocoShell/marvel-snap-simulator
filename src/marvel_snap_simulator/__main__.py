"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Marvel Snap Simulator."""


if __name__ == "__main__":
    main(prog_name="marvel-snap-simulator")  # pragma: no cover
