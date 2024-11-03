import csv
from pathlib import Path



def compute_difference(file1_path: Path, file2_path: Path):
    """Calculate the difference between two CSV files containing email lists"""
    # Read first file
    emails1 = set()
    with open(file1_path, 'r') as f1:
        reader = csv.DictReader(f1)
        for row in reader:
            emails1.add(row['Member Email'])
    
    # Read second file
    emails2 = set()
    with open(file2_path, 'r') as f2:
        reader = csv.DictReader(f2)
        for row in reader:
            emails2.add(row['Member Email'])
    
    # Calculate difference (emails in file1 but not in file2)
    diff = emails1 - emails2
    
    # Print results
    print(f"Emails in {file1_path} but not in {file2_path}:")
    for email in sorted(diff):
        print(email)

    return diff

def difference(file1_path: Path, file2_path: Path, output_path: Path, group_mail: str):
    """Calculate the difference between two CSV files containing email lists and create a new CSV file with the difference"""
    diff = compute_difference(file1_path, file2_path)

    # Write the difference to a new CSV file
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Member Email'])
        writer.writeheader()
        for email in sorted(diff):
            writer.writerow({'Member Email': email})

