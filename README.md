# SysBlueprint Community & Portfolio Hub

> Ruang kolaborasi terbuka untuk pembelajar, rekasayawan sistem, dan akademisi dalam merancang arsitektur perangkat lunak, skema database relasional, workflow state machine, dan validasi riset empiris.

[![CI Quality Gate](https://github.com/zadevpenseo/sysblueprint-community/actions/workflows/ci.yml/badge.svg)](https://github.com/zadevpenseo/sysblueprint-community/actions/workflows/ci.yml)
[![Rubric Evaluator](https://github.com/zadevpenseo/sysblueprint-community/actions/workflows/rubric-evaluator.yml/badge.svg)](https://github.com/zadevpenseo/sysblueprint-community/actions/workflows/rubric-evaluator.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Studio Web](https://img.shields.io/badge/Studio_Web-sysblueprint.pages.dev-0284c7)](https://sysblueprint.pages.dev)
[![Agent Ready: Level 5](https://img.shields.io/badge/Agent_Readiness-Level_5-emerald.svg)](https://sysblueprint.pages.dev/.well-known/agent-card.json)

---

## 🧭 Ikhtisar Platform

SysBlueprint dibangun di atas filosofi **GitHub-First, Bukan GitHub-Only**:
* **Front Stage (Web Studio)**: Mahasiswa, dosen, dan rekayasawan dapat langsung menggunakan tools tanpa hambatan login atau pembuatan akun internal di [sysblueprint.pages.dev](https://sysblueprint.pages.dev).
* **Back Stage (GitHub Community)**: Repositori publik ini bertindak sebagai infrastruktur kolaborasi terstruktur untuk template proyek, studi kasus terverifikasi, tantangan mingguan, dan pengajuan portofolio.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SYSBLUEPRINT COLLABORATION FLYWHEEL                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
┌──────────────┐             ┌──────────────┐             ┌──────────────┐
│ 1. BELAJAR   │   ─────►    │ 2. REKAYASA  │   ─────►    │ 3. VALIDASI  │
│ Modul Konsep │             │ Desain Schema│             │ Aiken / SUS  │
│ & Studi Kasus│             │ State SCXML  │             │ Rubrik Skor  │
└──────────────┘             └──────────────┘             └──────────────┘
       ▲                                                         │
       │                     ┌──────────────┐                    │
       └──────────────────── │ 4. SHOWCASE  │ ◄──────────────────┘
                             │ Galeri Publik│
                             │ Peer Review  │
                             └──────────────┘
```

---

## 🛠️ Fitur & Template yang Tersedia

### 1. Template Proyek Mandiri (`resources/`)
Mulai proyek portofolio dalam satu langkah tanpa membangun struktur dokumentasi dari nol:
* [Template README Portofolio](resources/project-readme-template.md): Struktur standar presentasi rekayasa sistem untuk portofolio profesional.
* [Template Studi Kasus Arsitektur](resources/case-study-template.md): Format kajian mendalam ERD, SQL DDL, diagram state machine, dan analisis trade-off.
* [Template Formulir Peer Review](resources/peer-review-template.md): Lembar evaluasi sejawat objektif berbasis 4 dimensi mutu.

### 2. Evaluator Rubrik Otomatis (`scripts/rubric_grader.py`)
Setiap kiriman portofolio dinilai secara deterministik menggunakan skrip Python yang terintegrasi pada GitHub Actions:
```bash
python3 scripts/rubric_grader.py path/to/blueprint-submission.json
```

Predikat kelulusan:
* **DISTINCTION (Skor >= 85)**: Memenuhi seluruh invarian arsitektur, relasi konsisten, siap masuk kurasi galeri showcase.
* **COMPETENT (Skor >= 70)**: Lulus kriteria dasar, siap untuk tahap peer review.
* **NEEDS REVISION (Skor < 70)**: Memerlukan perbaikan pada pendefinisian Primary Key atau konsistensi transisi state.

---

## 🚀 Alur Kontribusi Cepat (First Contributions)

Kami mengadopsi spesifikasi **All-Contributors** untuk mengakui kontribusi kode, tulisan, kurasi studi kasus, dan peninjauan sejawat:

1. **Eksplorasi Studio**: Buka [sysblueprint.pages.dev](https://sysblueprint.pages.dev) dan buat rancangan skema database atau alur status SCXML Anda.
2. **Ekspor Proyek**: Unduh berkas cadangan JSON melalui tombol *Export Backup (JSON)* pada Studio.
3. **Fork & Uji Mandiri**:
   ```bash
   git clone https://github.com/<username>/sysblueprint-community.git
   cd sysblueprint-community
   python3 scripts/rubric_grader.py path/to/your-project.json
   ```
4. **Buka Pull Request**: Kirimkan studi kasus Anda ke folder `showcase/` atau `cases/`. GitHub Actions akan menjalankan evaluasi otomatis dalam hitungan detik.

Panduan selengkapnya dapat dibaca pada [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 💬 Kanal Diskusi & Komunitas

Manfaatkan [GitHub Discussions](https://github.com/zadevpenseo/sysblueprint-community/discussions) yang telah dikategorikan:
* **Announcements**: Berita rilis fitur baru, agenda tantangan, dan pengumuman kurasi showcase.
* **Q&A**: Tanya jawab seputar normalisasi database, sintaks ANSI SQL, dan W3C SCXML.
* **Show and Tell**: Bagikan tautan proyek portofolio Anda untuk mendapatkan umpan balik dari komunitas.
* **Challenges**: Diskusi pemecahan tantangan arsitektur sistem.
* **Career & Collaboration**: Kolaborasi antarpeserta, pencarian rekan proyek, dan konsultasi portofolio.

---

## 📚 Berkas Tata Kelola & Panduan

* [Pedoman Komunitas](COMMUNITY_GUIDELINES.md)
* [Panduan Tantangan](CHALLENGE_GUIDELINES.md)
* [Kriteria Pengajuan Showcase](SHOWCASE_SUBMISSION.md)
* [Rubrik Penilaian Objektif](PEER_REVIEW_RUBRIC.md)
* [Panduan Kolaborasi Karir](CAREER_AND_COLLABORATION.md)
* [Kebijakan Moderasi](MODERATION.md)
* [Arsitektur ADR-0001](docs/adr/ADR-0001-community-and-portfolio-hub-architecture.md)

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah lisensi terbuka [MIT License](LICENSE).
Karya tulis studi kasus dan modul edukasi dapat dirujuk dan diadaptasi secara bebas dengan mencantumkan atribusi ke SysBlueprint Studio.
