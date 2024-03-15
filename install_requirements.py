# install_requirements.py

import subprocess

def install_requirements():
    try:
        from requirements import modules
    except ImportError:
        print("Error: Could not import 'requirements' module.")
        return
    
    for module in modules:
        subprocess.run(['pip', 'install', module])

if __name__ == "__main__":
    install_requirements()
