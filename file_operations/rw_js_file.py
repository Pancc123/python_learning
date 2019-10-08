import json


def read_json_file(file_name):
    with open(file_name) as f_obj:
        number = json.load(f_obj)
        print(number)


def write_json_file(data, file_name):
    with open(file_name, 'w') as file_object:
        json.dump(data, file_object)


if __name__ == '__main__':
    filename = 'number.json'
    numbers = [2, 3, 4, 5, 6, 7, 9]
    read_json_file(filename)
    write_json_file(numbers, filename)