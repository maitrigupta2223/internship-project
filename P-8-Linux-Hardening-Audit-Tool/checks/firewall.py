import subprocess

def check_firewall():
    try:
        output = subprocess.getoutput("ufw status")

        if "active" in output:
            return True, "Firewall is active"
        else:
            return False, "Firewall is inactive"
    except:
        return False, "Firewall check failed"
