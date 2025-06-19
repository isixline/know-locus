from core.matcher import match_in_files
from config.env import get_know_lib_path


def match_in_know_lib(query, file_filter, top):
    know_lib_path = get_know_lib_path()
    return match_in_files(query, know_lib_path, file_filter, top)
