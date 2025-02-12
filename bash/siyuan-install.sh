#!/bin/bash
# !, Not working. If you have time to handle, use python to convert bash instead of using this but It can be good to learn
# !, handling this manual error solving :)
# If you use .desktop.
# Get the version of the latest release
version=$(curl -s https://api.github.com/repos/siyuan-note/siyuan/releases/latest | jq -r '.tag_name')
version=${version#v}  # remove the 'v' character from the version number


# Download the SHA256SUMS.txt file
echo "Starting siyuan installation..."
echo "SHA256SUMS.txt file installing..."

if url=$(curl -s https://api.github.com/repos/siyuan-note/siyuan/releases/latest | jq -r '.assets[] | select(.name=="SHA256SUMS.txt") | .browser_download_url')
 wget -q -O SHA256SUMS.txt $url; then
	echo "SHA256SUMS.txt installed..."
else
	echo "ERROR: SHA256SUMS.txt can't installed!"
	exit 1
fi

# Download the appimage file
echo "Siyuan appimage installing..."

if url=$(curl -s https://api.github.com/repos/siyuan-note/siyuan/releases/latest | jq -r '.assets[] | select(.name | endswith(".AppImage")) | .browser_download_url')
 wget -q -O siyuan-$version-linux.AppImage $url; then
	echo "Siyuan appimage installed succefully."
else
	echo "ERROR: Siyuan appimage can't installed!"
	exit 1
fi

# Verify the sha256sum of the appimage file
echo "Verifying file..."
sha256sum -c SHA256SUMS.txt
if "siyuan-$version-linux.AppImage: OK"; then
	mv siyuan-$version-linux.AppImage siyuan.AppImage
    echo "SHA256SUMS.txt verified successfully"
else
    echo "Error: SHA256SUMS.txt verification failed!"
    exit 1
fi

# Make the appimage file executable
chmod +x siyuan.appimage

# Move the appimage file to the desired location
mv siyuan.appimage ~/Documents/appimages/

# Remove the SHA256SUMS.txt file
echo "SHA256SUMS.txt deleting..."
rm SHA256SUMS.txt

echo -e "\033[1;32mSuccessfully installed siyuan\033[0m"
