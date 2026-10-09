# Panduan Kontribusi SysBlueprint Community

Terima kasih atas minat Anda untuk berkontribusi pada SysBlueprint Community Hub! Kami menyambut segala bentuk kontribusi yang memajukan pemahaman rekayasa sistem, keterbacaan kode, dan validitas metodologi riset.

---

## 🌟 Model Pengakuan: All-Contributors

Kami percaya bahwa kontribusi bernilai tinggi tidak terbatas pada penulisan kode perangkat lunak. Kami secara resmi mengakui dan mencatat kontribusi dalam berbagai kategori:

* 📝 **Dokumentasi & Penulisan**: Menulis atau menyunting penjelasan studi kasus, artikel konsep, dan panduan belajar.
* 🎨 **Desain Skema & Alur**: Menyumbangkan model ERD relasional atau spesifikasi state machine SCXML teruji.
* 🔍 **Review Sejawat (Peer Review)**: Memberikan telaah konstruktif dan penilaian rubrik terhadap proyek peserta lain.
* 🐛 **Pelaporan Masalah**: Menemukan kelemahan logika, bug generator ANSI SQL, atau anomali visualizer.
* 🌐 **Penerjemahan & Glosarium**: Membantu standardisasi padanan istilah teknis arsitektur perangkat lunak ke dalam bahasa Indonesia baku.
* 💡 **Ide & Kasus Baru**: Mengusulkan skenario dunia nyata (misal: sistem escrow, lelang terdesentralisasi, rekam medis terpadu).

---

## 🚀 Alur Pengajuan Kontribusi Pertama (First Contributions)

1. **Fork Repositori**: Klik tombol *Fork* di pojok kanan atas repositori [sysblueprint-community](https://github.com/zadevpenseo/sysblueprint-community).
2. **Kloning ke Lokal**:
   ```bash
   git clone https://github.com/<username>/sysblueprint-community.git
   cd sysblueprint-community
   ```
3. **Buat Branch Fitur Baru**:
   Gunakan konvensi penamaan branch yang deskriptif:
   ```bash
   git checkout -b case/e-commerce-escrow-schema
   ```
4. **Validasi Mandiri Sebelum Commit**:
   Pastikan berkas JSON atau skrip baru lolos uji otomatis lokal:
   ```bash
   python3 -m unittest discover -s tests
   python3 scripts/rubric_grader.py path/to/your-submission.json
   ```
5. **Gunakan Format Conventional Commits**:
   * `feat: tambah studi kasus sistem escrow e-commerce`
   * `docs: perbarui rubrik penilaian normalisasi 3NF`
   * `fix: perbaiki referensi foreign key pada schema procurement`
6. **Buka Pull Request**:
   Ajukan Pull Request ke branch `main` repositori upstream. Sertakan ringkasan objektif dan motivasi perubahan pada deskripsi PR.

---

## 📋 Standar Mutu Kontribusi

Setiap kiriman studi kasus atau template wajib memenuhi 4 kriteria:
1. **Integritas Relasional**: Setiap tabel memiliki Primary Key yang eksplisit dan referensi Foreign Key yang valid.
2. **Determinisme State**: Diagram alur status wajib memiliki state awal (`initial`) yang terdefinisi dan bebas dari kondisi buntu (*deadlock*).
3. **Keterbacaan Naskah**: Mengikuti aturan penulisan jelas, menghindari kosakata klise mesin, dan tidak memuat teks kurung siku placeholder.
4. **Bebas Kredensial Rahasia**: Dilarang menyertakan token API, kata sandi, atau data identitas privat pada kode dan data contoh.
