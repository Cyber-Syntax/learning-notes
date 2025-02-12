import requests
import hashlib
import os, re
import subprocess

class AppImageDownloader:
    
    def __init__(self):
        self.owner = None
        self.repo = None
        self.appimage_name = None
        
        self.load_info()
        
    def load_info(self):
        try:
            with open("appimage_info.txt", "r") as f:
                self.owner = f.readline().strip()
                self.repo = f.readline().strip()
                self.appimage_name = f.readline().strip()
        except FileNotFoundError:
            self.owner = input("GitHub repository owner: ")
            self.repo = input("GitHub repository name: ")
            self.get_appimage_name()
            self.save_info()
            
    def save_info(self):
        with open("appimage_info.txt", "w") as f:
            f.write(self.owner + "\n")
            f.write(self.repo + "\n")
            f.write(self.appimage_name + "\n")
            
    def get_appimage_name(self):
        appimage_list = self.get_appimage_list()
        
        if not appimage_list:
            print("No AppImage file found in the repository.")
            exit(1)
            
        if len(appimage_list) == 1:
            self.appimage_name = appimage_list[0]
        else:
            for i, name in enumerate(appimage_list):
                print(f"{i + 1}. {name}")
                
            choice = input("Which AppImage file do you want to download (Enter the number): ")
            try:
                choice = int(choice) - 1
                self.appimage_name = appimage_list[choice]
            except (ValueError, IndexError):
                print("Invalid input.")
                self.get_appimage_name()
                
        confirm = input(f"Do you want to download {self.appimage_name}? (Y/n): ")
        if confirm.lower() == "n":
            self.appimage_name = input("Enter the full name of the AppImage file: ")
            self.get_appimage_name()
            
        save = input("Do you want to save this information for future use? (Y/n): ")
        if save.lower() == "y":
            self.save_info()
            
    def get_appimage_list(self):
        # Get the list of AppImage files in the repository
        pass
    
    def download_appimage(self):
        # Download the selected AppImage file
        pass
    
    def verify_appimage(self):
        #
