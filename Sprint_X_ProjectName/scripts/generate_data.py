"""Simple data generator script (example)
Run: python scripts/generate_data.py
"""
import csv
import random

def generate_csv(path='data/outputs/sample_data.csv', n=50):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id','value'])
        for i in range(n):
            writer.writerow([i, random.random()])

if __name__ == '__main__':
    generate_csv()
