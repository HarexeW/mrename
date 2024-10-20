import re

patterns = [
    {
        'pattern': r".*?S(\d+)\s*E(\d+)\.([a-zA-Z0-9]+).*",
        'has_season': True
    },  #S*E*.*
    {
        'pattern': r".*?S(\d+)\s*x\s*E(\d+)\.([a-zA-Z0-9]+).*",
        'has_season': True
    },  #S*xE*.*
    {
        'pattern': r".*?S(\d+)\s*-\s*E(\d+)\.([a-zA-Z0-9]+).*",
        'has_season': True
    },  #S*-E*.*
    {
        'pattern': r".*?(\d+)x(\d+)\.([a-zA-Z0-9]+).*",
        'has_season': True
    },  #*x*.*
    {
        'pattern': r".*[Ee](\d+)(?=\.[a-zA-Z0-9]+$)",
        'has_season': False
    },  #E*.*
    {
        'pattern': r".*?(\d+)(?=\.[a-zA-Z0-9]+$)",
        'has_season': False
    }  #*.*
]

def get_pattern(filename: str):

    for pattern in patterns:
        if re.match(pattern['pattern'], filename):
            return pattern

    return None

