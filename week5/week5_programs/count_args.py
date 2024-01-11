import sys

def count_arguments():
    argument_count = len(sys.argv) - 1
    print(f"Number of arguments provided: {argument_count}")
if __name__ == "__main__":
    count_arguments()
