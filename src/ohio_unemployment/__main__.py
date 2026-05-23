"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="ohio-unemployment")
def main() -> None:
    """Ohio Unemployment."""


if __name__ == "__main__":
    app()  # pragma: no cover
