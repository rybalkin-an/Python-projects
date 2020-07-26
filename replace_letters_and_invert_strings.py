import sys
import os.path


def get_config(i_file_name):
    """Read data from config"""
    try:
        l_config = {}
        for config_line in open(i_file_name).read().split('\n'):
            if config_line:
                key, value = config_line.split('=')
                l_config[key] = value
        return l_config if len(l_config) > 0 else print("Config file is empty!")
    except Exception:
        raise Exception("Config file reading error has been occurred!")


def read_text_file(i_file_name):
    """Get text from txt file"""
    try:
        l_txt_file = open(f'{i_file_name}').read()
        return l_txt_file if l_txt_file else print("Input file is empty!")
    except Exception:
        raise Exception("Text file reading error has been occurred!")


def proceed_data(i_config, i_text_file):
    """Replace line order from the end to the beginning and replace the characters in the text file"""
    for l_let, l_val in i_config.items():
        i_text_file = i_text_file.replace(l_let, l_val)
    return '\n'.join(reversed(i_text_file.split('\n')))


def write_text_file(i_file_name, i_str):
    """Write result into the text file"""
    try:
        with open(f'{i_file_name}', 'w') as l_txt_file:
            l_txt_file.write(i_str)
            l_txt_file.close()
        return print("Result has been saved!")
    except Exception:
        raise Exception("Text file writing error has been occurred!")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        config = get_config(sys.argv[1]) if os.path.exists(sys.argv[1]) else print("Config file doesn't exist!")
        text_file = read_text_file(sys.argv[2]) if os.path.exists(sys.argv[2]) else print("Text file doesn't exist!")
        if config and text_file:
            text_file = proceed_data(config, text_file)
            write_text_file(sys.argv[2], text_file)
    else:
        raise Exception("Text file writing error has been occurred!")
