import sys

import click
from rich import print, text, align
import os

from mrename.functions import process_folder


@click.command()
@click.option('--y', default=False, is_flag=True)
def cli(y):
    app_title = text.Text("mRename", style="bold magenta")
    app_title = align.Align.center(app_title)
    print(app_title)

    app_version = text.Text("Version 0.0.1", style="italic magenta")
    app_version = align.Align.center(app_version)
    print(app_version)
    click.echo('')

    current_dir = os.path.basename(os.path.normpath(os.getcwd()))
    folder_text = text.Text(f"Current folder: {current_dir}")
    print(folder_text)
    click.echo('')

    if not y:
        if click.prompt("Do you want to rename all files? (y/n)").lower() != "y":
            folder_text = text.Text(f"Aborting...", style="bold red")
            print(folder_text)
            sys.exit()

    correct, errors = process_folder()

    stats = text.Text()
    stats.append(f"Renamed {correct} files. ")
    stats.append(f"{errors} errors.", style="red bold")
    print(stats)

cli()