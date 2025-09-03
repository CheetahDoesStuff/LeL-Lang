import lellang.globals as g

def get_raw() -> str:

    path = g.file_path

    with open(path, "r") as f:
        return f.read()