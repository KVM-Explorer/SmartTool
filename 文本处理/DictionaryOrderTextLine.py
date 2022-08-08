import pathlib

root = pathlib.Path("./")


def ConvertToDirectoryOrder(random_content:list):
    random_content.sort()
    return random_content

def WriteFile(content,path):
    with open(path,"w") as f:
        f.writelines(content)

def ReadFile(path):
    with open(path,'r') as f:
        content = f.readlines()
        return content

def SearchTextFiles(current_path:pathlib.Path,extend_name):
    file_list = [path for path in current_path.iterdir()]

    for path in file_list:
        ## 文件夹
        if path.is_dir():
            SearchTextFiles(path,extend_name)
            continue
        if path.suffix not in extend_name: continue
        random_content = ReadFile(path)
        res = ConvertToDirectoryOrder(random_content)
        filename = path.stem+"_new.txt"
        new_path = path.with_name(filename)
        WriteFile(res,new_path)
    
    
if __name__=="__main__":

    SearchTextFiles(root,[".txt"])
