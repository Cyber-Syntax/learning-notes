import requests
import hashlib
import os, re
import subprocess

class AppImageDownloader:
    
    def __init__(self, owner, repo, sha=None, appimage_name=None):
        self.owner = owner
        self.repo = repo
        self.sha = sha
        self.appimage_name = appimage_name
        self.records = {}
        
    def save_records(self):
        if os.path.exists('records.txt'):
            with open('records.txt') as f:
                self.records = json.load(f)
        
        self.records[self.repo] = {'owner': self.owner, 'repo': self.repo}
        
        with open('records.txt', 'w') as f:
            json.dump(self.records, f)       
   
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
        self.save_records()

    def download_verify(self):
        if self.verify_url is None:
            self.verify_file = input("Enter the full name of the verify file: ")
            print("Downloading...")
            self.verify_url = f"https://github.com/{self.owner}/{self.repo}/releases/download/v{self.version}/{self.verify_file}"
        response = requests.get(self.verify_url)
        with open(self.verify_file, "wb") as f:
            f.write(response.content)


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