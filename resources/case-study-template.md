# Template Studi Kasus Rekayasa Arsitektur Sistem

## Informasi Dokumen
* **Judul Kasus**: [Judul Studi Kasus]
* **Domain Industri**: [Fintech / Kesehatan / Logistik / E-Commerce / Pendidikan]
* **Tingkat Kompleksitas**: [Dasar / Menengah / Mahir]
* **Penulis**: [Nama Lengkap Penulis]
* **Status Review**: [Draf / Siap Review / Terverifikasi]

---

## 1. Ringkasan Eksekutif
Jelaskan dalam 1 paragraf padat tentang tantangan operasional yang dihadapi organisasi dan bagaimana perancangan sistem ini memberikan solusi yang dapat dibuktikan.

---

## 2. Analisis Kebutuhan & Batasan Sistem
* **Kebutuhan Fungsional**: Daftar kapabilitas wajib yang harus disediakan sistem.
* **Kebutuhan Non-Fungsional**: Ketersediaan (*availability*), waktu respons (*latency*), dan auditabilitas transaksi.
* **Batasan Regulasi & Keamanan**: Standar perlindungan data pribadi dan pencegahan kebocoran kredensial.

---

## 3. Desain Model Data Relasional
* Lampirkan diagram relasi entitas (ERD) Mermaid.
* Cantumkan definisi skema DDL ANSI SQL.
* Paparkan argumen pemilihan normalisasi (misal: normalisasi 3NF untuk tabel inti dan tabel audit append-only).

---

## 4. Desain Alur Status Transaksi (State Machine)
* Lampirkan diagram state SCXML.
* Tabulasikan matriks transisi: State Asal, Pemicu (*Event*), Penjaga Kondisi (*Guard*), dan State Tujuan.
* Jelaskan penanganan skenario kegagalan (*failure modes*) dan pembatalan (*rollback*).

---

## 5. Analisis Trade-Off & Keputusan Arsitektur
Jelaskan mengapa Anda memilih solusi A dibanding alternatif B:
* **Pilihan A vs Pilihan B**: (misal: Relasional SQL vs Dokumen NoSQL).
* **Alasan Pemilihan**: Keunggulan integritas transaksi ACID dibanding skalabilitas horisontal tak terstruktur.
* **Kelemahan yang Diterima**: Kebutuhan migrasi skema terencana saat volume data meningkat.

---

## 6. Referensi & Rujukan Standar
* Standar ANSI SQL-92 / ISO 9075
* W3C State Chart XML (SCXML)
* APA 7th Edition untuk sitasi akademis (jika relevan)
