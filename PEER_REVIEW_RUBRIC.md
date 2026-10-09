# Rubrik Penilaian Portofolio Arsitektur (Peer Review Rubric)

Rubrik ini memuat kriteria objektif dalam 4 dimensi evaluasi teknis. Gunakan panduan ini saat menilai proyek rekan Anda.

---

## Matriks 4 Dimensi Penilaian

| Dimensi | Bobot | Kriteria Skor Penuh (4 - 5) | Kriteria Skor Sebagian (2 - 3) | Kriteria Perlu Perbaikan (0 - 1) |
|:---|:---|:---|:---|:---|
| **1. Skema Database Relasional** | 30% | Bentuk normal 3NF terpenuhi, seluruh tabel memiliki Primary Key, Foreign Key merujuk relasi valid, indeks pada kolom pencarian sering dispesifikasikan. | Tabel memiliki PK tetapi ada redundansi kolom transisional atau tipe data tidak seragam. | Tidak ada PK, kunci asing putus (*dangling reference*), atau struktur denormalisasi tanpa alasan yang dapat dipertahankan. |
| **2. Determinisme State Machine** | 30% | State awal eksplisit, seluruh transisi memiliki pemicu (*event*) dan target jelas, tidak ada status buntu (*dead end*), sesuai standar W3C SCXML / XState. | State awal ada, tetapi transisi kegagalan atau pembatalan belum dimodelkan secara lengkap. | Tidak ada deklarasi alur status, terjadi siklus tak terbatas (*infinite loop*) tanpa kondisi keluar. |
| **3. Validitas Riset & Pengukuran** | 20% | Koefisien validitas Aiken V dihitung dengan benar terhadap $N$ penilai, atau skor SUS dikalibrasi terhadap persentil Bangor, tabel APA 7th format bersih. | Rumus terlampir tetapi interpretasi statistik kurang mendalam. | Menggunakan angka rekaan tanpa dasar metodologis atau formula salah. |
| **4. Kejelasan Dokumentasi Arsitektur** | 20% | Diagram C4 Level 1-2 rapi, keputusan desain dicatat via ADR, batasan keamanan dan trade-off dijelaskan secara jujur dan rendah hati. | Penjelasan ada tetapi diagram sulit dibaca atau keputusan teknis tidak memiliki rujukan alasan. | Dokumentasi kosong atau hanya mengulang kode sumber tanpa penjelasan arsitektural. |

---

## Ambang Batas Kelulusan

* **Distinction (85 - 100)**: Direkomendasikan langsung ke kurasi Galeri Showcase SysBlueprint.
* **Competent (70 - 84)**: Memenuhi standar portofolio profesional siap kerja.
* **Revision Needed (< 70)**: Penulis wajib memperbaiki poin temuan sebelum dapat diajukan kembali.
