import subprocess

def check_services():

    output = subprocess.getoutput("systemctl list-units --type=service")

    risky = ["telnet", "ftp"]

    for r in risky:
        if r in output:
            return False, f"Risky service running: {r}"

    return True, "No risky services detected"
