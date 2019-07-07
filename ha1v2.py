#!/usr/bin/env python


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
    output = {}
    # Getting recursive all folders paths from top folder 'dir_name' and their output
    accum_path = {}
    accum_path[dir_name] = ''
    while accum_path != {}:
        for path in list(accum_path):
            if path not in output:
                output[path] = get_folder_listing(path)
                accum_path.pop(path)
                dir_list = [el.split(' ')[-1] for el in output[path] if el[0] == 'd']
                for p in dir_list:
                    if ' ' in p:
                        p = p.replace(' ', '\ ')
                    p = '{}/{}'.format(path, p)
                    accum_path[p] = ''
            else:
                accum_path.pop(path)

    return output


def main(path=None):

    print(process_all(path))


if __name__ == '__main__':
    main()
