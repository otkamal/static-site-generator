import os
import shutil

def copy_static(src: str, dest: str) -> None:
    clear_destination(dest)
    recursive_copy(src, dest)

def clear_destination(dest: str) -> None:
    for path in os.listdir(dest):
        file_path = os.path.join(dest, path)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except RuntimeError as e:
            print(f"failed to delete {file_path}. {e}")

def recursive_copy(src: str, dest: str) -> None:
    for path in os.listdir(src):
        old_path = os.path.join(src, path)
        new_path = os.path.join(dest, path)
        if os.path.isfile(old_path):
            print(f"copy {old_path} to {new_path}")
            shutil.copy(old_path, new_path)
        else:
            os.mkdir(new_path)
            recursive_copy(old_path, new_path)