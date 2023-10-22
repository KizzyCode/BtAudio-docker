import os
import subprocess
import sys

if __name__ == "__main__":
    # Set address
    print(f"{ os.environ }")
    address = os.environ.get("BT_MAC_ADDRESS")
    if address is not None:
        # Parse and reverse MAC address
        address_hex = address.split(":")
        address_hex = reversed(address_hex)

        # Run subprocess
        print(f"*> Changing bluetooth device address to { address }...")
        subprocess.run(["hcitool", "cmd", "0x3f", "0x001", *address_hex], check=True)
    
    # Become supervisord
    print(f"*> Starting supervisord...")
    sys.stdout.flush()
    os.execl("/usr/bin/supervisord", "/usr/bin/supervisord", "-c", "/etc/supervisord.conf")
