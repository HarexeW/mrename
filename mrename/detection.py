import re
import mrename.handlers as handler

patterns = {
    r".*?S(\d+)\s*E(\d+)\.[a-zA-Z0-9]+.*": handler.rename_se, #S*E*.*
    r".*?S(\d+)\s*x\s*E(\d+)\.[a-zA-Z0-9]+.*": handler.rename_sxe, #S*xE*.*
    r".*?S(\d+)\s*-\s*E(\d+)\.[a-zA-Z0-9]+.*": handler.rename_sde, #S*-E*.*
    r".*?(\d+)x(\d+)\.[a-zA-Z0-9]+.*": handler.rename_x, #*x*.*
    r".*[Ee](\d+)(?=\.[a-zA-Z0-9]+$)": handler.rename_e, #E*
    r".*?(\d+)(?=\.[a-zA-Z0-9]+$)": handler.rename_num #*
}

def get_handler(filename: str):
    for pattern in patterns.keys():
        if re.match(pattern, filename):
            return patterns[pattern]

    return None

