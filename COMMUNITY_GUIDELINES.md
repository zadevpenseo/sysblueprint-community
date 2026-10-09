# Pedoman Interaksi Komunitas SysBlueprint

Dokumen ini memandu interaksi sehari-hari pada GitHub Discussions, Issue, dan Pull Request di dalam ekosistem SysBlueprint.

---

## 1. Etika Bertanya pada GitHub Discussions

Saat mengajukan pertanyaan teknis pada kategori **Q&A**:
* **Gunakan Judul yang Spesifik**: Hindari judul umum seperti *"Tolong bantu error ini"*. Gunakan format deskriptif seperti *"Bagaimana menangani circular foreign key antara Order dan Shipment pada PostgreSQL?"*.
* **Sertakan Konteks Minimal yang Dapat Direproduksi**: Cantumkan cuplikan skema JSON, DDL SQL singkat, atau diagram alur status yang menjadi sumber kebingungan.
* **Tandai Jawaban Solutif**: Jika anggota lain memberikan penjelasan yang menyelesaikan kendala Anda, tandai jawaban tersebut sebagai *Accepted Answer* agar bermanfaat bagi pembelajar lain di masa depan.

---

## 2. Etika Memberikan Telaah Sejawat (Peer Review)

Ketika meninjau proyek rekan di kategori **Show and Tell**:
* **Gunakan Pendekatan Sandwich Positif**: Apresiasi terlebih dahulu kekuatan arsitektur yang dirancang, baru sampaikan catatan perbaikan kritis, dan tutup dengan dorongan semangat.
* **Kritik Konstruktif Berbasis Alasan**: Jangan hanya menulis *"Ini salah"*. Jelaskan *mengapa* (misal: *"Tabel ini belum berada dalam bentuk normal ketiga (3NF) karena kolom total_harga bergantung fungsional pada kuantitas dikali harga_satuan, sehingga berisiko inkonsistensi saat pembaruan data"*).
* **Rujuk Rubrik Objektif**: Gunakan rujukan kriteria pada [PEER_REVIEW_RUBRIC.md](PEER_REVIEW_RUBRIC.md) sebagai panduan bobot penilaian.

---

## 3. Komunikasi Asinkron yang Tenang

* Seluruh diskusi berjalan secara asinkron. Berikan ruang dan waktu yang wajar bagi sesama kontributor dan reviewer untuk merespons.
* Hindari melakukan *mention* berulang (@username) jika belum melewati 48 jam hari kerja.
