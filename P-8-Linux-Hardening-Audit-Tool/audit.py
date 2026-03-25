from checks.firewall import check_firewall
from checks.ssh import check_ssh
from checks.permissions import check_permissions
from checks.services import check_services
from checks.rootkit import check_rootkit
from report import generate_report

def run_audit(gui_mode=False):

    results = {}

    results["Firewall"] = check_firewall()
    results["SSH"] = check_ssh()
    results["Permissions"] = check_permissions()
    results["Services"] = check_services()
    results["Rootkit"] = check_rootkit()

    score = int(sum(1 for r in results.values() if r[0]) / len(results) * 100)

    generate_report(results, score)

    if not gui_mode:
        print("\nAudit Results:\n")

        for k,v in results.items():
            print(f"{k}: {'PASS' if v[0] else 'FAIL'} - {v[1]}")

        print(f"\nSecurity Score: {score}%")

    return results, score


if __name__ == "__main__":
    run_audit()
