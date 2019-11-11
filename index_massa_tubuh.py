weight = int(input('masukkan berat (KG): '))
height_cm = int(input('masukkan tinggi (CM): '))
height_m = height_cm/10
imt = weight / (height_m**2)*100
if imt < 18.5:
    print(imt)
    print('Berat badan Anda kurang.')
elif imt >= 18.5 and imt <=24.9:
    print(imt)
    print('Berat badan Anda ideal.')
elif imt >= 25.0 and imt <= 29.9:
    print(imt)
    print('Berat badan Anda berlebih!')
elif imt >= 30.0 and imt <= 39.9:
    print(imt)
    print('Berat badan Anda sangat berlebih')
else:
    print(imt)
    print('Anda obesitas!')