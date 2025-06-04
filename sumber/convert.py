import glob
import os

# Direktori input (tempat file .txt berada)
input_dir = "../path/"  # Relatif terhadap ~/Amankah/sumber/, menuju ~/Amankah/path/
# Direktori output (tempat file .yaml akan disimpan)
output_dir = "../path/"  # Bisa diubah ke direktori lain jika perlu

# Pastikan direktori output ada
os.makedirs(output_dir, exist_ok=True)

# Cari semua file .txt di direktori input
txt_files = glob.glob(os.path.join(input_dir, "*.txt"))

for txt_file in txt_files:
    # Baca isi file .txt
    with open(txt_file, 'r') as input_file:
        domains = input_file.readlines()

    # Membersihkan whitespace dan baris kosong
    domains = [domain.strip() for domain in domains if domain.strip()]

    # Jika file kosong, lewati
    if not domains:
        print(f"File {txt_file} kosong, dilewati.")
        continue

    # Mengubah format ke DOMAIN-SUFFIX
    yaml_lines = [f"  - DOMAIN-SUFFIX,{domain}" for domain in domains]

    # Tentukan nama file output (.yaml)
    yaml_file = os.path.join(output_dir, os.path.basename(txt_file).replace(".txt", ".yaml"))

    # Simpan ke file .yaml
    with open(yaml_file, 'w') as output_file:
        output_file.write('\n'.join(yaml_lines))
    print(f"Berhasil mengonversi {txt_file} menjadi {yaml_file}")
