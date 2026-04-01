import os
import requests
import json

# Fetch leaked prompts
response = requests.get('https://api.github.com/repos/jujumilk3/leaked-system-prompts/contents/')
files = response.json()

missing = []
for file in files:
    if file['name'].endswith('.md') and file['name'] != 'README.md':
        missing.append(file['name'])

print(f"Found {len(missing)} possible files")
for i, name in enumerate(missing[:15]):
    print(f"{i+1}. {name}")
