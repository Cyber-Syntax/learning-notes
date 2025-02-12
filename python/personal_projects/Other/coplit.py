import requests

class AppImageDownloader:
    def __init__(self):
        self.appimages = {}

    def save_appimage(self, owner, repo, appimage_name):
        """Save the AppImage name for a given repository in the form of {owner: {repo: appimage_name}}"""
        if owner not in self.appimages:
            self.appimages[owner] = {}
        self.appimages[owner][repo] = appimage_name

    def get_appimage(self, owner, repo):
        """Return the AppImage name for a given repository if it exists, otherwise None."""
        if owner in self.appimages and repo in self.appimages[owner]:
            return self.appimages[owner][repo]
        return None

    def download_verify(self, owner, repo, sha, file_name):
        """Download the AppImage from the given repository, verify it, and save it to file_name."""
        appimage_name = self.get_appimage(owner, repo)
        if not appimage_name:
            appimage_name = self.ask_for_appimage_name(owner, repo)
            self.save_appimage(owner, repo, appimage_name)

        appimage_url = f"https://github.com/{owner}/{repo}/releases/download/{sha}/{appimage_name}"
        response = requests.get(appimage_url)
        if response.status_code == 200:
            with open(file_name, "wb") as f:
                f.write(response.content)
            return True
        return False

    def ask_for_appimage_name(self, owner, repo):
        """Prompt the user to enter the AppImage name for the given repository."""
        appimage_name = input(f"AppImage name for {owner}/{repo} not found. Please enter it: ")
        return appimage_name

def main():
    """Main function to download and verify the AppImage"""
    a = AppImageDownloader()
    owner = input("Enter the owner of the repository: ")
    repo = input("Enter the name of the repository: ")
    sha = input("Enter the sha of the release: ")
    file_name = input("Enter the name of the file you want to save: ")
    if a.download_verify(owner, repo, sha, file_name):
        print(f"{file_name} was successfully saved.")
    else:
        print(f"Failed to download {file_name}.")

if __name__ == "__main__":
    main()
