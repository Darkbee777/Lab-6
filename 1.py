import platform

def can_run():
    system = platform.system()
    architecture = platform.architecture()
    machine = platform.machine()
    return (system == 'Windows' or system == 'Linux') and architecture == '64bit' and machine == 'AMD64'
