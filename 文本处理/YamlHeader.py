import pathlib
import yaml
import time
import os

root = pathlib.Path("/home/geek/Code/Blog/source/_posts")

'''
转换时间戳格式为 YYYY-MM-DD HH:MM:SS
'''
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
'''
获取文件创建时间
'''
def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

def SearchMarkDown(current_path):
    file_list = [path for path in current_path.iterdir()]

    for path in file_list:
        ## 文件夹
        if path.is_dir():
            SearchMarkDown(path)
            continue
        ## Markdown

        ### 检查是否已经添加yaml
        name = path.name.split('.')[0]
        text = path.read_text(encoding='utf-8')
        header_position = text.count("---")
        if header_position >= 2 and 0 == text.find("---") : continue

        ### 添加yaml
        header = {}
        header['title'] = name
        header['toc'] = True
        header['date'] = get_FileCreateTime(path)
        # print(header)
        text = "---\n"+yaml.dump(header,allow_unicode=True)+"---\n" + text
        # print(yaml.dump(header,allow_unicode=True,encoding='utf-8'))
        path.write_text(text)
        print(name)


SearchMarkDown(root)
