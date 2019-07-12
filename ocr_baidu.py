#pip install baidu-aip
from aip import AipOcr

APP_ID = '16774289'
API_KEY = 'sy8aMtK3h5KjY1Zo2KtMGMa9'
SECRET_KEY = 'OgYVFXYGP4AzKgLXieaefCrKCMIZ5AyC'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

G_PurchaserName_JC='台州市季诚电子科技有限公司'
G_PurchaserRegisterNum_JC='91331001MA2AL6KY6U'

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_result_data_words_result(result):
    if type(result) is dict:
        if 'words_result' in result:
            return result['words_result']
    
def do_result_data(result):
    print(type(result))
    print(result)
    words_result=get_result_data_words_result(result)
    texts=[]
    if type(result) is dict:
        if 'words_result' in result:
            words_result=result['words_result']
    for w in words_result:
        texts.append(w['words'])
    return texts

def get_dict_string(data,key):
    if key in data:
        temp=data[key]
        if type(temp) is str:
            return temp
        print('key={} value is not string type={}'.format(key,type(temp)))
    print("dict data not has key={}".format(key))
    return ''

def do_result_vatInvoice_data(result):
    
    content='error is happen'
    if type(result) is not dict:
        return content
    print("result={}".format(result))

    PurchaserName=get_dict_string(result,'PurchaserName')
    PurchaserRegisterNum=get_dict_string(result,'PurchaserRegisterNum')
    # SellerRegisterNum=get_dict_string(result,'SellerRegisterNum')
    # SellerName=get_dict_string(result,'SellerName')

    if PurchaserName == G_PurchaserName_JC:
        if PurchaserRegisterNum == G_PurchaserRegisterNum_JC:
            content='验证通过:购方名称={} 购方纳税人识别号={}'.format(G_PurchaserName_JC,G_PurchaserRegisterNum_JC)
        else:
            content='验证错误:购方纳税人识别号错误  ({})({})'.format(PurchaserRegisterNum,G_PurchaserRegisterNum_JC)
    else:
        content='验证错误:购方名称错误  ({})({})'.format(PurchaserName,G_PurchaserName_JC)
    
    return content

    
def get_image_ocr_path(filePath):
    image = get_file_content(filePath)
    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    # result = client.basicGeneral(image, options)
    """ 带参数调用通用文字识别（高精度版） """
    result = client.basicAccurate(image, options)
    return do_result_data(result)

def get_image_ocr_url(url):
    """ 带参数调用通用文字识别, 图片参数为远程url图片 """
    result = client.webImageUrl(url, options)
    return do_result_data(result)

def get_image_ocr_vatInvoice(filePath):
    image = get_file_content(filePath)
    """ 调用增值税发票识别 """
    result = client.vatInvoice(image)
    words_result=get_result_data_words_result(result)
    return do_result_vatInvoice_data(words_result)
    

if __name__ == "__main__":
    texts=get_image_ocr_vatInvoice('/Users/miaozw/Pictures/vatInvoice01.jpeg')
    # texts=get_image_ocr_path('/Users/miaozw/Pictures/test.png')
    # texts=get_image_ocr_url('https://pics2.baidu.com/feed/279759ee3d6d55fbec757dba1044534f21a4dd62.jpeg?token=8ed1451acf5d921a7f50dcb74778652b&s=8012CC32C5E0F9030E6800C6000090B2')
    print(type(texts))
    print(texts)

""" 带参数调用通用文字识别, 图片参数为本地图片 """
# url = "http//www.x.com/sample.jpg"
# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);