import os
import logging
import time
import shutil
import locale

#logging.basicConfig(level=logging.INFO)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class MyFile(object):
    def __init__(self, f_mtime, f_type, f_size, f_name):
        self.f_mtime = f_mtime
        self.f_type = f_type
        self.f_size = f_size
        self.f_name = f_name

    @property
    def f_mtime(self):
        return self._f_mtime

    @f_mtime.setter
    def f_mtime(self, value):
        self._f_mtime = value

    @property
    def f_type(self):
        return self._f_type

    @f_type.setter
    def f_type(self, value):
        self._f_type = value

    @property
    def f_size(self):
        return self._f_size

    @f_size.setter
    def f_size(self, value):
        self._f_size = value

    @property
    def f_name(self):
        return self._f_name

    @f_name.setter
    def f_name(self, value):
        self._f_name = value

    def __str__(self):
        mtime = time.strftime('%Y/%m/%d %H:%M',time.localtime(self.f_mtime))
        if self.f_size != '':
            size = locale.format_string('%d', self.f_size, grouping=True)
        else:
            size = self.f_size
        return '%s\t%s\t%s\t%s' % (mtime, self.f_type, size.rjust(10), self.f_name)


class MyDir(object):
    def __init__(self, path):
        self.path = path

    def dir_l(self):
        path = self.path
        if not os.path.isdir(path):
            raise FileNotFoundError('%s is not a dir' % path)
        
        f_list = []
        count_file,count_dir = 0,0
        size_file = 0
        # .
        f_mtime = os.path.getmtime(path)
        f_type = '<DIR>'
        f_size = ''
        f_name = '.'
        f_list.append(MyFile(f_mtime, f_type, f_size, f_name))
        count_dir += 1
        # ..
        f_mtime = os.path.getmtime(os.path.dirname(path))
        f_type = '<DIR>'
        f_size = ''
        f_name = '..'
        f_list.append(MyFile(f_mtime, f_type, f_size, f_name))
        count_dir += 1
        
        # foreach
        for f in os.listdir(path):
            f_abs = os.path.join(path, f)
            f_mtime = os.path.getmtime(f_abs)
            if os.path.isdir(f_abs):
                f_type =  '<DIR>'
                f_size = ''
                count_dir += 1
            else:
                f_type = ''
                f_size = os.path.getsize(f_abs)
                count_file += 1
                size_file += f_size
            f_name = f

            f_list.append(MyFile(f_mtime, f_type, f_size, f_name))

        _,_,size_available = shutil.disk_usage(path)
        
        # print
        self.__print_f(f_list, count_file, count_dir, size_file, size_available)

    def __print_f(self, f_list, count_file, count_dir, size_file, size_available):
        for f in f_list:
            print(f)
        count_file = str(count_file) + ' 个文件'
        count_dir = str(count_dir) + ' 个目录'
        size_file = str(locale.format_string('%d', size_file, grouping=True)) + ' 字节'
        size_available = str(locale.format_string('%d', size_available, grouping=True)) + ' 字节'
        print('%s\t%s\t%s\t%s' % ('', count_file.rjust(10), '', size_file.rjust(20)))
        print('%s\t%s\t%s\t%s' % ('', count_dir.rjust(10), '', size_available.rjust(20)))


def test():
    path = input('Please Input Your Path: ')
    d = MyDir(path)
    d.dir_l()


if __name__ == '__main__':
    test()
