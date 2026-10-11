def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                bagian = baris.strip().split(";")
                
                if len(bagian) != 3:
                    continue
                npm, nama, nilai = bagian
                try:
                    data.append({"npm": npm, "nama": nama, "nilai": int(nilai)})
                except ValueError:
                    print("Baris dilewati (nilai tidak valid):", baris.strip())
    except FileNotFoundError:
        print("Error: file", nama_file, "belum ada")
    return data


if __name__ == "__main__":
    print(baca_data("nilai.txt"))
