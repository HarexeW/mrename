import re
from mrename.exceptions import MatchNotFoundError

from mrename.functions import rename_file

def handle_rename(pattern, file, has_season):
    print(pattern)
    print(file)
    match = re.search(pattern, file)
    if match is None:
        raise MatchNotFoundError("Season and Episode Number not found.")

    if has_season:
        return rename_file(
            file,
            int(match.group(1)),
            int(match.group(2)),
            match.group(3)
        )
    else:
        return rename_file(
            file,
            None,
            int(match.group(1)),
            match.group(2)
        )