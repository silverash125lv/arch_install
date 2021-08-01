import install_uefi as inu


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


resp = ""
print("O deseja fazer?")
print("1 - Instalar")
resp = int(input())

if resp == 1:
    install()
