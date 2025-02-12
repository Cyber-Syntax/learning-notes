class AppImage:
    def __init__(self, appimageName, githubRepo, shaName):
        self.appimageName = appimageName
        self.githubRepo = githubRepo
        self.shaName = shaName
    
    def get_appimageName(self):
        return self.appimageName

    def set_appimageName(self, appimageName):
        self.appimageName = appimageName

    
class FileHandler:
    def __init__(self, appimageName, shaName):
        self.appimageName = appimageName
        self.shaName = shaName
    
    def changeName(self, appimageName):
        self.appimageName = appimageName
    
    def get_appimageName(self):
        return self.appimageName

# AppImage
appimage_1 = AppImage('Joplin', 'Laurent22', 'sha256.yml')

print(appimage_1.get_appimageName()) # Joplin
print(appimage_1.set_appimageName('Siyuan')) # None
print(appimage_1.get_appimageName()) # Siyuan


# FileHandler
appimage_f = FileHandler('VSCodium', 'sha512.yml')

print(appimage_f.changeName('VSCode')) 

print(appimage_f.get_appimageName()) # VSCode