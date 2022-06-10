import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,filename=''):
        if(filename==''):
            return None
        try:
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def delete(self, filename):
        try:
            if not os.path.exists(filename):
                #gagal
                print("Gagal, file {} tidak ditemukan pada remote server".format(filename))
                return
            os.remove(filename)
            return dict(status='OK',data="File {} berhasil dihapus".format(filename))
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def upload(self, filename, data):
        try:
            fp = open(f"{filename}",'wb+')
            file_binary = base64.b64decode(data)
            fp.write(file_binary)
            fp.close()

            return dict(status='OK',data="File {} berhasil disimpan".format(filename))
        except Exception as e:
            return dict(status='ERROR',data=str(e))



if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get('pokijan.jpg'))
