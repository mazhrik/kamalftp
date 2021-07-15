from ftplib import FTP, error_perm

# ftp = FTP('ftp.us.debian.org')  # connect to host, default port
# print(ftp.login())
# import ftplib
# with ftplib.FTP('ftp.somehost.it') as ftp:
#     ftp.login('testuser', 'password')
#
FILE_SERVER = '192.168.18.33'
USERNAME = 'microcrawler'
PASSWORD = 'rapidev'
PORT = 21
HOST = FILE_SERVER
PORT = PORT
USERNAME = USERNAME
PASSWORD = PASSWORD
BASE_PATH = 'cms'
import os.path, os


class FTP_Client(object):

    def __init__(self):
        self.ftp = FTP()

    def connect(self):

        try:
            self.ftp.connect(HOST, PORT)
            return True

        except error_perm as e:
            print(e)
            return False

    def login(self):
        try:
            self.connect()
            self.ftp.login(USERNAME, PASSWORD)
            return True
        except error_perm as e:
            print(e)
            return False

    def directory_exists(self, dir):
        filelist = []
        self.ftp.retrlines('LIST', filelist.append)
        print(filelist)

        for f in filelist:
            if f.split()[-1] == dir and f.upper().startswith('D'):
                return True
        return False

    def chdir(self, dir):
        if self.directory_exists(dir) is False:
            self.ftp.mkd(dir)
        self.ftp.cwd(dir)

    def create_directory_path(self, path):
        temp_path = ''
        temp_path_list = []

        try:
            path_list = path.split('/')
            path_list = list(filter(lambda i: len(i) > 0, path_list))

            for dir in path_list:
                temp_path = temp_path + dir + '/'
                temp_path_list.append(temp_path)
                self.chdir(dir)  # change to directory if not exist create one


        except Exception as e:
            print(e)
            print('--------------')
            print(temp_path_list)

    def upload_f(self, file_pick_path, filename):

        if os.path.isfile(os.path.join(file_pick_path, filename)):
            print("STOR>", filename)
            self.ftp.storbinary('STOR ' + filename, open(os.path.join(file_pick_path, filename), 'rb'))
        else:
            print('elssssssssssssssssse')

    def upload_file(self, file_pick_path, filename, file_drop_path=''):
        if (self.login()):
            try:
                self.chdir(BASE_PATH)
                self.create_directory_path(file_drop_path)
                self.upload_f(file_pick_path, filename)
                return f"{HOST}/{file_drop_path}"

            except error_perm as e:
                print(e)
                return False

        self.quit()
        return True

    def newfunc(self):
        if (self.login()):
            try:
                print('--------------------------->', self.ftp.cwd('cms/ess_frs'))
                self.ftp.retrlines('LIST')
            except error_perm as e:
                print(e)
                return False
        else:
            pass


obj = FTP_Client()
obj.login()
obj.connect()
filename = 'istockphoto-535695503-612x612'
var = (obj.upload_file('/home/zohaib/Desktop/', filename, 'ess_frs'))
url = 'https://' + var + '/' + filename
print('larki.jpeg')

obj.newfunc()

