def output_to_console(data):
    """Outputs text to the console"""
    print(data)

def write_to_file_builtin(file_path, data):
    """Writes data to a file using built-in tools"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)