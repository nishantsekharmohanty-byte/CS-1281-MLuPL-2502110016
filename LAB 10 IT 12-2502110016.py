import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

INPUT_FILE = os.path.join(DATA_DIR, "shift_log.txt")
REPORT_FILE = os.path.join(DATA_DIR, "report.txt")
REJECTS_FILE = os.path.join(DATA_DIR, "rejects.csv")
