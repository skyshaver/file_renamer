from pathlib import Path
import os

def rename_dest_to_source(source: str, dest: str):
    """
    this presumes there are the same number of files in source and dest and that 
    all the files have one that matches it in size, also presumes linux/mac paths
    function iterates source and stores {size : filename} of all files in directory,
    then iterates destination and matches size of file to the source dictionary and uses that 
    to overwrite the name
    will also fail if there are two files of the same size
    """
    source_info = {}
    for path in Path(source).iterdir():
        info = path.stat()
        source_info[info.st_size] = path.name
    
    for path in Path(dest).iterdir():
        info = path.stat()
        os.rename(f"{dest}/{path.name}", f"{dest}/{source_info[info.st_size]}")

if __name__ == "__main__":    
    rename_dest_to_source("source", "dest_test")