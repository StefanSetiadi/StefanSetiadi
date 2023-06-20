import math
import statistics

# bykdata = int(input("Jumlah data : "))
# for i in range(bykdata):
#     bantu = int(input(f"Masukkan data ke-{i+1} : "))
#     data.append(bantu)

data = [20,16,51,22,32,60,23,15,30,30,41,17,35,33,28,40,25,31,31,26,42,20,24,30]
bykdata = len(data)

for i in range(bykdata):
    data[i] = data[i] + 4

data.sort()

def kuartil(data,bykdata,i):
    letak = i * (bykdata + 1)
    if((letak) % 4 == 0):
        letak = letak // 4
        letak = int(letak)
        hasil = data[letak - 1]
    else:
        letak = letak / 4
        pecahan = letak - (int(letak))
        letak = int(letak)
        hasil = data[letak-1] + (pecahan * (data[letak] - data[letak-1]))
    return hasil

def desil(data,bykdata,i):
    letak = i * (bykdata + 1)
    if((letak) % 10 == 0):
        letak = letak // 10
        letak = int(letak)
        hasil = data[letak - 1]
    else:
        letak = letak / 10
        pecahan = letak - (int(letak))
        letak = int(letak)
        hasil = data[letak-1] + (pecahan * (data[letak] - data[letak-1]))
    return hasil

def persentil(data,bykdata,i):
    letak = i * (bykdata + 1)
    if((letak) % 100 == 0):
        letak = letak // 100
        letak = int(letak)
        hasil = data[letak - 1]
    else:
        letak = letak / 100
        pecahan = letak - (int(letak))
        letak = int(letak)
        hasil = data[letak-1] + (pecahan * (data[letak] - data[letak-1]))
    return hasil
print("")
print(data)
print("Mean / Rata-rata : ",statistics.mean(data))
print("Median           : ",statistics.median(data))
print("Modus            : ",statistics.multimode(data))
print("Kuartil(1)       : ",kuartil(data, bykdata, 1))
print("Kuartil(2)       : ",kuartil(data, bykdata, 2))
print("Kuartil(3)       : ",kuartil(data, bykdata, 3))

var_desil = int(input("Masukkan desil ke-: "))
print(f"Desil ke-{var_desil}        : ",desil(data,bykdata,var_desil))

var_persentil = int(input("Masukkan persentil ke-: "))
print(f"Desil ke-{var_persentil}        : ",persentil(data,bykdata,var_persentil))

jarak = max(data) - min(data)
print("Nilai Tertinggi : ",max(data))
print("Nilai Terendah  : ",min(data))
print("Range : ",jarak)

jumlah_xi_x = 0
for i in range(bykdata):
    jumlah_xi_x = jumlah_xi_x + abs(data[i] - statistics.mean(data))
rataRataSimpangan = 1/bykdata * (jumlah_xi_x)
print("Rata-rata simpangan : ",rataRataSimpangan)

jumlah_xi_x2 = 0
for i in range(bykdata):
    jumlah_xi_x2 = jumlah_xi_x2 + ((data[i] - statistics.mean(data)) * (data[i] - statistics.mean(data)))
simpanganBaku = math.sqrt(jumlah_xi_x2/(bykdata-1))
print("Simpangan baku      : ",simpanganBaku)
