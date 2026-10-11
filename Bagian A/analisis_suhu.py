def baca_data_suhu(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                bagian = baris.strip().split(";")
                if len(bagian) != 2:
                    continue
                try:
                    data.append({"hari": bagian[0], "suhu": float(bagian[1])})
                except ValueError:
                    print("Baris dilewati:", baris.strip())
    except FileNotFoundError:
        print("Error: file", nama_file, "tidak ditemukan")
    return data


def hitung_rata_rata(*suhu):
    return sum(suhu) / len(suhu)


def analisis_suhu(data, batas_panas=32):
    if not data:
        return {}
    rata = hitung_rata_rata(*[d["suhu"] for d in data])
    tertinggi = max(data, key=lambda d: d["suhu"])   #lambda sebagai key
    terendah = min(data, key=lambda d: d["suhu"])
    detail = []
    jumlah_panas = 0
    for d in data:
        kategori = "Panas" if d["suhu"] >= batas_panas else "Normal"
        if kategori == "Panas":
            jumlah_panas += 1
        detail.append({"hari": d["hari"], "suhu": d["suhu"], "kategori": kategori})
    return {"rata_rata": rata, "tertinggi": tertinggi, "terendah": terendah,
            "jumlah_panas": jumlah_panas, "detail": detail}


def tulis_laporan(nama_laporan, hasil):
    with open(nama_laporan, "w") as file:
        file.write("=== LAPORAN SUHU MINGGUAN ===\n")
        file.write(f"Rata-rata suhu   : {hasil['rata_rata']:.2f} C\n")
        file.write(f"Suhu tertinggi   : {hasil['tertinggi']['suhu']} C ({hasil['tertinggi']['hari']})\n")
        file.write(f"Suhu terendah    : {hasil['terendah']['suhu']} C ({hasil['terendah']['hari']})\n")
        file.write(f"Jumlah hari panas: {hasil['jumlah_panas']}\n\n")
        file.write("Detail:\n")
        for d in hasil["detail"]:
            file.write(f"- {d['hari']}: {d['suhu']} C [{d['kategori']}]\n")
    with open(nama_laporan, "r") as file:
        print(file.read())


if __name__ == "__main__":
    data = baca_data_suhu("suhu.txt")
    if data:
        hasil = analisis_suhu(data, batas_panas=32)   #keyword argument
        tulis_laporan("laporan_suhu.txt", hasil)
