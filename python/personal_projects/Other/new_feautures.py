import requests
import hashlib
import os, re
import subprocess

class AppImageDownloader:

    def __init__(self):
        self.owner = None
        self.repo = None
        self.appimage_url = None
        self.verify_url = None
        self.appimage_file = None
        self.verify_file = None
        self.version = None

    def save_credentials(self, owner, repo):        
        credentials = input("Do you want to save these credentials for future use? (y/n)")
        
        if credentials.lower() == "y":
            with open("credentials.txt", "w") as file:
                f.write(owner + "\n")
                f.write(repo + "\n") 
                f.write(sha_file + "\n")          
                f.write(hash_type + "\n")
        else:
            return owner, repo, sha_file


    def load_credentials():
        try:
            with open("credentials", "r") as file:
                lines = file.readlines()
                owner = lines[0].strip()
                repo = lines[1].strip()
                return owner, repo
        except FileNotFoundError():
            return save_credentials()

    def get_urls(self):
        print("Downloading...")
        api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
        response = requests.get(api_url)        

        if response.status_code == 200:
            data = response.json()
            self.version = data["tag_name"].replace("v", "")                                            
            for asset in data["assets"]:
                # Find appimage, sha256 file names and download them.
                if asset["name"].endswith(".AppImage"):                    
                    self.appimage_url = asset["browser_download_url"]
                    self.appimage_file = asset["name"]
                elif asset["name"].endswith(".sha256"):
                    self.verify_url = asset["browser_download_url"]
                    self.verify_file = asset["name"]
                

    def download_appimage(self):        
        if self.appimage_url is None:
            self.appimage_file = input("Enter the full name of the AppImage file: ")
            print("Downloading...")
            self.appimage_url = f"https://github.com/{self.owner}/{self.repo}/releases/download/v{self.version}/{self.appimage_file}"
        response = requests.get(self.appimage_url)
        with open(self.appimage_file, "wb") as f:
            f.write(response.content)

    def download_verify(self):
        if self.verify_url is None:
            self.verify_file = input("Enter the full name of the verify file: ")
            print("Downloading...")
            self.verify_url = f"https://github.com/{self.owner}/{self.repo}/releases/download/v{self.version}/{self.verify_file}"
        response = requests.get(self.verify_url)
        with open(self.verify_file, "wb") as f:
            f.write(response.content)
#! error
    def verify(self):  
        hash_type = input("What is the hash type in your verify file: ")
        print("Verifying...")
        if hash_type not in ["sha256", "sha512"]:
            print("Error: Unsupported hash type")
            exit(1)

        with open(self.verify_file, "r") as f:
            contents = f.read()

        match = re.search(self.appimage_file, contents)
        if not match:
            print("Error: AppImage file not found in the verify file")
            exit(1)

        cmd = [hash_type + "sum", self.appimage_file, "-c", self.verify_file]
        result = subprocess.run(cmd, capture_output=True, text=True)              
        if f"{self.verify_file}: OK" in result.stdout:
            print("AppImage verified successfully")                       
        else:
            print("Error: Verification failed")
            exit(1)

# class FileHandler:

#     def __init__(self, appimage_dir, appimage_name):
#         self.appimage_dir = appimage_dir
#         self.appimage_name = appimage_name

#     def log_version():


#     def move_to_destination(self, destination):
#         try:
#             os.makedirs(destination, exist_ok=True)
#             os.rename(self.appimage_file, os.path.join(destination, self.appimage_file))
#             os.rename(self.verify_file, os.path.join(destination, self.verify_file)

def main():
    owner = input("What is the github owner name: ")
    repo = input("What is the github repo name: ")
    a = AppImageDownloader(owner, repo)
    
    a.get_urls()
    a.download_appimage()
    a.download_verify()
    a.verify()

if __name__ == "__main__":
    main()


        
        