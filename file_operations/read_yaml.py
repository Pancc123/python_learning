import yaml,os


# 获取yaml文件中的参数
def get_config(file_path):
    try:
        http_config = yaml.load(open(file_path, "r"), Loader=yaml.FullLoader)
        return http_config
    except FileNotFoundError as e:
        print("没有找到文件")
        raise e


if __name__ == '__main__':
    file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(file_path1, r'test_files\test.yaml')
    # file_path = os.path.join(file_path1, r'test_files\login.yaml')
    data = get_config(file_path)
    print(list(data[3].keys()))
    # print(type(data[0]))
    # print(data[0]['login_ok'])

