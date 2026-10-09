#!/usr/bin/env python3
"""
rubric_grader.py
Evaluator deterministik untuk menilai kualitas kiriman portofolio dan rancangan
arsitektur SysBlueprint Community berdasarkan rubrik objektif empat dimensi.
"""

import sys
import json
import os
import argparse

def evaluate_database_schema(db_data):
    """Menilai integritas skema database relasional."""
    score = 100
    findings = []
    
    if not isinstance(db_data, dict) or "tables" not in db_data:
        return 0, ["Struktur database tidak memuat koleksi tabel yang valid."]
        
    tables = db_data.get("tables", [])
    if not tables:
        return 20, ["Tidak ditemukan tabel dalam skema database."]
        
    table_names = set(t.get("name", "") for t in tables)
    
    for tbl in tables:
        name = tbl.get("name", "unnamed")
        columns = tbl.get("columns", [])
        
        # Aturan 1: Setiap tabel wajib memiliki Primary Key
        has_pk = any(c.get("is_pk") for c in columns)
        if not has_pk:
            score -= 35
            findings.append(f"Tabel '{name}' tidak memiliki Primary Key yang terdefinisi.")
            
        # Aturan 2: Verifikasi referensi Foreign Key
        for col in columns:
            if col.get("is_fk"):
                ref = col.get("references", "")
                if "." in ref:
                    ref_tbl = ref.split(".")[0]
                    if ref_tbl not in table_names:
                        score -= 15
                        findings.append(f"Kolom '{name}.{col.get('name')}' merujuk tabel asing '{ref_tbl}' yang tidak ada dalam skema.")
                        
    return max(0, score), findings

def evaluate_workflow_state(wf_data):
    """Menilai determinisme dan kelengkapan state machine SCXML / XState."""
    score = 100
    findings = []
    
    if not isinstance(wf_data, dict) or "states" not in wf_data:
        return 0, ["Struktur workflow tidak memuat definisi state."]
        
    states = wf_data.get("states", [])
    if not states:
        return 20, ["Koleksi state kosong."]
        
    state_names = set(s.get("name", "") for s in states)
    
    # Aturan 1: Wajib ada initial state
    initial = wf_data.get("initial")
    if not initial:
        score -= 45
        findings.append("Workflow tidak mendeklarasikan initial state.")
    elif initial not in state_names:
        score -= 30
        findings.append(f"Initial state '{initial}' tidak terdaftar dalam koleksi state.")
        
    # Aturan 2: Verifikasi target transisi
    for st in states:
        s_name = st.get("name", "unnamed")
        for tr in st.get("transitions", []):
            target = tr.get("target")
            if target and target not in state_names:
                score -= 15
                findings.append(f"Transisi pada state '{s_name}' merujuk target '{target}' yang tidak terdefinisi.")
                
    return max(0, score), findings

def grade_submission(payload):
    """Menghitung skor gabungan dan menetapkan predikat kelulusan rubrik."""
    db_score, db_findings = evaluate_database_schema(payload.get("database", {}))
    wf_score, wf_findings = evaluate_workflow_state(payload.get("workflow", {}))
    
    # Pembobotan: Database (50%), Workflow (50%)
    total_score = round((db_score * 0.5) + (wf_score * 0.5), 1)
    
    if total_score >= 85:
        grade = "DISTINCTION (Siap Masuk Galeri Showcase)"
    elif total_score >= 70:
        grade = "COMPETENT (Lulus Rubrik Dasar)"
    elif total_score >= 50:
        grade = "NEEDS REVISION (Perlu Perbaikan Relasi/State)"
    else:
        grade = "UNSATISFACTORY (Struktur Belum Memenuhi Syarat)"
        
    all_findings = db_findings + wf_findings
    
    return {
        "author": payload.get("author", "Anonymous"),
        "project_name": payload.get("project_name", "Untitled Blueprint"),
        "database_score": db_score,
        "workflow_score": wf_score,
        "total_score": total_score,
        "grade": grade,
        "findings": all_findings
    }

def main():
    parser = argparse.ArgumentParser(description="SysBlueprint Rubric Grader CLI")
    parser.add_argument("file", help="Path berkas JSON kiriman proyek")
    parser.add_argument("--json", action="store_true", help="Cetak output dalam format JSON murni")
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"[ERROR] Berkas '{args.file}' tidak ditemukan.", file=sys.stderr)
        sys.exit(1)
        
    with open(args.file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    result = grade_submission(data)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("   SYSBLUEPRINT COMMUNITY: HASIL PENILAIAN RUBRIK PORTOFOLIO   ")
        print("=" * 60)
        print(f"Penulis      : {result['author']}")
        print(f"Proyek       : {result['project_name']}")
        print(f"Skor DB      : {result['database_score']}/100")
        print(f"Skor Alur    : {result['workflow_score']}/100")
        print(f"Skor Akhir   : {result['total_score']}/100")
        print(f"Predikat     : {result['grade']}")
        print("-" * 60)
        if result['findings']:
            print("Catatan & Temuan Evaluator:")
            for item in result['findings']:
                print(f"  • {item}")
        else:
            print("Temuan: Bersih, seluruh invarian arsitektur terpenuhi.")
        print("=" * 60)

if __name__ == "__main__":
    main()
