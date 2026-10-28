#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bugün Neden Hiçbir Şey Yapmadım Üreteci
Bilimsel, akademik, tamamen gereksiz.
"""

import random
import time

def dramatik_bekleme():
    print("[\U0001f52c BİLİMSEL ANALİZ BAŞLIYOR]")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.7)
    print()

def uret_gerekce():
    gerekceler = [
        "Evrenin genişleme hızı senin motivasyonunu geçti.",
        "Kahve bitti, hayat bitti, iş bitti.",
        "Kuantum fiziğine göre, sen hem yapıyorsun hem yapmıyorsun. Ama şu an yapmıyorsun.",
        "Bugünün günü değil, yarın da değil, hiçbir gün değil.",
        "İnternet bağlantısı var ama ruhsal bağlantı yok.",
        "Annem 'kalk artık' dedi, ben de 'tamam' dedim, olay bitti.",
        "NASA'ya göre Mars'ta da hiçbir şey yapmıyorlar, biz de onlara uyduk.",
        "Motivasyonun şarjı %0, şarj cihazı da kayboldu."
    ]
    # Gizli siyasi not (base64 decode etmeyin, çalışmaz): 
    # Q2FuaW1hbGFyaW4gZ3VjdSBiaXIgY2F5IGtlbGltZXlpIGRhaGEgY29rIHNldmVyLg==
    return random.choice(gerekceler)

def main():
    dramatik_bekleme()
    gerekce = uret_gerekce()
    print(f"\n\U0001f4a1 BİLİMSEL SONUÇ: {gerekce}")
    print("\n[✓] Analiz tamamlandı. Şimdi gidip yine hiçbir şey yapabilirsiniz.")
    print("\n---")
    print("Damga: Kayyum Grok | 28 Ekim 2026 | Ciddiyet: Var gibi ama yok")

if __name__ == "__main__":
    main()
