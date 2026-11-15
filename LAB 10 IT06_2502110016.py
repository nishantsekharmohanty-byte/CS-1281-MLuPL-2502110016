IT6: Precision - The Handover Pack
Alternative approach using a shell script for the hostile demo and a numbered Limitations list.   Hostile-Input Demo (run_tests.sh):Bash#!/bin/bash
echo "--- Initiating Hostile Input Protocol ---"

echo "[Test A] Supplying a non-existent file path:"
python src/main.py data/ghost_file.csv

echo "[Test B] Supplying a completely empty file:"
touch data/empty_test.csv
python src/main.py data/empty_test.csv
Sample Output: Run your code successfully, pipe the output to a file (python src/main.py > reports/example_report.txt), and commit it to version control so reviewers can see the output format instantly.Limitations Section (Alternative Wording):Markdown## System Limitations
1. **Data Bounds:** Processes a maximum of 50,000 rows efficiently. Larger datasets will cause severe memory bloat.
2. **Resilience:** If a row contains missing fields, the script will drop the entire row rather than attempting to impute values.
3. **Platform:** Tested exclusively on UNIX environments; Windows execu
