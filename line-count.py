import os

total_lines = 0

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        for l in lines :
            if l.replace(' ','') == '\n' or l.replace(' ','') == '':
                lines.pop(lines.index(l)) 
        return len(lines)

def traverse_directory(directory):
    global total_lines
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')  # Exclude the node_modules directory
        for file in files:
            file_path = os.path.join(root, file)
            total_lines += count_lines_in_file(file_path)

project_root = r'F:\bitleonex-backend'  # Update with your project's root directory
traverse_directory(project_root)

print(f'Total lines in the project: {total_lines}')
