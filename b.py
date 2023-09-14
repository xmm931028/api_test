import requests

# data_name = ['company','person','bid']
# data_count = [111,222,333]
#
# data_dict = {}
#
# for i in range(len(data_name)):
#     data_dict[data_name[i]] = data_count[i]
#
#
# print(data_dict)


# outside=['user','commodity','Shopping']
# pieces_num=[1000,3999,2000]
#
# def merge(outside,pieces_num):  #封装
#     mer={}  # 定义为字典格式
#     # mer['ours']=outside
#     # mer['pieces']=pieces_num
# #循环取出两个列表中的信息并附给outside，pieces_num，进行打印输出
#     for key,value in zip(outside,pieces_num):
#         mer[key]=value
#         # print(mer)
#
#     return mer
#
# mer_a=merge(outside,pieces_num)
# print(mer_a)




# def user_login():
#     url = 'xxxxxx',
#     header = {
#         "Content-Type":"xxx",
#         "User-Agent:":"xxx"
#     },
#     data = {
#         "username":"",
#         "password":""
#     }
#     response = requests.post(url=url,headers=header,json=data)
#     print(response.json())
#

#计算从1-n中出现了多少个9，n是一个正整数
# def num(n):
#     count = 0
#     for i in range(1,n+1):
#         count += str(i).count('9')
#
#     return count
#
#
# print(num(100))

""" 给定一个字符串，
将它们其中的每个字符（区分大小写）再重复一次。 
示例：输入："Hogwarts"，输出："HHooggwwaarrttss" """

# def num2(str_a):
#     num_new=[]
#     for i in range(len(str_a)):
#         if i in str_a:
#             num_new.append(i*2)
#
#
#     return ''.join(num_new)
#
#
# print(num2('Hogwarts'))


# def str2(input_str):
#     output_str = ''
#     for char in input_str:
#         output_str += char*2
#     return output_str
#
# print(str2('Hogwarts'))

item_id='7926332075054106120'
item_ids: ['7926332075054106120']


new_list =[item_id]
print(new_list)

