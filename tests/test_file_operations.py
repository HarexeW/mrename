import os
import random
import re
import shutil
import string

import pytest

from mrename.functions import rename_file, move_file

def random_string(length=10):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(characters) for _ in range(length))


def create_file(work_folder):
    file_path = os.path.join(work_folder, random_string(10))

    f = open(file_path, "w")
    f.close()

    return file_path

@pytest.fixture
def temporary_directory():
    """Creates a Temporary directory to test file operations"""
    temp_dir = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    yield temp_dir  # This is where the test will run

    # Teardown: remove the temporary directory
    shutil.rmtree(temp_dir)


def test_rename_file(temporary_directory):
    file_path = create_file(temporary_directory)
    assert os.path.exists(file_path)

    pattern = r"\.([a-zA-Z0-9]+)$"

    match = re.search(pattern, file_path)

    file_extension = '' if match is None else match.group(1)

    season = random.randint(1, 10)
    episode = random.randint(1, 10)

    rename_file(file_path, season, episode, file_extension)

    new_path = os.path.join(
        os.path.dirname(file_path),
        f"S{str(season).zfill(2)}E{str(episode).zfill(2)}.{file_extension}"
    )
    assert os.path.exists(new_path)


def test_move_file(temporary_directory):
    file_path = create_file(temporary_directory)
    assert os.path.exists(file_path)

    move_file(file_path, current_folder=temporary_directory)
    error_folder = os.path.join(temporary_directory, "err")
    assert os.path.isdir(error_folder)

    file_name = os.path.basename(file_path)
    new_file_path = os.path.join(error_folder, file_name)
    assert os.path.exists(new_file_path)
