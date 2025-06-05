import os
import glob

# Direktori tempat file .txt berada
input_directory = 'host/'  # Ganti dengan path folder Anda
output_directory = 'host/'  # Ganti dengan path folder output (opsional)

# Pastikan direktori output ada
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Cari semua file .txt di direktori
txt_files = glob.glob(os.path.join(input_directory, '*.txt'))

for txt_file in txt_files:
    # Baca isi file
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Menghapus duplikat sambil mempertahankan urutan
        seen = set()
        unique_lines = [line.strip() for line in lines if not (line.strip() in seen or seen.add(line.strip()))]

    # Nama file output (bisa di folder yang sama atau folder output terpisah)
    output_file = os.path.join(output_directory, os.path.basename(txt_file))
    
    # Tulis hasil ke file output
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in unique_lines:
            file.write(line + '\n')

    print(f"Duplikat dihapus untuk: {txt_file}. Hasil disimpan di: {output_file}")

print("Semua file telah diproses.")
