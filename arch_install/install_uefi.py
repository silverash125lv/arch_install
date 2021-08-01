import os


def system_clock(zone: str, city: str):
    os.system(f"echo 'ln -sf /usr/share/zoneinfo/{zone}/{city} /etc/localtime'")
    os.system(f"echo 'hwclock --systohc'")


def locale(lang: str, keyboard: str):
    os.system("echo 'locale-gen'")
    with open("./etc/locale.conf", "w") as f:
        f.write(f'LANG="{lang}"')
    with open("./etc/vconsole.conf", "w") as f:
        f.write(f'KEYMAP="{keyboard}"')


def host(name: str):
    with open("./etc/hostname", "w") as f:
        f.write(f"{name}")

    with open("./etc/hosts", "w") as f:
        f.write("127.0.0.1\tlocalhost.localdomain\tlocalhost\n")
        f.write("::1\t\t\tlocalhost.localdomain\tlocalhost\n")
        f.write(f"127.0.1.1\t{name}.localdomain\t{name}\n")


def create_user(username: str, password: str, shell="bash"):

    username = username.lower()
    os.system(f"echo 'echo root:{password} | chpasswd'")
    os.system(f"echo 'useradd -m --shell=/usr/bin/{shell} {username}'")
    os.system(f"echo 'echo {username}:{password} | chpasswd'")

    with open(f"./etc/sudoers.d/{username}", "w") as f:
        f.write(f"{username} ALL=(ALL) ALL")


def install_packages():
    pm = "pacman -S"
    os.system(
        f"echo '{pm} grub efibootmgr networkmanager network-manager-applet dialog wpa_supplicant mtools dosfstools'"
    )
    os.system(
        f"echo '{pm} reflector base-devel linux-headers avahi xdg-user-dirs xdg-utils gvfs gvfs-smb nfs-utils'"
    )
    os.system(f"echo '{pm} inetutils dnsutils bluez bluez-utils cups hplip'")
    os.system(
        f"echo '{pm} alsa-utils pipewire pipewire-alsa pipewire-pulse pipewire-jack bash-completion openssh rsync'"
    )
    os.system(
        f"echo '{pm} reflector acpi acpi_call tlp tlp-rdw virt-manager qemu qemu-arch-extra edk2-ovmf bridge-utils'"
    )
    os.system(
        f"echo '{pm} dnsmasq vde2 openbsd-netcat iptables-nft ipset firewalld flatpak sof-firmware nss-mdns acpid os-prober ntfs-3g terminus-font'"
    )
    os.system(f"echo '{pm} xf86-video-amdgpu neovim emacs micro'")

    font = "noto-fonts"
    os.system(
        f"echo '{pm} ttf-dejavu ttf-droid ttf-ibm-plex ttf-roboto ttf-liberation ttf-ubuntu-font-family ttf-jetbrains-mono ttf-inconsolata ttf-hack ttf-fira-code otf-fira-mono ttf-fira-mono ttf-cascadia-code ttf-anonymous-pro {font} {font}-cjk {font}-emoji {font}-extra'"
    )

    os.system("echo 'systemctl enable NetworkManager'")
    os.system("echo 'systemctl enable bluetooth'")
    os.system("echo 'systemctl enable cups.service'")
    os.system("echo 'systemctl enable sshd'")
    os.system("echo 'systemctl enable avahi-daemon'")
    os.system("echo 'systemctl enable tlp'")
    os.system("echo 'systemctl enable reflector.timer'")
    os.system("echo 'systemctl enable fstrim.timer'")
    os.system("echo 'systemctl enable libvirtd'")
    os.system("echo 'systemctl enable firewalld'")
    os.system("echo 'systemctl enable acpid'")


def install_grub(target="x86_64-efi", dir="/boot/efi", boot_id="GRUB"):
    os.system(
        "echo 'grub-install --target={target} --efi-directory={dir} --bootloader-id={boot_id}'"
    )
