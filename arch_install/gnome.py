from modulefinder import packagePathMap
import os
from time import sleep 

def sync_clock():
    os.system("echo 'sudo timedatectl set-ntp true'")
    os.system("echo 'sudo hwclock --systohc'")

def firewall_conf():
    ports = ["1025-65535/tcp", "1025-65535/udp"]
    for p in ports:
        os.system(f"echo 'sudo firewall-cmd --add-port={p} --permanent'")

    os.system(f"echo 'sudo firewall-cmd --reload'")
    

def install_aur_helper(helper: str):
    os.system("echo 'cd /tmp'")
    os.system(f"'echo git clone https://aur.archlinux.org/{helper}.git'")
    os.system(f"echo 'cd {helper/}'")
    os.system("echo 'makepkg -si'")

def install_packages():
    packs = [
        "gdm gnome gnome-extra gnome-tweaks simplescreenrecorder arc-gtk-theme arc-icon-theme",
        "obs-studio vlc dina-font tamsyn-font bdf-unifont ttf-bitstream-vera",
        "ttf-croscore ttf-dejavu ttf-droid gnu-free-fonts ttf-ibm-plex ttf-liberation ttf-linux-libertine noto-fonts ttf-roboto", 
        "tex-gyre-fonts ttf-ubuntu-font-family ttf-anonymous-pro ttf-cascadia-code ttf-fantasque-sans-mono ttf-fira-mono ttf-hack", 
        "ttf-fira-code ttf-inconsolata ttf-jetbrains-mono ttf-monofur adobe-source-code-pro-fonts cantarell-fonts inter-font ttf-opensans", 
        "gentium-plus-font ttf-junicode adobe-source-han-sans-otc-fonts adobe-source-han-serif-otc-fonts noto-fonts-cjk noto-fonts-emoji",
        "pavucontrol"
    ]

    for p in packs:
        os.system(f"echo 'sudo pacman -S {p}'")

    services = ["gdm"]

    for s in services:
        os.system(f"echo 'sudo systemctl enable {s}'")

    
def flatpak_install():
    packages = [
        "org.videolan.VLC",
        "com.github.wwmm.pulseeffects",
        "org.onlyoffice.desktopeditors",
        "org.kde.kdenlive",
        "com.spotify.Client",
        "org.mozilla.firefox"
    ]

    for p in packages:
        os.system(f"echo 'flatpak install flathub {p}'")

    
def install_aur(helper):
    packages = [
        "zramd",
        "snapd",
        "snapd-glib",
        "timeshift"
    ]

    for p in packages:
        os.system(f"echo '{helper} -S {p}'")


def reboot():
    resp = input("Deseja reiniciar? [Y/N] ")

    if resp in "Ss":
        for c in range(1, 5):
            print(f"{c}")
            sleep(1)
        print("Reiniciando...")
        os.system("echo 'reboot'")

