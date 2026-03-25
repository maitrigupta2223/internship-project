import subprocess

def check_rootkit():

    output = subprocess.getoutput("ps aux")

    if "nc -l" in output or "netcat" in output:
        return False, "Suspicious process detected"

    return True, "No rootkit indicators"
