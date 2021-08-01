import install_uefi as inu
import gnome as gn


def install():
    inu.system_clock("America", "Sao_Paulo")
    inu.locale("pt_BR.UTF-8", "br-abnt2")
    inu.host("archlinux")
    inu.create_user("user", "password")
    inu.install_packages()
    inu.install_grub()

    print(
        'Adicione os drivers da placa de vídeo no arquivo mkinitcpio.conf na parte escrita "modules"'
    )
    print('depois saia do chroot e antes de reiniciar use o comando "umount -a"')


def install_gui():
    h = "paru"

    gn.sync_clock()
    gn.firewall_conf()
    gn.install_aur_helper(h)
    gn.install_aur(h)
    gn.install_packages()
    gn.flatpak_install()
    gn.reboot()


resp = ""
print("O deseja fazer?")
print("1 - Instalar")
print("2 - Instalar Ambiente Gráfico")
resp = int(input())

if resp == 1:
    install()
elif resp == 2:
    install_gui()
