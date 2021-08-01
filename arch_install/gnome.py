import os 

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


