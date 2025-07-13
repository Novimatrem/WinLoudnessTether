import subprocess
import urllib.request
import os
import zipfile
import time

# 📦 NirCmd setup
NIRCMD_URL = "https://www.nirsoft.net/utils/nircmd.zip"
INSTALL_DIR = os.path.join(os.getenv("APPDATA"), "NirCmd")
EXE_PATH = os.path.join(INSTALL_DIR, "nircmd.exe")
ZIP_PATH = os.path.join(INSTALL_DIR, "nircmd.zip")

# 🎚 Target volume: 64% = 41942
TARGET_VOLUME = 41942
FORCE_INTERVAL_SEC = 1

def download_nircmd():
    print("[SETUP] Downloading NirCmd...")
    os.makedirs(INSTALL_DIR, exist_ok=True)
    urllib.request.urlretrieve(NIRCMD_URL, ZIP_PATH)
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(INSTALL_DIR)
    os.remove(ZIP_PATH)
    print("[INFO] NirCmd setup complete.")

def ensure_nircmd():
    if not os.path.exists(EXE_PATH):
        try:
            download_nircmd()
        except Exception as e:
            print("[ERROR] NirCmd download failed:", e)
            exit(1)

def enforce_volume(level):
    subprocess.call(
        f'"{EXE_PATH}" setsysvolume {level}',
        shell=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

# 🌀 Start tether
print("[DAEMON] Hard Volume Tether Starting...")
ensure_nircmd()
print(f"[INFO] Force-setting system volume to {int(TARGET_VOLUME / 65535 * 100)}% every {FORCE_INTERVAL_SEC} second(s)")

while True:
    try:
        enforce_volume(TARGET_VOLUME)
        print("[FORCE] Volume enforced.")
        time.sleep(FORCE_INTERVAL_SEC)
    except Exception as e:
        print("[ERROR] Runtime failure:", e)
        time.sleep(1)
