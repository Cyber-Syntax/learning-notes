import download
import json
import os

class filehandler(download.download):
    def __init__(self):
        super().__init__()
        

        
    def save_credentials(self):
        """Save the credentials to a file in json format, one file per owner and repo"""
        self.appimages["owner"] = self.owner
        self.appimages["repo"] = self.repo
        self.appimages["appimage"] = self.appimage_name
        self.appimages["version"] = self.version
        self.appimages["sha"] = self.sha_name
        self.appimages["hash_type"] = self.hash_type
        # add "/" to the end of the path if not exists
        if not self.appimage_folder.endswith("/") and not self.appimage_folder.startswith("~"):
            self.appimages["appimage_folder"] = os.path.expanduser("~") + self.appimage_folder + "/"
        elif self.appimage_folder is not None and self.appimage_folder.startswith("~") and self.appimage_folder.endswith("/"):
            self.appimage_folder = os.path.expanduser("~") + self.appimage_folder
        elif self.appimage_folder is not None and self.appimage_folder.startswith("~") and not self.appimage_folder.endswith("/"):
            self.appimages["appimage_folder"] = os.path.expanduser("~") + self.appimage_folder + "/"

        with open(f"{self.repo}.json", "w", encoding="utf-8") as file:
            json.dump(self.appimages, file, indent=4)
        print(f"Saved credentials to {self.repo}.json file")    