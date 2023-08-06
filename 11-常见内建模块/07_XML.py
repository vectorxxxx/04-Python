# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    def __init__(self):
        self.pointer = ''
        self.city = ''
        self.forecast = []
        self.weather = {}
        
    def start_element(self, name, attrs):
        self.pointer = name

    def end_element(self, name):
        self.forecast.append(self.weather)

    def char_data(self, text):
        if self.pointer == 'city':
            self.city = text
        elif self.pointer == 'date':
            self.weather['date'] = text
        elif self.pointer == 'daytemp':
            self.weather['high'] = int(text)
        elif self.pointer == 'nighttemp':
            self.weather['low'] = int(text)

    def toJSON(self):
        return {'city':self.city, 'forcast': self.forecast}
    
        
def parseXml(xml_str):
    print(xml_str)
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    print(handler.toJSON())
    return handler.toJSON()


# 测试:
URL = 'https://restapi.amap.com/v3/weather/weatherInfo?key=a4238a61f892a6692453252cef687735&city=320582&extensions=all&output=XML'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == '张家港市'
print('ok')
