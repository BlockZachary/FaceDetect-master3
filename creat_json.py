#Author： Zachary
import json
# 列表写入文件
# 测试list

# names = ['None', 'Alice', 'Curry', 'zachary', 'Tom']

names = {
    '1' : 'Alice',
    '2' : 'Curry',
    '3' : 'Zachary'
}

with open('names.json', 'w') as file:
    json.dump(names,file)
file.close()

with open('names.json','r') as f:
    # 读取数据并分割。 最后一个为空，所以去除
    names_result = json.load(f)
f.close()

print("原始数据是：", names)
print("结果数据是：", names_result)

t = 1
str_t = str(t)
print(names[str_t])