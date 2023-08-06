import os
import logging


class FindFile(object):
    def __init__(self):
        self.f_path = []

    def getCwdFilePath(self, ext):
        self.getFilePath(os.getcwd(), ext)

    def getFilePath(self, root, ext):
        logging.info('检索根目录：%s' % root)
        self.__findFile(root, ext)
        self.__print()
        
    def __findFile(self, root, ext, path=''):
        for f in os.listdir(os.path.join(root, path)):
            f_abs = os.path.join(root, path, f)
            logging.info('正在检索：', f_abs)
            if os.path.isdir(f_abs):
                self.__findFile(root, ext, os.path.join(path, f))
            elif os.path.isfile(f_abs) and os.path.splitext(f_abs)[1] == ext:
                self.f_path.append(os.path.join(path, f))

    def __print(self):
        logging.info('=============================')
        logging.info('检索结果：')
        for path in self.f_path:
            print(path)


if __name__ == '__main__':
    #path = 'D:/workspace-mine/python'
    #ext = '.py'
    FindFile().getCwdFilePath('.py')
    
    logging.info('=============================')

    #path = 'C:/Users/uxiah/Documents/Epoint'
    #ext = '.docx'
    FindFile().getFilePath('C:/Users/uxiah/Documents/Epoint', '.docx')
