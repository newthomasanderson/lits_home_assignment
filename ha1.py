#!/usr/bin/env python


import os
import subprocess


def _get_command_output(command):
    """

    :param command: shell CLI command
    :return: shell command execution result
    """
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        std_out, std_err = process.communicate()
        return std_out
    except (OSError, ValueError) as e:
        print(e)


def get_folder_listing(folders_path):
    """

    :param folders_path: string with path value of desirable directory to list
    :return: list of folders objects
    """
    command = ['ls -l {}'.format(folders_path)]
    return _get_command_output(command).split('\n')[:-1]


def process_all(dir_name):
    """

    :param dir_name: string with path value of desirable directory to list
    :return: dict with recursive listing of each directory starting from dir_name
    """

    if dir_name is None:
        dir_name = _get_command_output('pwd').split('\n')[:-1][0]

    # handling spaces in path
    if ' ' in dir_name:
        dir_name = dir_name.replace(' ', '\ ')
    output = dict()
    # Avoid case when folder contains only files
    output[dir_name] = get_folder_listing(dir_name)
    # Getting recursive all folders paths from top folder 'dir_name'
    try:
        list_of_pathes = [[os.path.join(root, name) for name in dirs] for root, dirs, files in
                          os.walk('{}'.format(dir_name), topdown=True)]
        # Get plain list of folder's pathes from folded/nested lists
        list_dirs = [e for el in list_of_pathes if el for e in el]

    except (OSError, ValueError) as e:
        print(e)
    # Get content listing for each folder
    for el in list_dirs:
        if el not in output.keys():
            if ' ' in el:
                el = el.replace(' ', '\ ')
            output[el] = get_folder_listing(el)

    return output


def main(path=None):

    print(process_all(path))


if __name__ == '__main__':
    main()
