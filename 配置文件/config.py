import configparser


# 注意python3开头小写而2开头大写

def write(file, my_config:configparser.ConfigParser):
    ## 添加内容
    my_config.add_section("my ini")
    my_config.set("my ini", "user","wfcyywh1225")
    my_config.set("my ini", "password","1234353")
    my_config.set("my ini", "target_email","asd")

    ## 写入文件
    with open(file,"w") as f:
        my_config.write(f)


def read(file, my_config: configparser.ConfigParser):
    my_config.read(file,encoding='utf-8')
    user = my_config.get("my ini", "user")
    password = my_config.get("my ini","password")
    print(user,password)

if __name__ == "__main__":
    # init
    config = configparser.ConfigParser()
    write("config.ini", config)
    read("config.ini",config)
