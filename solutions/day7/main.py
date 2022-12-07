from __future__ import annotations

import dataclasses
from typing import Callable, List, Optional


@dataclasses.dataclass
class File:
    size: int


@dataclasses.dataclass
class Dir:
    parent: Optional['Dir']
    children: dict[str, 'Dir' | File]

    @property
    def size(self):
        return sum([child.size for child in self.children.values()])


def get_example_input():
    s = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    return s.splitlines()


def get_input():
    with open('solutions/day7/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def flatten_all_child_dirs(top_directory: Dir):
    child_dirs = [child for child in top_directory.children.values() if type(child) == Dir]
    dirs = []
    for directory in child_dirs:
        dirs += flatten_all_child_dirs(directory)
    return child_dirs + dirs


def get_dirs_for_criterion(top_directory: Dir, criterion: Callable[[Dir], bool]):

    def check_below_dirs(top: Dir) -> List[Dir]:
        dirs: List[Dir] = []
        for directory in [child for child in top.children.values() if type(child) == Dir]:
            if criterion(directory):
                dirs += [directory]
            dirs += check_below_dirs(directory)

        return dirs

    return check_below_dirs(top_directory)


def get_dir_tree(input_data: List[str]):
    top = Dir(None, {})
    top.children['/'] = Dir(top, {})

    active_directory = top

    for line in input_data:
        if line == '$ ls':
            continue

        if line == '$ cd ..':
            active_directory = active_directory.parent
            continue

        if line.startswith('$ cd'):
            folder_to_go_to = line.split(' ')[2]
            active_directory = active_directory.children[folder_to_go_to]
            continue

        if line.startswith('dir'):
            dir_name = line.split(' ')[1]
            if dir_name not in active_directory.children.keys():
                active_directory.children[dir_name] = Dir(active_directory, {})
            continue

        size, file_name = line.split(' ')
        active_directory.children[file_name] = File(int(size))

    return top


def task1():
    input_data = get_input()
    top = get_dir_tree(input_data)

    return sum([directory.size for directory in flatten_all_child_dirs(top) if directory.size < 100000])


def task2():
    input_data = get_input()
    top = get_dir_tree(input_data)

    total_size = 70000000
    needed_space = 30000000
    occupied_space = top.size
    free_space = total_size - occupied_space
    space_to_be_cleared = needed_space - free_space

    big_enough_directories = [
        directory for directory in flatten_all_child_dirs(top) if directory.size > space_to_be_cleared
    ]

    return min([directory.size for directory in big_enough_directories])
