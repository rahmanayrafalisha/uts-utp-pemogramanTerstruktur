class DataError(Exception):
    """Induk untuk semua error data buatan sendiri."""


class NilaiNegatifError(DataError):
    """Dimunculkan jika harga atau stok negatif."""


class DataKosongError(DataError):
    """Dimunculkan jika kode atau nama kosong."""


def validasi_produk(kode, nama, harga, stok):
    if not str(kode).strip() or not str(nama).strip():
        raise DataKosongError("Kode dan nama tidak boleh kosong")
    if harga < 0 or stok < 0:
        raise NilaiNegatifError("Harga dan stok tidak boleh negatif")
    assert isinstance(stok, int), "Stok harus bilangan bulat"
    return True


if __name__ == "__main__":
    print(validasi_produk("E01", "Laptop", 8000000, 5))
    try:
        validasi_produk("E02", "Mouse", -1, 2)
    except NilaiNegatifError as e:
        print("Error tertangkap:", e)
