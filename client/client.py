from ftplib import FTP
import os
import time
from termcolor import colored

if os.name != 'nt':
    from simple_term_menu import TerminalMenu
    clear_command = 'clear'
else:
    clear_command = 'cls'

def main():
    # for windows
    if os.name == 'nt':
        forWindows()

    # for mac and linux(here, os.name is 'posix')
    else:
        forMac()

def option0():
    flag = True
    while flag:
        print(colored(" Daha önce aynı isimde bulunan dosya varsa üzerine yazacağını unutmayınız! \n", 'yellow'))
        file_path = input("Yüklenecek dosyanın path'i: ") 
        directory_path = input("Dosyanın yüklenmesini istediğiniz klasör (Eğer hiçbir klasöre yüklemek istemiyorsanız boş bırakabilirsiniz.): ") 
        try:
            flag = False
            ftp.cwd(directory_path)   
            ftp.storbinary('STOR '+os.path.split(file_path)[1], open(file_path, 'rb'))
        except:
            flag = True
            print(colored("\n Dosya bulunamadı ya da belirtilen dizin daha önce oluşturulmadı! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    print(colored("\n Başarıyla yüklendi.", 'green'))
    ftp.cwd('..') 
    time.sleep(3)

def option1():
    flag = True
    while flag:
        print(colored(" Daha önce aynı isimde bulunan dosya varsa üzerine yazacağını unutmayınız! \n", 'yellow'))
        file_name = input("İndirilecek dosyanın adı: ")  
        directory_path = input("İndirilecek dosyanın bulunduğu klasör (Eğer ana klasördeyse boş bırakabilirsiniz.): ")
        try:
            flag = False
            ftp.cwd(directory_path)  
            download_file = open(file_name, 'wb')
            ftp.retrbinary('RETR ' + file_name, download_file.write, 1024)
            download_file.close()
        except:
            flag = True
            print(colored("\n Dosya bulunamadı ya da belirtilen dizin daha önce oluşturulmadı! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    print(colored("\n Başarıyla indirildi.", 'green'))
    ftp.cwd('..') 
    time.sleep(3)

def option2():
    flag = True
    while flag:
        directory_name = input("Oluşturulacak dizinin adı: ")
        try:
            flag = False
            ftp.mkd(directory_name)
        except:
            flag = True
            print(colored("\n Bu dizin daha önce zaten oluşturuldu! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    print(colored("\n Başarıyla oluşturuldu.", 'green'))
    time.sleep(3)

def option3():
    flag = True
    while flag:
        directory_name = input("Silinecek dizinin adı: ")
        try:
            flag = False
            ftp.cwd(directory_name)
            for file_name in ftp.nlst():
                ftp.delete(file_name) 
            ftp.cwd('..')
            ftp.rmd(directory_name)
        except:
            flag = True
            print(colored("\n Böyle bir dizin bulunamadı! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    print(colored("\n Başarıyla silindi.", 'green'))
    time.sleep(3)

def option4():
    flag = True
    while flag:
        directory_name = input("Silinecek dosyanın bulunduğu klasör (Eğer ana klasördeyse boş bırakabilirsiniz.): ")
        file_name = input("Silinecek dosyanın adı: ")
        try:
            flag = False
            ftp.cwd(directory_name)
            ftp.delete(file_name)
        except:
            flag = True
            print(colored("\n Dosya bulunamadı ya da belirtilen dizin daha önce oluşturulmadı! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    print(colored("\n Başarıyla silindi.", 'green'))
    ftp.cwd('..') 
    time.sleep(3)

def option5():
    flag = True
    while flag:
        directory_path = input("Değiştirilecek dosyanın bulunduğu klasör (Eğer ana klasördeyse boş bırakabilirsiniz.): ")
        old_file_name = input("Değiştirilecek dosyanın adı: ")
        new_file_name = input("Dosyanın yeni adı: ")
        try:
            flag = False
            ftp.cwd(directory_path)  
            ftp.rename(old_file_name,new_file_name)
        except:
            flag = True
            print(colored("\n Dosya bulunamadı ya da belirtilen dizin daha önce oluşturulmadı! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    print(colored("\n Başarıyla değiştirildi.", 'green'))
    ftp.cwd('..') 
    time.sleep(3)

def option6():
    ftp.dir()
    input("\nMenüye dönmek için enter'a basınız.")

def option7():
    ftp.quit()
    print(colored("Sunucu bağlantısı başarıyla sonlandırıldı.", 'green'))

def forMac():
    main_menu_items = ["Dosya Yükleme", "Dosya İndirme", "Dizin Oluşturma", "Dizin Silme", "Dosya Silme", "Dosya Adı Değiştirme", "Dizin ve Dosya Listeleme", "Çıkış"]
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            option0()
        elif main_sel == 1:
            option1()
        elif main_sel == 2:
            option2()
        elif main_sel == 3:
            option3()
        elif main_sel == 4:
            option4()
        elif main_sel == 5:
            option5()
        elif main_sel == 6:
            option6()  
        elif main_sel == 7 or main_sel == None:
            main_menu_exit = True
            option7()

def forWindows():
    while(True):
        menu_options = {
        0: 'Dosya Yükleme',
        1: 'Dosya İndirme',
        2: 'Dizin Oluşturma',
        3: 'Dizin Silme',
        4: 'Dosya Silme',
        5: 'Dosya Adı Değiştirme',
        6: 'Dizin ve Dosya Listeleme',
        7: 'Çıkış'
        }
        
        for key in menu_options.keys():
            print(key, ') ', menu_options[key] )
        option = int(input('\nYapmak istediğiniz işlemi seçiniz: '))

        if option == 0:
            os.system('cls')
            option0()
            os.system('cls')
        elif option == 1:
            os.system('cls')
            option1()
            os.system('cls')
        elif option == 2:
            os.system('cls')
            option2()
            os.system('cls')
        elif option == 3:
            os.system('cls')
            option3()
            os.system('cls')
        elif option == 4:
            os.system('cls')
            option4()
            os.system('cls')
        elif option == 5:
            os.system('cls')
            option5()
            os.system('cls')
        elif option == 6:
            os.system('cls')
            option6()
            os.system('cls')
        elif option == 7:
            os.system('cls')
            option7()
            exit()
        else:
            print(colored("\n Geçersiz seçenek! \n", 'red'))
            input("Devam etmek için enter'a basınız.")

if __name__ == "__main__":
    os.system(clear_command)
    flag = True
    while flag:
        print("FTP sunucusuna bağlanmak için ip adresini ve portunu giriniz. \n")
        ip_address = input("Sunucunun ip adresi: ")
        port = input("Sunucunun portu: ")
        ftp = FTP('')
        try:
            flag = False
            ftp.connect(ip_address,int(port))
        except:
            os.system(clear_command)
            flag = True
            print(colored("Bağlantı reddedildi.! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)

    os.system(clear_command)
    print(colored("Sunucuya başarıyla bağlanıldı! \n", 'green'))
    print("3 saniye sonra giriş ekranı gelecektir...")
    # time.sleep(3)
    os.system(clear_command)


    flag = True
    while flag:
        print("FTP sunucusuna giriş yapmak için kullanıcı adınızı ve şifrenizi giriniz. \n")
        user_name = input("Kullanıcı adınız: ")
        user_pass = input("Şifreniz: ")
        try:
            flag = False
            ftp.login(user_name,user_pass)
        except:
            os.system(clear_command)
            flag = True
            print(colored("Kullanıcı adı veya şifre hatalı! \n", 'red'))
            input("Lütfen yeniden denemek için enter'a basınız.")
            os.system(clear_command)
    
    os.system(clear_command)
    print(colored("Sunucuya başarıyla giriş yapıldı! \n", 'green'))
    print("3 saniye sonra menü ekranı gelecektir...")
    # time.sleep(3)
    os.system(clear_command)

    main()