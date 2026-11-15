IT10: Standard - README & Tidy
Alternative approach using Windows PowerShell commands and a more concise README layout.   Repository Tidy (Windows PowerShell):PowerShell# Create the required workshop directories
New-Item -ItemType Directory -Force -Path src, data, reports

# Organize files into the sensible layout
Move-Item -Path *.py -Destination src\
Move-Item -Path sample.csv -Destination data\

# Remove unused files
Remove-Item -Path old_test.py
README.md Alternative Format:Markdown# [Project Name]
> [Insert your one-sentence problem description here]

### How to Run
1. Drop your input dataset into the `data/` folder.
2. Run the application: `python src/main.py`
3. View the generated results inside `reports/`.
