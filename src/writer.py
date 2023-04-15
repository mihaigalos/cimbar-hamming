import os
from datetime import datetime


class Writer:
    def __init__(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        self.today = datetime.today().strftime("%Y%m%d")
        self.output_folder = path+"/"+str(self.today)
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

    def write(self, data):
        filename = self.output_folder + "/" + self.today + \
            "_" + datetime.today().strftime("%H:%M:%S")
        with open(filename, 'w') as f:
            f.write(data)
        f.close()
