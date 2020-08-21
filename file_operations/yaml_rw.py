import yaml,os
#from ruamel import yaml


# yaml模块获取yaml文件中的参数
def get_config(file_path):
    try:
        http_config = yaml.load(open(file_path, "r"), Loader=yaml.FullLoader)
        return http_config
    except FileNotFoundError as e:
        print("没有找到文件")
        raise e


''' 
# 原生写入yaml文件，但是内部嵌套字典会显示大括号
#with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f)
# 用原生yaml 模块读取yaml文件 用python读取yaml文件案例，先用open方法读取文件数据，再通过load方法转成字典，这个load跟json里面的load是相似的
# with open('test.yaml', 'r', encoding='utf-8') as f:
      print(yaml.load(f.read(),Loader=yaml.Loader))
      
# 用 ruamel 写入
from ruamel import yaml
# with open("test.yaml","w",encoding="utf-8") as f:
#     yaml.dump(desired_caps,f,Dumper=yaml.RoundTripDumper)
'''





if __name__ == '__main__':
    file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(file_path1, r'test_files\test.yaml')
    # file_path = os.path.join(file_path1, r'test_files\login.yaml')
    data = get_config(file_path)
    print(list(data[3].keys()))
    # print(type(data[0]))
    # print(data[0]['login_ok'])

