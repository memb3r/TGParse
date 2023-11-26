# pip install telethon
from telethon.sync import TelegramClient
import csv
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

print('''\u001b[34m
  ________________                     
 /_  __/ ____/ __ \_\u001b[37mRegistration\u001b[34m___ __
  / / / / __/ /_/ / __ `/ ___/ ___/ _ |
 / / / /_/ / ____/ /_/ / /  (__  )  __/
/_/  \____/_/    \__,_/_/  /____/\___/ \u001b[37m1.0.0
                                       
''')

api_id = 0 # Enter your values. Example - 12345678
api_hash = '' # Enter your values. Example - a12b345c6d789efg01h2ij3456kl789mn
phone = '' # Enter your values. Example - 79998887766

client = TelegramClient(phone, api_id, api_hash)

client.start()

chats = []
last_date = None
size_chats = 200
groups=[]

result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=size_chats,
            hash = 0
        ))
chats.extend(result.chats)

for chat in chats:
   try:
       if chat.megagroup== True:
           groups.append(chat)
   except:
       continue

print('''\u001b[34m
  ________________                     
 /_  __/ ____/ __ \_\u001b[37mBy memb3r\u001b[34m______ __
  / / / / __/ /_/ / __ `/ ___/ ___/ _ |
 / / / /_/ / ____/ /_/ / /  (__  )  __/
/_/  \____/_/    \__,_/_/  /____/\___/ \u001b[37m1.0.0
                                       
''')

print('\u001b[34m[+] \u001b[37mChoose group: ')
i=0
for g in groups:
   print(str(i) + ' - ' + g.title)
   i+=1

g_index = input("\u001b[34m[+] \u001b[37mEnter group number: ")
target_group=groups[int(g_index)]

print('\u001b[34m[+] \u001b[37mChecking group...')
all_participants = []
all_participants = client.get_participants(target_group)

print('\u001b[34m[+] \u001b[37mSaving members of this group into csv file...')
with open("parse.csv","w",encoding='UTF-8') as f:
   writer = csv.writer(f,delimiter=",",lineterminator="\n")
   writer.writerow(['username','name','group'])
   for user in all_participants:
       if user.username:
           username= user.username
       else:
           username= ""
       if user.first_name:
           first_name= user.first_name
       else:
           first_name= ""
       if user.last_name:
           last_name= user.last_name
       else:
           last_name= ""
       name= (first_name + ' ' + last_name).strip()
       writer.writerow([username,name,target_group.title])     
print('\u001b[34m[!] \u001b[37mSuccess!.')