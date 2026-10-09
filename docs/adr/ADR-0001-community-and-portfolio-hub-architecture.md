# ADR-0001: Arsitektur Pemisahan Repositori Inti Privat dan Hub Komunitas Publik

* **Status**: Diterima (*Accepted*)
* **Tanggal**: 2026-10-09
* **Penulis**: Muhammad Khoiruzzadittaqwa (Zadev)
* **Konteks**: SysBlueprint Studio & Community Hub (`github.com/zadevpenseo`)

---

## Konteks dan Masalah

SysBlueprint memerlukan infrastruktur kolaborasi untuk pembelajar, akademisi, dan praktisi industri tanpa mengorbankan keamanan kode inti dan generator backend privat. Jika seluruh kode aplikasi dan materi komunitas disatukan dalam satu repositori tunggal:
1. Kode sumber backend dan skrip operasional privat terekspos tanpa batas pemisah yang jelas.
2. Pengguna pemula yang ingin belajar atau mengajukan portofolio terintimidasi oleh kompleksitas dependensi web client dan bundle build tool.
3. Keterbatasan kuota menit GitHub Actions pada repositori privat menghambat eksekusi linter otomatis dan pengujian rubrik bagi kontributor umum.

---

## Keputusan Arsitektur

Kami memutuskan untuk menerapkan pola **Dual-Repository Architecture**:

1. **`zadevpenseo/sysblueprint` (Repositori Privat)**:
   * Menjadi rumah kanonikal bagi kode sumber aplikasi web (`web-client`), konfigurasi build, skrip generator OpenXML/DOCX, dan rahasia operasional.
   * Berfungsi sebagai *Engine Room* back-stage.

2. **`zadevpenseo/sysblueprint-community` (Repositori Publik)**:
   * Menjadi *Public Stage* untuk template portofolio, berkas panduan komunitas, kurasi showcase, dan repositori studi kasus.
   * Memanfaatkan fasilitas **unlimited GitHub Actions minutes** untuk repositori publik guna menjalankan evaluasi rubrik otomatis (`rubric_grader.py`), linter skema, dan bot penerima kontributor.
   * Mengaktifkan GitHub Discussions sebagai forum tanya-jawab terbuka dan peer-review tanpa perlu self-host platform forum mandiri (Discourse/Flarum).

---

## Konsekuensi

### Positif:
* **Keamanan Maksimal**: Kode internal dan rahasia generator aman di repositori privat.
* **Onboarding Bersih**: Kontributor publik hanya berhadapan dengan struktur studi kasus, template Markdown, dan schema JSON tanpa beban kompilasi React/Vite.
* **Otomasi Gratis & Cepat**: Pengecekan CI/CD dan grading rubrik berjalan otomatis melalui GitHub Actions publik tanpa memakan kuota berbayar.
* **Kepatuhan Invarian**: Menghilangkan kebutuhan autentikasi rumit di sisi website; pengguna bebas menjelajah Studio secara lokal.

### Negatif / Mitigasi:
* Diperlukan pemeliharaan sinkronisasi manual/terprogram jika ada pembaruan skema data di web-client yang berdampak pada template studi kasus di repositori komunitas. Mitigasi: Runtime schema Zod diekspor dalam format JSON Schema yang dapat diakses secara publik via endpoint static `llms.txt` dan `.well-known/agent-card.json`.
