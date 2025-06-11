# Amankah/sumber/convert.py
import glob
import os
import json

# Direktori input dan output (relatif terhadap root repositori)
input_dir = "host/"  # Direktori tempat file .txt berada
output_dir = "host/"  # Direktori tempat file .json akan disimpan

# Log untuk debugging
print(f"Current working directory: {os.getcwd()}")
print(f"Input directory: {os.path.abspath(input_dir)}")
print(f"Output directory: {os.path.abspath(output_dir)}")

# Periksa apakah direktori input ada
if not os.path.exists(input_dir):
    print(f"Input directory {input_dir} does not exist. Skipping conversion.")
    exit(0)  # Exit gracefully

# Pastikan direktori output ada
os.makedirs(output_dir, exist_ok=True)

# Cari semua file .txt di direktori input
txt_files = glob.glob(os.path.join(input_dir, "*.txt"))
print(f"Found .txt files: {txt_files}")

if not txt_files:
    print("No .txt files found in host/. Skipping conversion.")
    exit(0)  # Exit gracefully to avoid failing the workflow

for txt_file in txt_files:
    # Baca isi file .txt
    try:
        with open(txt_file, 'r', encoding='utf-8') as input_file:
            domains = input_file.readlines()
        print(f"Read {txt_file}: {domains}")
    except Exception as e:
        print(f"Failed to read {txt_file}: {e}")
        continue

    # Membersihkan whitespace dan baris kosong
    domains = [domain.strip() for domain in domains if domain.strip()]
    print(f"Processed domains from {txt_file}: {domains}")

    # Jika file kosong, lewati
    if not domains:
        print(f"File {txt_file} is empty or contains no valid domains. Skipping.")
        continue

    # Buat struktur JSON
    json_data = {
        "version": 1,
        "rules": [
            {
                "domain_suffix": domains
            }
        ]
    }
    print(f"JSON content for {txt_file}: {json_data}")

    # Tentukan nama file output (.json)
    json_file = os.path.join(output_dir, os.path.basename(txt_file).replace(".txt", ".json"))
    print(f"Output file: {json_file}")

    # Simpan ke file .json
    try:
        with open(json_file, 'w', encoding='utf-8') as output_file:
            json.dump(json_data, output_file, indent=2, ensure_ascii=False)
        print(f"Successfully converted {txt_file} to {json_file}")
    except Exception as e:
        print(f"Failed to write {json_file}: {e}")
        continue
