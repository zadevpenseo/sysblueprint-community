# Enterprise Multi-Tier Procurement Approval System

> Studi kasus perancangan skema database relasional 3NF dan mesin alur status multi-tier approval untuk tata kelola pengadaan barang korporat.

[![Rubrik Grade: Distinction](https://img.shields.io/badge/Rubrik_Skor-100%2F100_Distinction-emerald.svg)](https://sysblueprint.pages.dev)
[![Standard: ANSI SQL-92](https://img.shields.io/badge/Standard-ANSI_SQL--92-blue.svg)](https://sysblueprint.pages.dev)
[![Workflow: W3C SCXML](https://img.shields.io/badge/Workflow-W3C_SCXML-purple.svg)](https://sysblueprint.pages.dev)

---

## 🎯 1. Konteks Masalah & Kebutuhan

Sistem pengadaan barang enterprise sering menghadapi risiko penipuan internal (*internal fraud*), pesanan pembelian tanpa otorisasi anggaran, dan ketiadaan jejak audit yang tak dapat dimanipulasi. Solusi ini memisahkan peran pemohon (*department requestor*), peninjau operasional (*department manager*), dan pengesah keuangan (*finance division*).

---

## 🏛️ 2. Model Data Relasional

```mermaid
erDiagram
    departments ||--o{ procurement_requests : submits
    procurement_requests ||--|{ approval_audits : tracks
```

1. **Integritas Referensial**: Kunci asing `dept_id` mengikat ke `departments.id` dengan batasan `ON DELETE RESTRICT` guna memastikan riwayat departemen tidak terhapus selama memiliki berkas pengadaan.
2. **Append-Only Audit Log**: Tabel `approval_audits` bersifat *append-only* untuk memelihara catatan audit stempel waktu bagi setiap keputusan persetujuan.

---

## 🔄 3. Alur Status Transaksi (SCXML State Machine)

```mermaid
stateDiagram-v2
    [*] --> draft
    draft --> manager_review: SUBMIT
    manager_review --> finance_review: APPROVE_MANAGER
    manager_review --> rejected: REJECT
    finance_review --> po_issued: APPROVE_FINANCE
    finance_review --> rejected: REJECT
    po_issued --> [*]
    rejected --> [*]
```

---

## 📊 4. Hasil Verifikasi Evaluator

```
Skor Database : 100/100
Skor Alur     : 100/100
Skor Akhir    : 100.0/100 (Predikat: DISTINCTION)
```

Skrip DDL SQL lengkap tersedia pada [schema.sql](schema.sql) dan manifest data dapat diimpor langsung via [project.json](project.json).
