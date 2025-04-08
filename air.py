import pexpect
import sys
import os
 
airgeddon_path = '/home/kali/airgeddon/airgeddon.sh'  # Change to your path
 
if not os.path.isfile(airgeddon_path):
    print("Airgeddon script not found!")
    sys.exit(1)
 
if not os.access(airgeddon_path, os.X_OK):
    os.chmod(airgeddon_path, 0o755)
 
child = pexpect.spawn(f'bash {airgeddon_path}', encoding='utf-8', timeout=None)
child.logfile = sys.stdout
 
try:
    child.expect(["Choose your wireless interface", "Select your interface", pexpect.EOF, pexpect.TIMEOUT])
    child.sendline('2')  # Select first interface
    
    child.expect(["Monitor mode enabled", "Press any key", pexpect.EOF, pexpect.TIMEOUT])
    child.sendline('')  # Press Enter to continue
 
except pexpect.exceptions.ExceptionPexpect as e:
    print("Interaction failed:", e)
