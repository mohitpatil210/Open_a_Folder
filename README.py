import os

def list_files_recursive(folder_path, level=0):
    try:
        items = os.listdir(folder_path)        
        indent = "  " * level

        for item in items:
            full_path = os.path.join(folder_path, item)
            if os.path.isfile(full_path):
                print(f"{indent}f {item}") 
            elif os.path.isdir(full_path):
                print(f"{indent}fd {item}/")
                list_files_recursive(full_path, level + 1)                
    except PermissionError:
        print(f"{indent} Permission denied: {folder_path}")
    except Exception as e:
        print(f"{indent} Error: {e}")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ")    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(f"\nRecursive listing of '{folder_path}':")
        print("=" * 50)
        list_files_recursive(folder_path)
    else:
        print("Folder not found or not a directory!")
