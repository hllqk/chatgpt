#写python文件管理器
import os

class FileManager:
    def __init__(self):
        self.current_dir = os.getcwd()  # 初始化当前目录
        self.all_files = os.listdir(self.current_dir)  # 列出当前目录下的所有文件

    # 显示当前路径
    def show_current_dir(self):
        print(self.current_dir)

    # 显示当前路径下所有文件
    def show_all_files(self):
        for i in self.all_files:
            print(i)

    # 切换到指定路径
    def change_dir(self, path):
        if os.path.isdir(path):  # 如果路径存在
            self.current_dir = path
            self.all_files = os.listdir(self.current_dir)  # 列出当前路径下的所有文件
            print('切换成功')
        else:
            print('路径不存在')

    # 删除指定文件
    def delete_file(self, filename):
        if filename in self.all_files:  # 如果文件存在
            os.remove(os.path.join(self.current_dir, filename))  # 删除文件
            self.all_files.remove(filename)  # 从all_files列表中移除
            print('删除成功')
        else:
            print('文件不存在')

    # 重命名文件
    def rename_file(self, old_name, new_name):
        if old_name in self.all_files:  # 如果文件存在
            os.rename(os.path.join(self.current_dir, old_name),
                      os.path.join(self.current_dir, new_name))  # 重命名
            self.all_files.remove(old_name)  # 从all_files列表中移除
            self.all_files.append(new_name)  # 添加新文件名
            print('重命名成功')
        else:
            print('文件不存在')


if __name__ == '__main__':
    my_file_manager = FileManager()
    my_file_manager.show_current_dir()
    my_file_manager.show_all_files()
    my_file_manager.change_dir('/Users/xxx/Desktop')
    my_file_manager.show_all_files()
    my_file_manager.delete_file('test.txt')
    my_file_manager.show_all_files()
    my_file_manager.rename_file('test2.txt', 'test3.txt')
    my_file_manager.show_all_files()