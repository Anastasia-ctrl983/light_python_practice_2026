def find_duplicates(files_info):
    # Находит дубликаты по хэшу ---------
    hash_groups = {}
    
    for file_info in files_info:
        file_hash = file_info.get('hash')
        if file_hash is None:
            continue
        
        if file_hash not in hash_groups:
            hash_groups[file_hash] = []
        hash_groups[file_hash].append(file_info['path'])
    
    duplicates = {h: paths for h, paths in hash_groups.items() if len(paths) > 1}
    return duplicates
