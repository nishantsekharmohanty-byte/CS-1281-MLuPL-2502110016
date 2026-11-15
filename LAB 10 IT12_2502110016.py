IT12: Rough cut - Fix Yesterday's Gaps
Alternative approach using modern pathlib and sys.exit() for cleaner error handling.   Relative Paths (pathlib):Pythonfrom pathlib import Path
import sys

# Dynamically resolve the path relative to this script's location
current_dir = Path(__file__).parent
target_file = current_dir.parent / 'data' / 'input_data.csv'
Targeted Exception Handling:Pythontry:
    data = target_file.read_text()
except FileNotFoundError:
    # Replaces tracebacks with a clean, user-facing exit message
    sys.exit("Error: Could not locate 'input_data.csv' in the data/ directory.")
except PermissionError as e:
    sys.exit(f"Error: Lacking permissions to read the file. Details: {e}")
# No bare 'except:' used anywhere
