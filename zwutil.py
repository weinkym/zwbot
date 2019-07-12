import os
import logging
import time

def create_path(parentpath,dirname):
    d = os.path.join(parentpath,dirname)
    if not os.path.exists(d):
        os.mkdir(d)
    return d

def get_root_path(dirname):
    d = os.path.dirname(__file__)
    return create_path(d,dirname)


def get_temp_path():
    return get_root_path('TEMP')

def get_save_path_pictrue(fileName):
    d = get_temp_path()
    d = create_path(d,'PICTRUE')
    return os.path.join(d,fileName)

def get_save_path_log(fileName):
    d = get_temp_path()
    d = create_path(d,'log')
    return os.path.join(d,fileName)


def init_log():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
    DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"                        # 日期格式
    log_path=get_save_path_log('{}.log'.format(time.strftime("%Y%m%d%H%M%S", time.localtime())))
    fp = logging.FileHandler(log_path, encoding='utf-8')
    fs = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用 

if __name__ == "__main__":
    texts=get_save_path_log('vatInvoice01.jpeg')
    print(type(texts))
    print(texts)