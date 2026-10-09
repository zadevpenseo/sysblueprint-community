#!/usr/bin/env python3
"""
SysBlueprint Community Broken-Link Sentinel
Memeriksa ketersediaan dan validitas URL materi OER secara berkala.
Dirancang ringan tanpa dependensi eksternal (stdlib urllib saja).
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error

USER_AGENT = "Mozilla/5.0 (compatible; SysBlueprint-Sentinel/1.0; +https://github.com/zadevpenseo/sysblueprint-community)"

def check_url(url: str, max_retries: int = 2) -> dict:
    """Memeriksa tautan URL menggunakan HTTP HEAD atau GET dengan mekanisme retry."""
    headers = {"User-Agent": USER_AGENT}
    
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers, method="HEAD")
            with urllib.request.urlopen(req, timeout=12) as resp:
                status = resp.status
                return {
                    "url": url,
                    "status": status,
                    "ok": 200 <= status < 400,
                    "error": None
                }
        except urllib.error.HTTPError as e:
            # Beberapa server menolak metode HEAD (405) atau 403, coba GET ringan
            if e.code in (403, 405):
                try:
                    get_req = urllib.request.Request(url, headers=headers, method="GET")
                    with urllib.request.urlopen(get_req, timeout=12) as get_resp:
                        return {
                            "url": url,
                            "status": get_resp.status,
                            "ok": 200 <= get_resp.status < 400,
                            "error": None
                        }
                except Exception as get_err:
                    if attempt == max_retries:
                        return {"url": url, "status": getattr(get_err, "code", 0), "ok": False, "error": str(get_err)}
            else:
                if attempt == max_retries:
                    return {"url": url, "status": e.code, "ok": False, "error": f"HTTP {e.code}: {e.reason}"}
        except Exception as e:
            if attempt == max_retries:
                return {"url": url, "status": 0, "ok": False, "error": str(e)}
        
        time.sleep(1.0) # Jeda sopan antar percobaan

    return {"url": url, "status": 0, "ok": False, "error": "Max retries exceeded"}

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "oer_resources.json")
    report_path = os.path.join(base_dir, "data", "broken_link_report.md")

    if not os.path.exists(data_path):
        print(f"[FATAL] Berkas data OER tidak ditemukan: {data_path}")
        sys.exit(1)

    with open(data_path, "r", encoding="utf-8") as f:
        resources = json.load(f)

    print(f"[*] Memulai audit Sentinel untuk {len(resources)} sumber OER...")
    results = []
    broken_count = 0

    for item in resources:
        url = item.get("canonicalUrl")
        res_id = item.get("id")
        title = item.get("title")

        if not url:
            continue

        print(f"  -> Memeriksa [{res_id}]: {url} ... ", end="", flush=True)
        res = check_url(url)
        res["id"] = res_id
        res["title"] = title
        results.append(res)

        if res["ok"]:
            print(f"OK (HTTP {res['status']})")
        else:
            print(f"GAGAL ({res['status']} / {res['error']})")
            broken_count += 1

        time.sleep(0.5) # Jeda santai untuk menjaga beban CPU 7W

    # Tulis laporan audit markdown
    lines = [
        "# Laporan Audit Sentinel Tautan OER SysBlueprint",
        "",
        f"Tanggal Audit: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        f"Total Sumber Diperiksa: {len(results)}",
        f"Tautan Aktif: {len(results) - broken_count}",
        f"Tautan Terindikasi Kendala: {broken_count}",
        "",
        "## Rincian Status Sumber Belajar",
        "",
        "| ID Sumber | Judul Materi | Status | Kode HTTP | Catatan / Kendala |",
        "| :--- | :--- | :---: | :---: | :--- |"
    ]

    for r in results:
        status_badge = "AKTIF" if r["ok"] else "KENDALA"
        err_msg = r["error"] or "Normal"
        clean_title = r["title"].replace("|", "/")
        lines.append(f"| `{r['id']}` | {clean_title} | {status_badge} | {r['status']} | {err_msg} |")

    lines.append("")
    lines.append("Laporan ini dihasilkan secara otomatis oleh Sentinel CI SysBlueprint Community.")
    lines.append("")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n[+] Audit selesai. Laporan disimpan ke: {report_path}")
    print(f"[+] Ringkasan: {len(results) - broken_count} aktif, {broken_count} kendala.")

    if broken_count > 0:
        print("[!] Terdapat tautan bermasalah yang membutuhkan verifikasi manusia atau pembaruan URL.")
        # Di CI mingguan, keluar dengan 0 jika sekadar laporan rutin atau 1 jika mode strict
        if os.getenv("STRICT_SENTINEL") == "true":
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
