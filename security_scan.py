import random

def run_scan():
    print("Running security scan...")

    # Simulate detection
    vulnerability_detected = random.choice([True, False])

    if vulnerability_detected:
        print("CRITICAL: Hardcoded password found!")
        return True
    else:
        print("No vulnerabilities found.")
        return False

if __name__ == "__main__":
    run_scan()