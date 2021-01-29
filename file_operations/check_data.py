# import json
#
#
# def check_response(self, case_name, file_data, response):
#     # yaml case
#     check_type = file_data['check_type']
#     check_data = file_data['check_data']
#     try:
#         text = json.loads(response.text)
#         # print(text)
#         for key in check_type.keys():
#             if check_type[key] == '1':
#                 # print(text[key])
#                 assert text[key] is not None, "失败测试用例：response返回值" + check_data[key]
#             elif check_type[key] == '2':
#                 # print(type(check_data[key]))
#                 assert text[key] is None, "失败测试用例：response返回值" + check_data[key]
#             elif check_type[key] == '3':
#                 assert text[key] == check_data[key], "失败测试用例：response返回值" + str(text[key]) + \
#                                                      "不等于期望结果" + check_data[key]
#             elif check_type[key] == '4':
#                 response_data = text[key]
#                 data = check_data[key]
#                 while True:
#                     data_type=type(data)
#                     if data_type == str:
#                         assert response_data ==check_data[key] , "测试失败：response返回值" + response_data + \
#                                                            "不等于期望结果" + check_data[key]
#                         break
#                     if data_type == list:
#                         data = check_data[key][0]
#                         continue
#                     if data_type == dict:
#
#
#
#
#
#
#                 # print(list1)
#                 num = len(list1)
#                 # print(num)
#                 while num >= 1:
#                     if type(response_data) == str:
#                         # if response_data == list1[-1]:
#                         # print("ok")
#                         assert response_data == list1[-1], "测试失败：response返回值" + response_data + \
#                                                            "不等于期望结果" + list1[-1]
#                         num = num - 1
#
#                     elif type(response_data) == dict:
#                         response_data = response_data[list1[0]]
#                         num = num - 1
#                         # 去除第一个列表元素
#                         del list1[0]
#
#                     elif type(response_data) == list:
#                         response_data = response_data[list1[0]]
#                         num = num - 1
#                         # 去除第一个列表元素
#                         del list1[0]
#
#             else:
#                 self.mylog.error('未找到校验类型：' + str(key))
#     except Exception as e:
#         self.mylog.error('测试失败：' + case_name + ' 返回结果：' + str(response))
#         raise e
#     self.mylog.info('测试通过' + str(case_name))