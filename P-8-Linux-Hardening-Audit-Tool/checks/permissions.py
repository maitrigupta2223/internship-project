import os

def check_permissions():

    issues = []

    if os.stat("/etc/shadow").st_mode & 0o777 != 0:
        issues.append("/etc/shadow permissions insecure")

    if os.stat("/etc/passwd").st_mode & 0o777 > 0o644:
        issues.append("/etc/passwd permissions too open")

    if issues:
        return False, ", ".join(issues)

    return True, "Permissions secure"
