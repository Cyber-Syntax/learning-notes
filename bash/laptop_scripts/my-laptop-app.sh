#!/bin/usr/env bash

# sh script to install my apps

packages=(
# Essentials 
acpi # for battery status and my custom battery-warn.sh script
smartmontools #* Install smartmontools for disk drive health info
fwupd
#* Install ethtool to disable Wake-on-LAN
ethtool
# pacman -Qqet to get all installed packages
xorg-xinit
xorg # for all xorg packages
acpilight # for brightness control, also xbacklight
#rxvt-unicode # I don't thing this necessary
xterm
gtk4
base
base-devel
fuse2
grub
htop
linux-headers  
r8168 # for realtek ethernet
iwd # fallback for wifi
networkmanager # for ethernet and wifi
rofi
#terminator # I don't thing this necessary
sh
rsync
zsync # for zsync files similar to rsync
cronie # for cron jobs, also anacron
# Dark mode 
materia-gtk-theme
lxappearance
# gpu
# xf86-video-intel # Gen2 to Gen 9, cause issue on above gens
# mesa-amber # gen2 to gen 11
mesa # extra-testing for 12th and above gen
mesa-utils

intel-gpu-tools # similar to nvidia-smi
lib32-mesa # multilib-testing for 12th and above gen

# these are for old gpus
# xf86-video-fbdev # this is used for old gpus
# xf86-video-qxl # this is used for virtual machines
# xf86-video-vesa # this is used for old gpus
#
#git,seahorse etc.
gnome-keyring
git
wget
curl
unzip
# audio
pipewire
pipewire-pulse
rtkit # for pipewire
# audio manager
pavucontrol
# TODO: need to find which one is needed
alsa-utils 
alsa-firmware 
#alsa-lib 
#alsa-oss

# misc
fastfetch
xdg-user-dirs

## Fonts
#nerd-fonts # all nerd fonts
ttf-jetbrains-mono-nerd
ttf-roboto-mono       # Good for notes
#ttf-roboto-mono-nerd #
noto-fonts # fix fonts issues on some apps
#noto-fonts-emoji  # noto-fonts already includes emojis
# window manager
qtile
python-dbus-next
python-psutil # for memory widget on qtile
python-pip # pip for python
picom
playerctl
feh
dunst
#swaybg # for wayland
#lxpolkit # fedora only
polkit # for arch

# firewall
ufw

# terminal
kitty
zsh
zsh-autosuggestions
zsh-syntax-highlighting
# screenshot
# TODO: is it needed for flameshot?
xclip

# file manager
pcmanfm

# web browser
#firefox
openh264
ffmpeg
ffmpeg-libs
#ungoogled-chromium # if needed
#librewolf # maybe later

#password manager
keepassxc

# text editor
neovim
vim

# virtualization
#virt-manager
#libvirt

# blue light filter
gammastep

# sync
syncthing

# backup
#backintime # fedora only
# backintime in aur maybe creating rsync is better
borgbackup
)

#yay
yay_packages=(
#btrfs-assistant
#snapper-support 
thinkfan
)

# pacman install packages
for package in ${packages[@]}; do
  echo "Installing $package"
  # error handling
  if ! sudo pacman -S --noconfirm --needed $package; then
    echo "Error installing $package"
  else
    echo "$package installed"
  fi
done

#TODO: Debug this
# # yay package installation
# git clone https://aur.archlinux.org/yay.git
# cd yay
# makepkg -si

# yay install packages
for yay_package in ${yay_packages[@]}; do
  echo "Installing $yay_package"
  # error handling
  if ! yay -S --noconfirm --needed $yay_package; then
    echo "Error installing $yay_package"
  else
    echo "$yay_package installed"
  fi
done
