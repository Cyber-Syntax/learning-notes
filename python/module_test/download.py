class download:
    def __init__(self):
        self.owner = None
        self.repo = None
        self.api_url = None
        self.sha_name = None
        self.sha_url = None
        self.appimage_name = None
        self.version = None
        self.appimage_folder = None
        self.hash_type = None
        self.url = None
        self.appimages = {}

    def ask_inputs(self):
        while True:
            self.url = input("Enter the app github url: ").strip(" ")
            self.sha_name = input("Enter the sha name: ").strip(" ")
            self.appimage_folder = input("Which directory(e.g /Documents/appimages)to save appimage: ").strip(" ")
            self.hash_type = input("Enter the hash type for your sha (e.g md5, sha256, sha1) file: ").strip(" ")
        
            if self.url and self.sha_name and self.appimage_folder and self.hash_type:
                break
            else:
                print("Invalid inputs, please try again.")

    
