import csv

ids_ignore = """
2319
2325
2326
2327
2328
4388
6241
6246
6263
7156
7406
7424
7430
10848
10852
10866
10917
11203
11209
11228
11262
13100
"""
rows_string = """
44
64
308-311
313-325
327-328
376-377
380
385
391
393
395
400
414
430-432
537
558
762
770
772
790
793
813
838
904
972
973
1053
1179
1183
1206-1210
1215
1216
1218
1219
1223
1233
1243
1244
1784
1846
1847
1850
1851
1959
1962
2006
2012
2119
2149
2163
2168
2453-2457
2464
2472
2482
2483
2540
2578
2662
2665-2667
2685
2858
2884
2890
2899
2917
2924
2926
2986
2993
3017
3063
3067
3076
3081
3132
3143
3162-3164
3170
3177
3180
3271
3306
3307
3338
3352
3353
3370
3375-3378
3391-3399
3420
3559
3564
3572
3582
3617
3619
3622
3630
3639-3646
3648
"""

# Функция для преобразования строки в список номеров строк


def parse_rows(rows_string):
    rows = []
    for part in rows_string.strip().split('\n'):
        if '-' in part:
            start, end = map(int, part.split('-'))
            rows.extend(list(range(start, end + 1)))
        else:
            rows.append(int(part))
    return rows


# Получаем список всех нужных строк
rows_needed = parse_rows(rows_string)
ids_to_ignore = parse_rows(ids_ignore)
print(ids_to_ignore)

# Открываем исходный CSV-файл и новый файл для записи
with open('source.csv', 'r', newline='') as source_file, open('filtered.csv', 'w', newline='') as filtered_file:
    reader = csv.reader(source_file)
    writer = csv.writer(filtered_file)

    # Счетчик строк для определения, какую строку читаем
    row_number = 0

    # Читаем каждую строку в исходном файле
    for row in reader:
        row_number += 1

        if row_number > 1 and int(row[1]) in ids_to_ignore:
            print(row)
            print()
            print()
            continue
        # Если номер текущей строки в списке нужных строк, записываем ее в новый файл
        if row_number in rows_needed:
            writer.writerow(row)

print("Фильтрация строк завершена. Проверьте файл 'filtered.csv'.")
