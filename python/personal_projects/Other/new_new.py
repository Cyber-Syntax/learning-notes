import requests
import os

class GithubAppImageDownloader:
    def __init__(self):
        self.owner = None
        self.repo = None
        self.appimage_name = None
        self.records = {}

    def download_appimage(self):
        """        If owner and repo None, run get_appimage_details() """
        if self.owner is None or self.repo is None:
            self.get_appimage_details()

        # Get the latest version appimage infos with api
        release_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
        response = requests.get(release_url)
        
        # Get appimage version 
        latest_version = response.json()["tag_name"].replace("v", "")
        appimage_url = f"https://github.com/{self.owner}/{self.repo}/releases/download/{latest_version}/{self.appimage_name}"

        # Get appimage with request
        response = requests.get(appimage_url)
        if response.status_code == 404:
            print("AppImage not found.")
            return

        with open(self.appimage_name, "wb") as f:
            f.write(response.content)

        # save credentials with save_record() function
        self.save_record()
        print("AppImage download successful.")

    def get_appimage_details(self):
        """ Get appimage credentials """
        self.owner = input("Enter the Github repository owner: ")
        self.repo = input("Enter the Github repository name: ")

        response = requests.get(f"https://api.github.com/repos/{self.owner}/{self.repo}/releases")
        releases = response.json()
        appimage_names = [asset["name"] for release in releases for asset in release["assets"] if asset["name"].endswith(".AppImage")]

        if not appimage_names:
            print("No AppImage found for this repository.")
            return

        if len(appimage_names) == 1:
            self.appimage_name = appimage_names[0]
        else:
            self.appimage_name = input("Enter the exact name of the AppImage (e.g. endswith '.AppImage'): ")

    def save_record(self):
        record = {"owner": self.owner, "repo": self.repo, "appimage_name": self.appimage_name}
        if self.owner in self.records:
            self.records[self.owner].append(record)
        else:
            self.records[self.owner] = [record]

        with open("records.txt", "w") as f:
            f.write(str(self.records))

    def load_records(self):
        if os.path.exists("records.txt"):
            with open("records.txt", "r") as f:
                self.records = eval(f.read())

if __name__ == "__main__":
    downloader = GithubAppImageDownloader()
    downloader.load_records()
    downloader.download_appimage()
