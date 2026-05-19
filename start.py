import os
import sys
import subprocess
import time
import threading

# Install required packages using subprocess (safer than os.system)
def install_required_packages():
    """Install missing packages safely."""
    try:
        import requests
    except ModuleNotFoundError:
        print("Installing requests...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])

def run_bootstrap_script():
    """Run the bootstrap script with error handling."""
    script_path = 'r00t.sh'
    
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found")
        return False
    
    try:
        result = subprocess.run(['bash', script_path], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        return False
    except FileNotFoundError:
        print("Error: bash not found")
        return False

if __name__ == '__main__':
    install_required_packages()
    run_bootstrap_script()
