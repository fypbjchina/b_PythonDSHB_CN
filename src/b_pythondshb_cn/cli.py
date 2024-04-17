"""Console script for b_pythondshb_cn."""
import b_pythondshb_cn

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for b_pythondshb_cn."""
    console.print("Replace this message by putting your code into "
               "b_pythondshb_cn.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
