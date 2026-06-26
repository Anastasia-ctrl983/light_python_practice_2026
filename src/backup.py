import os

def compare_with_backup(source_files, backup_files):
    # Сравнивает исходную папку с бэкапом по имени файла и хэшу ---
    # Создаем словари: имя файла - информация
    source_by_name = {}
    for info in source_files:
        name = os.path.basename(info['path'])
        source_by_name[name] = info
    
    backup_by_name = {}
    for info in backup_files:
        name = os.path.basename(info['path'])
        backup_by_name[name] = info
    
    source_names = set(source_by_name.keys())
    backup_names = set(backup_by_name.keys())
    
    missing = []
    extra = []
    modified = []
    same = []
    
    for name in source_names:
        if name not in backup_names:
            missing.append(name)
        else:
            source_hash = source_by_name[name].get('hash')
            backup_hash = backup_by_name[name].get('hash')
            
            if source_hash and backup_hash and source_hash == backup_hash:
                same.append(name)
            else:
                modified.append(name)
    
    for name in backup_names:
        if name not in source_names:
            extra.append(name)
    
    return {
        'missing': missing,
        'extra': extra,
        'modified': modified,
        'same': same
    }

def print_comparison_report(comparison_result):
    print()
    print("-" * 60)
    print("СРАВНЕНИЕ С РЕЗЕРВНОЙ КОПИЕЙ:")
    
    if comparison_result['missing']:
        print(f"\n Отсутствуют в бэкапе (есть в исходной): {len(comparison_result['missing'])}")
        for name in comparison_result['missing']:
            print(f"  - {name}")
    else:
        print("\n Все файлы присутствуют в бэкапе")
    
    if comparison_result['extra']:
        print(f"\n Лишние в бэкапе (нет в исходной): {len(comparison_result['extra'])}")
        for name in comparison_result['extra']:
            print(f"  - {name}")
    else:
        print("\n В бэкапе нет лишних файлов")
    
    if comparison_result['modified']:
        print(f"\n Изменённые файлы: {len(comparison_result['modified'])}")
        for name in comparison_result['modified']:
            print(f"  - {name}")
    else:
        print("\n Все общие файлы совпадают")
    
    print(f"\n Совпадают: {len(comparison_result['same'])} файлов")
    
    print("-" * 60)
