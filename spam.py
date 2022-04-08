# Author : Khoirul Anam

# Reccode : |2!¥απαDΔ

import requests, os

def logo():
  print("""
=========================================================
¦¦
¦¦   ===============================
¦¦   [ ♻ TOOLS SPAM SMS,WA,CALL ♻ ]
¦¦   ===============================
¦¦   =====================
¦¦   [ RECODE : |2!¥απαDΔ ✔ ]
¦¦   =====================
¦¦   =========================================
¦¦   [ Github : https://github.com/riyanid ✔ ]
¦¦   =========================================
¦¦    ======================
¦¦   [ YouTube : R1Y4N4D4 ✔ ]                           
¦¦   =======================                           
¦¦                                                        
==========================================================
""")

def menu():
  os.system('clear')
  logo()
  print("\nMasukan Nomer Di Awali (8xxx)")
  nomor = input("Nomer Target : 0")
  jum = int(input("Jumlah : "))
  for i in range(jum):
      req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if 'terkirim' in req:
           print("\nSpam Terkirim ✔ | By:|2!¥απαDΔ")
      else:
           print("\nKendala jaringan! Coba beberapa saat!")
           os.system('clear')

menu()
