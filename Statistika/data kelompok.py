import math

# Percobaan Pertama (Latihan power point) data buat sendiri
# ListData = [23,60,79,32,57,74,52,70,82,36,80,77,81,95,41,65,92,85,55,76,52,10,64,75,78,25,80,98,81,67,41,71,83,54,64,72,88,62,74,43,60,78,89,76,84,48,84,90,15,79,34,67,17,82,69,74,63,80,85,61]
# skalaTerkecil = 1

# Percobaan Kedua (tugas 2)
# ListData = [170.2,172.5,180.4,172.1,159.3,168.6,168.9,172.3,174.4,159.5,170.0,161.5,172.1,170.7,168.9,168.4,177.4,174.5,186.4,164.6,170.6,168.5,164.3,167.3,167.5,165.8,166.8,167.9,173.6,170.3,167.4,160.5,169.2,166.6,172.1]
# skalaTerkecil = 0.1


# Percobaan Ketiga
# ListData = [254.25,256.55,264.45,256.15,243.35,252.65,252.95,256.35,258.45,243.55,254.05,245.55,256.15,254.75,252.95,252.45,261.45,258.55,270.45,248.65,254.65,252.55,248.35,251.35,251.55,249.85,250.85,251.95,257.65,254.35,251.45,244.55,253.25,250.65,256.15]
ListData = [41.47, 55.33, 49.40, 43.64, 51.70, 62.61, 42.77, 61.66, 39.51, 45.19, 57.99, 51.38, 47.81, 48.39, 38.18, 57.88, 47.69, 35.65, 59.90, 48.41, 34.51, 61.52, 43.52, 43.63, 40.13, 57.53, 44.55, 46.30, 42.15, 38.57, 45.12, 47.24, 55.20, 51.89, 35.95]
skalaTerkecil = 0.01


BanyakData = len(ListData)
for i in range(BanyakData):
    ListData[i] = ListData[i] + 4


maks = ListData[0]
min = ListData[0]
for i in range(BanyakData-1):
    if(ListData[i+1] > maks):
        maks = ListData[i+1]
    if(ListData[i+1] < min):
        min = ListData[i+1]
jangkauan = round(maks - min,2)
jumlahKelas = 1 + (3.3 * math.log10(BanyakData))
jumlahKelas = int(jumlahKelas)
jumlahKelas = int(input(f"Pilih jumlah kelas ({jumlahKelas}/{jumlahKelas+1}) : "))
interval = jangkauan / jumlahKelas

interval = int(interval) + 1

# menentukan LCL, UCL, LCB, UCB
ListLCL = []
ListUCL = []
ListLCB = []
ListUCB = []

bantu = min
for i in range(jumlahKelas):
    ListLCL.append(bantu)
    ListUCL.append(bantu+(interval-skalaTerkecil))
    ListLCB.append(ListLCL[i] - (0.5 * skalaTerkecil))
    ListUCB.append(ListUCL[i] + (0.5 * skalaTerkecil))
    bantu = bantu + interval

# menentukan fi dan Fk
ListFi = []
ListFk = []
urutanList = 0
jumlahFk = 0
for i in range(jumlahKelas):
    jumlahFi = 0
    for i in range(BanyakData):
        if((ListData[i] >= ListLCL[urutanList]) and (ListData[i] <= ListUCL[urutanList])):
            jumlahFi = jumlahFi + 1
    urutanList = urutanList + 1
    ListFi.append(jumlahFi)
    jumlahFk = jumlahFk + jumlahFi
    ListFk.append(jumlahFk)

# menentukan CM dam fi.CM
ListCM = []
ListFiCM = []
for i in range(jumlahKelas):
    CM = 0.5 * (ListLCL[i] + ListUCL[i])
    ListCM.append(CM)

    bantuFiCM = ListFi[i] * ListCM[i]
    ListFiCM.append(bantuFiCM)


jumlahFiCM = 0
jumlahFi = 0
for i in range(jumlahKelas):
    jumlahFiCM = jumlahFiCM + ListFiCM[i]
    jumlahFi = jumlahFi + ListFi[i]

print("Maksimal  : ",maks)
print("Minimal   : ",min)
print("Jangkauan : ",jangkauan)
print("Interval  : ",interval)

# menghitung rata-rata
x = round(jumlahFiCM / jumlahFi,2)
print("-----------------------------------------------")
print("Rata-rata : ",x)

# menghitung median
letakMedian = BanyakData / 2
letakIntervalMedian = 0
i = 0
ketemu = False
while((i <= jumlahKelas) and (ketemu is False)):
    if(ListFk[i] > letakMedian):
        ketemu = True
        letakIntervalMedian = i
    i = i + 1
print("-----------------------------------------------")
print("Letak Median   : ",letakMedian)
print("Letak Interval : ",letakIntervalMedian+1)
median = ListLCB[letakIntervalMedian] + ((letakMedian - ListFk[letakIntervalMedian-1])/ListFi[letakIntervalMedian]) * interval
print("Median         : ",median)

# menghitung median
letakIntervalModus = 0
maksModus = 0
for i in range(jumlahKelas):
    if(ListFi[i] > maksModus):
        letakIntervalModus = i
        maksModus = ListFi[i]
print("-----------------------------------------------")
print("Fi modus       : ",maksModus)
print("Letak Interval : ",letakIntervalModus+1)
f1mod = ListFi[letakIntervalModus] - ListFi[letakIntervalModus - 1]
f2mod = ListFi[letakIntervalModus] - ListFi[letakIntervalModus + 1]
modus = ListLCB[letakIntervalModus] + (f1mod/(f1mod + f2mod)) * interval

print("f1 mod : ",f1mod)
print("f2 mod : ",f2mod)
print("Modus         : ",modus)


print("-----------------------------------------------")
print("Rumus Pearson")
K = x - modus
if(K > 0 ):
    print("Positive skew (ekor bagian kanan lebih panjang)")
elif(K < 0):
    print("Negative skew (ekor bagian kiri lebih panjang)")
else:
    print("Kurva normal")


# membuat CM-X , (CM-X)^2, dan fi.(CM-X)^2
ListCM_X = []
ListCM_X2 = []
ListFiCM_X2 = []
for i in range(jumlahKelas):
    CM_X = ListCM[i] - x
    CM_X2 = CM_X * CM_X
    FiCM_X2 = ListFi[i] * CM_X2
    ListCM_X.append(CM_X)
    ListCM_X2.append(CM_X2)
    ListFiCM_X2.append(FiCM_X2)

jumlahFiCM_X2 = 0
for i in range(jumlahKelas):
    jumlahFiCM_X2 = jumlahFiCM_X2 + ListFiCM_X2[i]

# membuat simpangan baku / standar deviasi
standarDeviasi = math.sqrt((jumlahFiCM_X2)/BanyakData)
print("-----------------------------------------------")
print("Standar Deviasi : ",standarDeviasi)


#rumus Momen
jumlahFiCM_X4 = 0
for i in range(jumlahKelas):
    jumlahFiCM_X4 = jumlahFiCM_X4 + (ListFi[i] * (ListCM_X2[i] * ListCM_X2[i]))
koefisienKemencengan = (1/(BanyakData * (standarDeviasi * standarDeviasi * standarDeviasi * standarDeviasi))) * jumlahFiCM_X4

print("-----------------------------------------------")
print("Koefisien Kemencengan : ",koefisienKemencengan)
print("-----------------------------------------------")
print("")


# Membuat tampilan tabel untuk data kelompok
spasiInterval = 20
spasiFi,spasiFk = 5,5
spasiLCL,spasiUCL,spasiLCB,spasiUCB,spasiCM = 8,8,8,8,8
spasiFiCM = 12
spasiCM_X = 8
spasiCM_X2 = 12
spasiFiCM_X2 = 14


jumlahSpasi = spasiInterval + spasiFi + spasiFk + spasiLCL + spasiUCL + spasiLCB + spasiUCB + spasiCM + spasiFiCM +spasiCM_X + spasiCM_X2 + spasiFiCM_X2 + 13
print("-"*jumlahSpasi)
print(f"|{'Interval':^{spasiInterval}}|{'fi':^{spasiFi}}|{'Fk':^{spasiFk}}|{'LCL':^{spasiLCL}}|{'UCL':^{spasiUCL}}|{'LCB':^{spasiLCB}}|{'UCB':^{spasiUCB}}|{'CM':^{spasiCM}}|{'fi.CM':^{spasiFiCM}}|{'CM-X':^{spasiCM_X}}|{'(CM-X)^2':^{spasiCM_X2}}|{'f.(CM-X)^2':^{spasiFiCM_X2}}|")
print("-"*jumlahSpasi)
for i in range(jumlahKelas):
    LCL = "{:.3f}".format(ListLCL[i])
    UCL = "{:.3f}".format(ListUCL[i])
    LCB = "{:.3f}".format(ListLCB[i])
    UCB = "{:.3f}".format(ListUCB[i])
    CM = "{:.3f}".format(ListCM[i])
    FiCM = "{:.3f}".format(ListFiCM[i])
    CM_X = "{:.3f}".format(ListCM_X[i])
    CM_X2 = "{:.3f}".format(ListCM_X2[i])
    FiCM_X2 = "{:.3f}".format(ListFiCM_X2[i])
    print(f"|{LCL:^{int((spasiInterval-2)/2)}} -{UCL:^{int((spasiInterval-2)/2)}}|{ListFi[i]:^{spasiFi}}|{ListFk[i]:^{spasiFk}}|{LCL:^{spasiLCL}}|{UCL:^{spasiUCL}}|{LCB:^{spasiLCB}}|{UCB:^{spasiUCB}}|{CM:^{spasiCM}}|{FiCM:^{spasiFiCM}}|{CM_X:^{spasiCM_X}}|{CM_X2:^{spasiCM_X2}}|{FiCM_X2:^{spasiFiCM_X2}}|",end="")
    print("")
print("-"*jumlahSpasi)
print("jumlah fi         : ",jumlahFi)
print("jumlah Fi.CM      : ",jumlahFiCM)
print("jumlah f.(CM-X)^2 : ",jumlahFiCM_X2)
print("jumlah f.(CM-X)^4 : ",jumlahFiCM_X4)