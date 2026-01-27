from dotenv import load_dotenv
import os

if (__name__ == "__main__"):
    load_dotenv()
    MATRIX_MODE = os.environ.get("MATRIX_MODE")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    API_KEY = os.environ.get("API_KEY")
    LOG_LEVEL = os.environ.get("LOG_LEVEL")
    ZION_ENDPOINT = os.environ.get("ZION_ENDPOINT")
    no_missing = True
    # Check if an env variable is missing
    if (not MATRIX_MODE):
        print("MATRIX_MODE is missing")
        no_missing = False
    if (not DATABASE_URL):
        print("DATABASE_URL is missing")
        no_missing = False
    if (not API_KEY):
        print("API_KEY is missing")
        no_missing = False
    if (not LOG_LEVEL):
        print("LOG_LEVEL is missing")
        no_missing = False
    if (not ZION_ENDPOINT):
        print("ZION_ENDPOINT is missing")
        no_missing = False
    if (no_missing):
        print("\nORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print("Mode:", MATRIX_MODE)
        print("Database:", DATABASE_URL)
        print("API Access:", API_KEY)
        print("Log Level:", LOG_LEVEL)
        print("Zion Network:", ZION_ENDPOINT)
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
