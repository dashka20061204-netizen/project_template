from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin


def main():
    """Console input and output"""
    text_console = input_from_console()
    output_to_console(f"З консолі: {text_console}")

    file_path = "data/input_data.txt"
    text_builtin = read_from_file_builtin(file_path)
    output_to_console(f"З файлу (Python): {text_builtin}")

    text_pandas = read_from_file_pandas(file_path)
    output_to_console(f"З файлу (Pandas): {text_pandas}")

    final_output = f"Консоль: {text_console}\nPython: {text_builtin}\nPandas: {text_pandas}"
    write_to_file_builtin("data/results.txt", final_output)

if __name__ == "__main__":
    main()