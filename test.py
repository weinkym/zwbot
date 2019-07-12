import os
import logging
import zwutil
import time


       

def testType():
    eventList = [1, 'Tom', {'name': 'Lucy', 'age': 16, 'grade': 98}]
    print(type(eventList[0]) is int)
    print(type(eventList[1]) is int)
    print(type(eventList[1]) is str)
    print(type(eventList[2]) is dict)
    temp='Tom'
    print("string is {}".format(eventList[1] == temp))

def test(filePath):
    with open(filePath, 'w') as fp:
        fp.write('111')

# d = os.path.dirname(__file__)
# d = os.path.join(d,'TEMP')
# os.mkdir(d)
# d = os.path.join(d,'test.txt')

zwutil.init_log()

l_temp=['拼多条', '5', '好量未来', 'DE IN CHA']
content=''.join('{}\n'.format(str(i)) for i in l_temp)
logging.info(content)

# print(time.strftime("%Y-%m-%d%H:%M:%S", time.localtime()))
# testType()
# test(d)

print(type(type(testType)))