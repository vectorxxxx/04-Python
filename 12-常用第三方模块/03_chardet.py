import chardet

str = chardet.detect(b'Hello motherfucker!')
print(str)

str = chardet.detect('你好，草泥马！'.encode('utf-8'))
print(str)

str = chardet.detect('你好，草泥马！你好，草泥马！'.encode('gbk'))
print(str)

str = chardet.detect('最新の主要ニュース'.encode('euc-jp'))
print(str)

