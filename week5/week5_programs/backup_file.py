import sys
import shutil

def create_backup(file_path):
    try:
        # Create a backup file by adding a suffix
        backup_path = file_path + '.bak'
        
        # Copy the contents of the original file to the backup file
        shutil.copy2(file_path, backup_path)

        print(f"Backup created successfully: {backup_path}")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_file.py <filename>")
    else:
        create_backup(sys.argv[1])
