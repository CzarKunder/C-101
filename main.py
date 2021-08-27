import dropbox 
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(fileFrom,"rb")
        dbx.files_upload(f.read(),fileTo)
def main():
    access_token="sl.A254MbUukFkqY3A71eVxeRuZXrWfW_Mgky8JEfiykOiCMQZdKDTRaaizEJF695dtsofb_F43eLuJVuMTdSu6LOCe4MJJxevj_LKaSta0f8P1o5hzLYjpZgJHJwgsPL8FTYeIzfk"
    transferData=TransferData(access_token)
    fileFrom="text.txt"
    fileTo="/folder1/text.txt"
    transferData.uploadFile(fileFrom,fileTo)
    print("file uploaded successfully")
main()