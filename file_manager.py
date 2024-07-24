import pathlib

def file_manager(file_name):
    return pathlib.Path(__file__).parent.resolve()