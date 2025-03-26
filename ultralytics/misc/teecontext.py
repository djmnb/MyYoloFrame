import sys

class Tee:
    def __init__(self, filename, mode='a'):
        self.file = open(filename, mode)
        self.stdout = sys.stdout  # 保存原始stdout

    def write(self, text):
        # 将内容同时写入文件和原始stdout
        self.file.write(text)
        self.stdout.write(text)

    def flush(self):
        # 确保缓冲区内容被写入
        self.file.flush()
        self.stdout.flush()

class TeeContext:
    def __init__(self, filename, mode='a'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # 替换sys.stdout为Tee实例
        self.original_stdout = sys.stdout
        sys.stdout = Tee(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 恢复原始stdout并关闭文件
        sys.stdout.file.close()
        sys.stdout = self.original_stdout

