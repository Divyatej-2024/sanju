import pexpect
import sys

# Change this to the full path of airgeddon.sh
script_path = '/path/to/airgeddon/airgeddon.sh'

# Spawn Airgeddon
child = pexpect.spawn(f'bash {script_path}', encoding='utf-8', timeout=None)

# Optional: Log output to the terminal (useful for debugging)
child.logfile = sys.stdout

# Let it run for a bit or wait for specific output
try:
    # Wait for a specific menu prompt or keyword Airgeddon shows
    child.expect(['Select an option', 'Choose your network interface', pexpect.EOF, pexpect.TIMEOUT])
except pexpect.exceptions.ExceptionPexpect as e:
    print("Error:", e)

# Interact manually if needed
# child.sendline('1')  # Example of selecting the first menu option
