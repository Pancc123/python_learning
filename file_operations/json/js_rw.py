import json,os


def read_jsf(file_name):
    with open(file_name) as f_obj:
        data = json.load(f_obj)
        # print(data)
        return data


def write_to_jsf(data, file_name):
    with open(file_name, 'w') as file_object:
        json.dump(data, file_object)


def add_to_jsf(data, file_name):
    with open(file_name, 'a') as file_object:
        json.dump(data, file_object)


if __name__ == '__main__':
    file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(file_path1, r'test_files\number.json')
    # read_json_file(file_path)
    data1 = {'name': "pcc"}
    add_to_jsf("\r\n", file_path)
    #print(read_jsf(file_path))