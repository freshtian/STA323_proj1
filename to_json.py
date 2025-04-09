import pandas as pd
import json

#
with open('dns_merged.txt', 'r', encoding='utf-8') as file:
    df = pd.DataFrame(json.loads(line) for line in file if line.strip())

df.to_csv('dns_merged.csv', index=False)

with open('http_merged.txt', 'r', encoding='utf-8') as file:
    df = pd.DataFrame(json.loads(line) for line in file if line.strip())
df.to_csv('http_merged.csv', index=False)

with open('test.txt', 'r', encoding='utf-8') as file:
    df = pd.DataFrame(json.loads(line) for line in file if line.strip())

df.to_csv('test.csv', index=False)