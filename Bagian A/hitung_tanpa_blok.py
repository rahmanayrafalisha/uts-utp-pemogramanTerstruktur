# hitung_tanpa_blok if __name__ == "__main__"

def hitung_rata_rata(daftar_nilai):
    if not daftar_nilai:
        return 0.0
    angka = [float(n) for n in daftar_nilai]
    return sum(angka) / len(angka)


def proses_mahasiswa(nama, daftar_nilai, batas_lulus=70):
    rata = hitung_rata_rata(daftar_nilai)
    status = "Lulus" if rata >= batas_lulus else "Tidak Lulus"
    print("Nama      :", nama)
    print("Rata-rata :", round(rata, 2))
    print("Status    :", status)
    print("-" * 25)
    return rata, status

proses_mahasiswa("Budi", [80, 75, 90])
proses_mahasiswa("Sari", [60, 65, 55, 70])