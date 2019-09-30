from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
from pydrive.drive import GoogleDrive
# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
