# processing.py
from inventaris_pkg.validasi import validasi_produk


class Produk:
    def __init__(self, kode, nama, harga, stok, **kwargs):
        # data divalidasi dulu sebelum disimpan
        validasi_produk(kode, nama, harga, stok)
        self.kode = kode
        self.nama = nama
        self.harga = float(harga)
        self.stok = stok
        # **kwargs: atribut tambahan yang bisa berbeda tiap produk
        self.kategori = kwargs.get("kategori", "Umum")
        self.tambahan = kwargs

    def nilai_stok(self):
        # nilai total satu produk
        return self.harga * self.stok

    def to_dict(self):
        return {"kode": self.kode, "nama": self.nama, "harga": self.harga,
                "stok": self.stok, "kategori": self.kategori}


class OlahInventaris:
    def __init__(self, daftar_produk=None):
        self.daftar_produk = daftar_produk if daftar_produk is not None else []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def hitung_total_nilai(self):
        return sum(p.nilai_stok() for p in self.daftar_produk)

    def hitung_stok_kategori(self, *kategori):
        # *kategori: boleh menyebut berapa pun kategori; kosong = semua
        terpilih = filter(lambda p: not kategori or p.kategori in kategori,
                          self.daftar_produk)
        return sum(p.stok for p in terpilih)

    def urutkan_termahal(self):
        # lambda sebagai key pengurutan
        return sorted(self.daftar_produk, key=lambda p: p.harga, reverse=True)

    def filter_stok_kritis(self, batas=5):
        # lambda untuk filter stok kecil
        return list(filter(lambda p: p.stok <= batas, self.daftar_produk))

    def ringkasan(self):
        if not self.daftar_produk:
            return {"total_item": 0, "total_nilai": 0.0, "termahal": "-"}
        termahal = max(self.daftar_produk, key=lambda p: p.harga)
        return {"total_item": len(self.daftar_produk),
                "total_nilai": self.hitung_total_nilai(),
                "termahal": termahal.nama}

    def laporan_teks(self, batas=5):
        r = self.ringkasan()
        baris = [f"Total jenis barang : {r['total_item']}",
                 f"Total nilai stok   : Rp {r['total_nilai']:,.0f}",
                 f"Barang termahal    : {r['termahal']}",
                 "",
                 "Urutan harga termahal ke termurah:"]
        for p in self.urutkan_termahal():
            baris.append(f"- {p.nama}: Rp {p.harga:,.0f} (stok {p.stok})")
        baris.append("")
        baris.append(f"Stok kritis (<= {batas}):")
        for p in self.filter_stok_kritis(batas=batas):
            baris.append(f"- {p.nama}: sisa {p.stok}")
        return "\n".join(baris) + "\n"
