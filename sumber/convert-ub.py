# Amankah/sumber/convert-ub.py
import glob
import os

# Direktori input dan output (relatif terhadap root repositori)
input_dir = "host/"  # Direktori tempat file .txt berada
output_dir = "host/"  # Direktori tempat file .text akan disimpan

# Log untuk debugging
print(f"Current working directory: {os.getcwd()}")
print(f"Input directory: {os.path.abspath(input_dir)}")
print(f"Output directory: {os.path.abspath(output_dir)}")

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
        with open(txt_file, 'r') as input_file:
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

    text_lines = ["## ublock"] + [f"||{domain}^" for domain in domains]
    print(f"text content for {txt_file}: {text_lines}")

    # Tentukan nama file output (.text)
    text_file = os.path.join(output_dir, os.path.basename(txt_file).replace(".txt", ".text"))
    print(f"Output file: {text_file}")

    # Simpan ke file .text
    try:
        with open(text_file, 'w') as output_file:
            output_file.write('\n'.join(text_lines))
        print(f"Successfully converted {txt_file} to {text_file}")
    except Exception as e:
        print(f"Failed to write {text_file}: {e}")
        continue