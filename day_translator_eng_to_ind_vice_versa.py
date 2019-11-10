days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday', 'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday',
    'ahad': 'sunday'
}
days
## ---------------------- LONG CODE VERSION ----------------------

# inggris - indonesia
# engind = input('Masukan bahasa: ').lower()
# day = input('Masukkan nama hari: ').lower()

# if engind == 'indonesia':
#     if day in days.values():
#         print('itu bahasa Inggris')
#     else:
#         day_translate = days.get(day, 'Not Found!')
#         print(f'Bahasa Inggris dari {day.upper()} adalah {day_translate.upper()}')
    
# elif engind == 'inggris':
#     days_item_list = list(days.items())
#     if day in days_item_list[0]:
#         index = days_item_list[0].index(day)
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:
#             hari = days_item_list[0][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     elif day in days_item_list[1]:
#         index = days_item_list[1].index(day)
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:
#             hari = days_item_list[1][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     elif day in days_item_list[2]:
#         index = days_item_list[2].index(day)
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:
#             hari = days_item_list[2][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     elif day in days_item_list[3]:
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:
#             index = days_item_list[3].index(day)
#             hari = days_item_list[3][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     elif day in days_item_list[4]:
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:
#             index = days_item_list[4].index(day)
#             hari = days_item_list[4][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     elif day in days_item_list[5]:
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:    
#             index = days_item_list[5].index(day)
#             hari = days_item_list[5][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     elif day in days_item_list[6]:
#         if index == 0:
#             print('itu bahasa Indonesia')
#         else:    
#             index = days_item_list[6].index(day)
#             hari = days_item_list[6][index-1]
#             print(f'Bahasa Indonesia dari {day.upper()} adalah {hari.upper()}')
#     else:
#         print(f'Bahasa Indonesia dari {day.upper()} adalah NGGA ADA HARI GITUAN, WOY!')

# --------------- CODE IF YANG BERHASIL YANG SIMPLE ---------------
hari_list = list(days)
days_list = list(days.values())
x = input('Ketik nama hari (ENG/INA): ').lower()

if x in hari_list:
    day = days_list[hari_list.index(x)]
    print(f'Bahasa Inggris {x} adalah {day}')
else:
    hari = hari_list[days_list.index(x)]
    print(f'Bahasa Indonesia {x} adalah {hari}')

# --------------- CODE FOR YANG BERHASIL ---------------
# for ind, eng in days.items():
#     if day == eng:
#         print(f'Bahasa Indonesia dari {day.upper()} adalah {ind.upper()}')