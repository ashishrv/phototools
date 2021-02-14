

import subprocess


def execute_cmd(cmd, shell=True):
    #print(cmd)
    proc = subprocess.Popen(cmd,
                            shell=shell,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout_value, stderr_value = proc.communicate()
    print(stdout_value.decode('utf-8'))
    print("\n")
    print(stderr_value.decode('utf-8'))


def get_cmd_otput(cmd, shell=True):
    #print(cmd)
    proc = subprocess.Popen(cmd,
                            shell=shell,
                            stdout=subprocess.PIPE)
    stdout_value, stderr_value = proc.communicate()
    return stdout_value.decode('utf-8').rstrip('\n')
