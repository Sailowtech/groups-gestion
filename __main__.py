import sys
import argparse
from groups_gestion.difference import difference

def main():
    # Parse arguments: command, file1, file2
    parser = argparse.ArgumentParser(description='Process CSV files containing email lists.')
    parser.add_argument('operation', type=str, help='Operation to perform (currently only "difference" is supported)')
    parser.add_argument('file1', type=str, help='Path to first CSV file')
    parser.add_argument('file2', type=str, help='Path to second CSV file')
    
    args = parser.parse_args()
    
    # Execute the operation. We only support difference for now.
    if args.operation.lower() == "difference":
        # TODO
    else:
        print(f"Unsupported operation: {args.operation}")
        sys.exit(1)

if __name__ == "__main__":
    main()

