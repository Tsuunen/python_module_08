import sys
import os
import site

if (__name__ == "__main__"):
    is_venv = sys.prefix != sys.base_prefix
    print("\nMATRIX STATUS: ", end="")
    if (is_venv):
        print("Welcome to the construct\n")
    else:
        print("You're still plugged in\n")
    print("Current Python:", sys.executable)  # python executable path
    print("Virtual Environment: ", end="")
    if (is_venv):
        print(os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("\nThen run this program again.")
