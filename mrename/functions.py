import os
import re
import sys

import click
from rich import print, text, style


def get_season():
    pattern = r"Season\s+(\d+)"

    out = text.Text("Auto detecting season number...", style="italic")
    print(out)

    folder = os.path.basename(os.path.normpath(os.getcwd()))
    match = re.search(pattern, folder, re.IGNORECASE)

    if match is None:
        out = text.Text("Could no autodetect the season number...", style="bold red")
        print(out)
        season = click.prompt("Please enter a season number", type=int)
        if season > 0:
            return season
        else:
            out = text.Text("Invalid Season number entered. Aborting...", style="bold red")
            print(out)
            sys.exit()

    season = int(match.group(1))

    out = text.Text(f"Detected Season {season}", style="bold")
    print(out)

    return season

def rename_file(file, season, episode, file_extension):
    if season is None:
        season = get_season()

    folder_path = os.path.dirname(file)

    new_filename = f"S{str(season).zfill(2)}E{str(episode).zfill(2)}.{file_extension}"
    new_file = os.path.join(folder_path, new_filename)
    old_filename = os.path.basename(file)

    out = text.Text()
    out.append(old_filename, style=style.Style(strike=True))
    out.append(" ")
    out.append(new_filename, style="bold")
    print(out)
    print("")

    os.rename(file, new_file)

def move_file(file, current_folder=None):
    folder = os.getcwd() if current_folder is None else current_folder

    try:
        os.mkdir(folder + "/err")
    except FileExistsError:
        pass

    folder_path = os.path.dirname(file)

    file_name = os.path.basename(file)

    out = text.Text(f"[ERROR] {file_name}", style="bold red")
    print(out)

    new_file = os.path.join(folder_path, "err", file_name)

    os.rename(file, new_file)

def process_folder():
    from mrename.detection import get_pattern
    from mrename.handlers import handle_rename

    folder = os.getcwd()

    correct = 0
    errors = 0

    files = os.listdir(folder)
    for file in files:
        path = os.path.join(folder, file)
        if os.path.isdir(path):
            continue

        pattern = get_pattern(file)
        if pattern is None:
            move_file(path)
            errors = errors + 1
            continue

        handle_rename(
            pattern=pattern['pattern'],
            file=path,
            has_season=pattern['has_season']
        )

        correct = correct + 1

    return correct, errors