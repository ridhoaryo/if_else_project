days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday', 'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday',
    'ahad': 'sunday'
}
days
day = input('Masukkan nama hari: ').lower()
day_translate = days.get(day, 'Not Found!')
print(f'Bahasa Inggris dari {day.upper()} adalah {day_translate.upper()}')