import os 

def sync_clock():
    os.system("echo 'sudo timedatectl set-ntp true'")
    os.system("echo 'sudo hwclock --systohc'")
    


