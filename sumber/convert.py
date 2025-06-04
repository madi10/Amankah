# Amankah/sumber/convert.py
import glob
import os

# Direktori input dan output (relatif terhadap root repositori)
input_dir = "path/"  # Direktori tempat file .txt berada
output_dir = "path/"  # Direktori tempat file .yaml akan disimpan

# Pastikan direktori output ada
os.makedirs(output_dir, exist_ok=True)

# Cari semua file .txt di direktori input
txt_files = glob.glob(os.path.join(input_dir, "*.txt"))

for txt_file in txt_files:
    # Baca isi file .txt
    try:
        with open(txt_file, 'r') as input_file:
            domains = input_file.readlines()
    except Exception as e:
        print(f"Gagal membaca {txt_file}: {e}")
        continue

    # Membersihkan whitespace dan baris kosong
    domains = [domain.strip() for domain in domains if domain.strip()]

    # Jika file kosong, lewati
    if not domains:
        print(f"File {txt_file} kosong, dilewati.")
        continue

    # Mengubah format ke DOMAIN-SUFFIX dengan header Payload
    yaml_lines = ["Payload:"] + [f"    - DOMAIN-SUFFIX,{domain}" for domain in domains]

    # Tentukan nama file output (.yaml)
    yaml_file = os.path.join(output_dir, os.path.basename(txt_file).replace(".txt", ".yaml"))

    # Simpan ke file .yaml
    try:
        with open(yaml_file, 'w') as output_file:
            output_file.write('\n'.join(yaml_lines))
        print(f"Berhasil mengonversi {txt_file} menjadi {yaml_file}")
    except Exception as e:
        print(f"Gagal menulis {yaml_file}: {e}")
