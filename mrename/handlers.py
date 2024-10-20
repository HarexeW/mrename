import re
from mrename.exceptions import MatchNotFoundError

from mrename.functions import rename_file

def rename_se(file):
    pattern = r"S(\d+)\s*E(\d+)\.[a-zA-Z0-9]+"
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Season and Episode Number not found.")

    return rename_file(
        file,
        int(match.group(1)),
        int(match.group(2)),
    )

def rename_sxe(file):
    pattern = r"S(\d+)\s*x\s*E(\d+)\.[a-zA-Z0-9]+"
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Season and Episode Number not found.")

    return rename_file(
        file,
        int(match.group(1)),
        int(match.group(2)),
    )

def rename_sde(file):
    pattern = r"S(\d+)\s*-\s*E(\d+)\.[a-zA-Z0-9]+"
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Season and Episode Number not found.")

    return rename_file(
        file,
        int(match.group(1)),
        int(match.group(2)),
    )

def rename_x(file):
    pattern = r"(\d+)\s*x\s*(\d+)\.[a-zA-Z0-9]+"
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Season and Episode Number not found.")

    return rename_file(
        file,
        int(match.group(1)),
        int(match.group(2)),
    )

def rename_e(file):
    pattern = r"[Ee](\d+)(?=\.[a-zA-Z0-9]+$)"
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Episode Number not found.")

    return rename_file(
        file,
        None,
        int(match.group(1)),
    )

def rename_num(file):
    pattern = r"(\d+)(?=\.[a-zA-Z0-9]+$)"
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Episode Number not found.")

    return rename_file(
        file,
        None,
        int(match.group(1)),
    )