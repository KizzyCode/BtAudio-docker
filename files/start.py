import os
import subprocess
import sys

if __name__ == "__main__":
    # Set address
    if "ADDRESS" in os.environ:
        # Get the vars
        address = os.environ["ADDRESS"]
        device = os.environ["DEVICE"]

        # Parse and reverse MAC address
        address_hex = address.split(":")
        address_hex = reversed(address_hex)
        address_hex = map(lambda hex: f"0x{ hex }", address_hex)

        # Run subprocess
        print(f"*> Changing bluetooth device address to { address }...")
        subprocess.run(["hcitool", "-i", device, "cmd", "0x3f", "0x001", *address_hex], check=True)
        subprocess.run(["hciconfig", device, "reset"], check=True)
    
    # Become supervisord
    print(f"*> Starting supervisord...")
    sys.stdout.flush()
    os.execlp("supervisord", "/usr/bin/supervisord", "-c", "/etc/supervisord.conf")
