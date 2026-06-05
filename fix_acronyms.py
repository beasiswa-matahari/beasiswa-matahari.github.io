import re
import os
import glob

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = re.sub(r'\bItb\b', 'ITB', content)
    content = re.sub(r'\bFaq\b', 'FAQ', content)
    content = re.sub(r'\bTa\b', 'TA', content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
