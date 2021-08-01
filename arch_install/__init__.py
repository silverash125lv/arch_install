import install_uefi as inu

def install():
    inu.system_clock("America", "Sao_Paulo")
    inu.locale("pt_BR.UTF-8", "br-abnt2")
    inu.host("archlinux")
    inu.create_user("user", "password")
    inu.install_packages()
    inu.install_grub()


install()


