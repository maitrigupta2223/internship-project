def check_ssh():

    try:
        with open("/etc/ssh/sshd_config") as f:
            data = f.read()

        if "PermitRootLogin no" in data:
            return True, "Root login disabled"
        else:
            return False, "Root login enabled - Disable using 'PermitRootLogin no'"

    except:
        return False, "SSH config not accessible"
