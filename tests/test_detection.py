from mrename.detection import get_pattern

patterns = [
    r".*?S(\d+)\s*E(\d+)\.[a-zA-Z0-9]+.*",
    r".*?S(\d+)\s*x\s*E(\d+)\.[a-zA-Z0-9]+.*",
    r".*?S(\d+)\s*-\s*E(\d+)\.[a-zA-Z0-9]+.*",
    r".*?(\d+)x(\d+)\.[a-zA-Z0-9]+.*",
    r".*[Ee](\d+)(?=\.[a-zA-Z0-9]+$)",
    r".*?(\d+)(?=\.[a-zA-Z0-9]+$)"
]



def test_get_pattern_with_good_filenames():
    """This tests the get_pattern function with all correct filenames"""

    filenames = [
        "S1E03.mkv",
        "S1xE01.mkv",
        "S1-E01.mkv",
        "1x01.mkv",
        "E01.mkv",
        "01.mkv"
    ]

    for i in range(len(patterns)):
        pattern = get_pattern(filenames[i])
        assert pattern['pattern'] == patterns[i]

def test_get_pattern_with_wrong_filenames():
    """This tests the get_pattern function with all wrong filenames"""

    filenames = [
        "E.mkv",
        "1E.mkv",
        "S1-E.mkv",
        "S1E01",
        "S1xE01",
        "S1-E01",
        "E01"
    ]

    for i in range(len(patterns)):
        pattern = get_pattern(filenames[i])
        assert pattern is None
