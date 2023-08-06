from io import StringIO,BytesIO

f1 = StringIO('Hello, motherfucker!')
print(f1.read())

f2 = BytesIO('草泥马'.encode('utf-8'))
print(f2.read(), f2.getvalue())
