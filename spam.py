# Author : Khoirul Anam

# Reccode : |2!¥απαDΔ

import requests, os

def logo():
  print("""
   ==========================
   [ ♻ TOOLS SPAM CHT WA ♻ ]
   ==========================
   =====================
   [ Author : |2!¥απαDΔ✔ ]
   =====================
   =================================
   [ Github : https://github.com/riyanid✔ ]
   =================================
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
           print("\nSpam Terkirim")
      else:
           print("\nSpam Gagal")
           os.system('clear')

menu()
