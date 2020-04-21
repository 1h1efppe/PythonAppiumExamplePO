import subprocess


# Shell command runner (for ADB mostly)
class ShellRunner:
    @staticmethod
    def run_command(command):
        subprocess.call(command, shell=True)
