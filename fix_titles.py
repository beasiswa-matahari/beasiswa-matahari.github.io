import re
import os
import glob

exceptions = {"yang", "di", "ke", "dari", "dan", "atau", "untuk", "pada", "dalam", "dengan", "sebagai", "tentang", "v2"}

def title_case(text):
    return text

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    def replacer(match):
        start_tag = match.group(1)
        inner_html = match.group(2)
        end_tag = match.group(3)
        
        parts = re.split(r'(<[^>]+>)', inner_html)
        first_word = True
        for i in range(0, len(parts), 2):
            tokens = re.split(r'(\s+)', parts[i])
            for j, token in enumerate(tokens):
                if token.strip():
                    if first_word:
                        tokens[j] = token.capitalize()
                        first_word = False
                    elif token.lower() in exceptions:
                        tokens[j] = token.lower()
                    else:
                        tokens[j] = token.capitalize()
            parts[i] = "".join(tokens)
            
        return start_tag + "".join(parts) + end_tag
        
    pattern = re.compile(r'(<h[1-6][^>]*>|<[^>]+class="[^"]*\beyebrow\b[^"]*"[^>]*>)(.*?)(</h[1-6]>|</[a-zA-Z0-9]+>)', re.IGNORECASE | re.DOTALL)
    
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")
