import requests
import json

class Release:       
    def get_input(self):
        self.github_owner = input("GitHub Owner: e.g 'siyuan-note' ")
        self.app_name = input("Github Project name e.g 'siyuan': ")
        self.api_url = f"https://api.github.com/repos/{self.github_owner}/{self.app_name}/releases/latest"
            
    @staticmethod
    def get_data(url):   
        global data     
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)            
            return data
        else:
            raise Exception("Failed to fetch latest release information")
    
    @staticmethod
    def get_version(data):
        version = data["tag_name"].replace("v", "")
        return version

# !, global
    def download(self, checksum_file):       
        global checksum_file
        data = self.get_data(self.api_url)
        version = self.get_version(data)


        checksum_url = [asset["browser_download_url"] for asset in data["assets"] if asset["name"] == checksum_file][0]
        

        
        if response.status_code == 200:
            content = response.text
            pattern = f"{checksum_file} * {version}"
            with open(checksum_file, "w") as f:
                f.write(content)
            print(f"Checksum file '{checksum_file}' and'{self.app_name}-{version}' has been downloaded.")                        
            return checksum_file
        else:
            raise Exception("Failed to download checksum file.")

# !, continue here    
    def verify_checksum(self):
        data = self.get_data(self.api_url)
        self.get_data(self.api_url)

        appimage_name = [asset["name"] for asset in data["assets"] if asset["name"].endswith(".AppImage")][0]
        
        with open(response, "r") as f:
            for line in f:
                checksum, filename = line.strip().split()
                if appimage_name == filename:
                    with open(appimage_name, "rb") as f:
                        file_checksum = hashlib.sha256(f.read()).hexdigest()
                        if file_checksum == checksum:
                            return print("verified")                        
                        else:
                            return False
            return False


#! , test edilmedi
class File:    
    def log_version(self, release, app_name):
        data = release.get_data(release.api_url)
        version = release.get_version(data)
        
        # Create file for logging siyuan version       
        filename = f"{app_name}-version"
        with open(filename, "a") as f:
            f.write(f"{version}\n")
        with open(filename, "r") as f:
            print(f.read(), "The version is logged.")

        # Move to appimage directory
        current_directory = os.getcwd()
        try:
            #!, current_directory need to change for user appimage directory.
            os.rename(f"{current_directory}/{filename}", f"{current_directory}/appimages/{filename}")    
            print("Appimage version successfully logged.")            
    
        except FileNotFoundError:
            print("Error: while moving files to appimages directory")
            return
    
    def save_old():
        
        # Find current directory
        pwd = ["pwd"]
        result_pwd = subprocess.run(pwd, capture_output=True) 
        
        # Solve, unknown parameters     
        last = result_pwd.stdout.decode('utf-8')[:-1] 
        
        # Check if the file already exists in the folder
        if os.path.exists(appimages_path):
            print(f"siyuan.AppImage found at {appimages_path}")
            confirm = input(f"If you want to overwritten (y), want to backup old (n)?")

            # The file is overwritten or backed up      
            if confirm.lower() == 'y':                                                              
                subprocess.run(["mv", f"{appimages_path}", appimages_dir])                                                              
            else:
                # backup old version
                subprocess.run(["mv", f"{appimages_path}", "siyuan.old.AppImage"])
                subprocess.run(["mv", "siyuan.old.AppImage", backup_dir])

                # Move new version to appimages directory
                subprocess.run(["mv", f"{appimages_path}", appimages_dir])       

def main():
    r = Release()
    r.get_input()
    r.download("SHA256SUMS.txt")   
    r.verify_checksum()
#    f = File()
#    f.log_version(r)


if __name__ == "__main__":
    main()
