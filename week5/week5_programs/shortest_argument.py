import sys

def find_shortest_argument():
    arguments = sys.argv[1:]
    if not arguments:
        print("No arguments provided.")
        return
    shortest_argument = min(arguments, key=len)
    print(f"The shortest argument is: {shortest_argument}")
if __name__ == "__main__":
    find_shortest_argument()
