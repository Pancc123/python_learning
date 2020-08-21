import json,os


def read_json_file(file_name):
    with open(file_name) as f_obj:
        number = json.load(f_obj)
        print(number)


def write_json_file(data, file_name):
    with open(file_name, 'w') as file_object:
        json.dump(data, file_object)


if __name__ == '__main__':
    file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(file_path1, r'test_files\number.json')
    numbers = [2, 3, 4, 5, 6, 7, 9]
    read_json_file(file_path)
    # write_json_file(numbers, file_path)