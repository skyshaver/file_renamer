import random
import os
from glob import glob
from shutil import copy

class RandomWordGen:
    lines = []    
    def init(self) -> str:        
        with open("female.names", 'r') as fin:
            self.lines = [line.rstrip() for line in fin]

    def get_random_word(self) -> str:        
        random_int = random.randint(0, len(self.lines) - 1)        
        return self.lines[random_int]


def make_random_files_in_dir(path_to_dir: str, file_prefix: str, num_files: int):
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)

    rando = RandomWordGen()
    rando.init()
    for i in range(num_files):
        with open(f"{path_to_dir}/{file_prefix}_{i}.txt", 'w+') as fin:
            for i in range(random.randint(10, 30)):
                fin.write(f"{rando.get_random_word()}\n")

def copy_folder_and_rename_files(src: str, dest: str, dest_prefix: str):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for idx, f in enumerate(glob(f"{src}/*")):
        copy(f, f"{dest}/{dest_prefix}_{idx}.txt")

if __name__ == "__main__":
    make_random_files_in_dir("source", "src", 10)
    # for idx, f in enumerate(glob("./source/*")):
    #     print(f"{f} {idx}")
    copy_folder_and_rename_files(src="source", dest="destination", dest_prefix="dest")