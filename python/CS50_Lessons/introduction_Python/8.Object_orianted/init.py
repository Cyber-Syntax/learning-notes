"""How init working.. Object Oriented"""

class AppImage:
    def __init__(self, repo, name):
        self.repo = repo
        self.name = name

    def save(self):
        print(f"This {self.repo} and {self.name} saved")

    def install(self):
        print("AppImage installing...")

    def get_repo(self):
        return [self.repo, self.name]
    
    def set_repo(self, repo, name):
        self.repo = repo
        self.name = name
        

appimage_1 = AppImage('siyuan-note', 'siyuan')

print(appimage_1.repo) # siyuan-note
print(appimage_1.name) # siyuan

appimage_1.save()
appimage_1.install()

print(appimage_1.get_repo()) # ['siyuan-note', 'siyuan']
print(appimage_1.set_repo('Laurent22', 'Joplin'))
print(appimage_1.get_repo()) # ['Laurent22', 'Joplin']