#TODO,We can't acces appimageName other class. I must access that attiribute.
class AppImage:
    def __init__(self):
        self.appimageName = None
        self.shaName = None
    
    def show(self):
        print(f"I am {self.appimageName} and I am {self.shaName}")
    
    
class AppImageDownload(AppImage):
    def __init__(self, githubRepo, githubOwner):
        super().__init__()
        self.githubRepo = githubRepo
        self.githubOwner = githubOwner
  
    def set_appimageName(self):
        self.appimageName = "VSCode"
        self.shaName = "sha256.yml"
        return self.appimageName

    def show(self):
        return self.githubRepo, self.githubOwner, self.appimageName

class FileHandler(AppImage):
    def __init__(self, appimageDir):
        super().__init__()
        self.appimageDir = appimageDir

    def show(self):
        return self.appimageName

# appimage1 = AppImage('Joplin', 'sha512.yml')    
# appimage1.show()

# a2 = AppImageDownload('siyuan-note', 'siyuan')
# print(a2.show())


download = AppImageDownload('siyuan', 'siyuan-note')
download.set_appimageName()
print(download.show())

filehandler = FileHandler('dir/')
print(filehandler.show())