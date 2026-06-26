import os
import datetime
from hash_utils import calculate_hash

def scan_folder(folder_path, extension=None):
    # Рекурсивно сканирует папку и собирает информацию о файлах ----
    files_info = []
    
    try:
        items = os.listdir(folder_path)
    except PermissionError:
        return files_info
    
    for item in items:
        full_path = os.path.join(folder_path, item)
        
        if os.path.isdir(full_path): # папка?
            sub_files = scan_folder(full_path, extension) # рекурсия
            files_info.extend(sub_files)
        else:
            if extension:
                if not full_path.lower().endswith(extension.lower()):
                    continue
            
            try:
                stat = os.stat(full_path)
                file_hash = calculate_hash(full_path)
                
                files_info.append({
                    'path': full_path,
                    'size': stat.st_size,
                    'modified': datetime.datetime.fromtimestamp(stat.st_mtime),
                    'hash': file_hash
                })
            except (OSError, PermissionError):
                continue
    
    return files_info
