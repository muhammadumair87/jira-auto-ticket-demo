import sys
import random

def run_scan():
    vulnerability_detected = random.choice([True, False])

    if vulnerability_detected:
        print("CRITICAL: Vulnerability detected!")
        sys.exit(1)  # Fails pipeline
    else:
        print("Scan clean.")
        sys.exit(0)

if __name__ == "__main__":
    run_scan()
