bash

cat /home/claude/seo_noticias_lunes.py
Salida

import time
import webbrowser
from datetime import datetime, timedelta

def obtener_noticias_seo():
    """Busca y abre las últimas novedades de SEO"""
    print("\n" + "="*60)
    print("🔍 BUSCANDO NOVEDADES DE SEO...")
    print("="*60 + "\n")
    
    # Portales de SEO principales
    sitios_seo = [
        ("SEO Roundtable", "https://www.seroundtable.com/"),
        ("Search Engine Journal", "https://www.searchenginejournal.com/"),
        ("Semrush Blog", "https://www.semrush.com/blog/"),
        ("Moz Blog", "https://moz.com/blog"),
        ("SEMrush Research", "https://www.semrush.com/"),
        ("LinkedIn - SEO News", "https://www.linkedin.com/feed/?keywords=seo"),
    ]
    
    print("📌 Portales de SEO a revisar:\n")
    for nombre, url in sitios_seo:
        print(f"   ✓ {nombre}")
        print(f"     🔗 {url}\n")
    
    print("\n" + "="*60)
    print("🌐 Abriendo portales en navegador...")
    print("="*60 + "\n")
    
    for nombre, url in sitios_seo:
        print(f"   📂 Abriendo {nombre}...")
        try:
            webbrowser.open(url)
            time.sleep(1.5)
        except Exception as e:
            print(f"   ⚠️ Error al abrir {url}: {e}")
    
    print("\n✅ Novedades de SEO cargadas correctamente")
    print(f"⏰ Próxima actualización: próximo lunes a las 09:00 AM\n")

def es_lunes_09_00():
    """Verifica si es lunes a las 09:00"""
    ahora = datetime.now()
    return ahora.weekday() == 0 and 9 <= ahora.hour < 10

def proxima_ejecucion():
    """Calcula la próxima ejecución (próximo lunes 09:00)"""
    ahora = datetime.now()
    dias_hasta_lunes = (7 - ahora.weekday()) % 7
    if dias_hasta_lunes == 0:
        dias_hasta_lunes = 7
    
    proxima = ahora + timedelta(days=dias_hasta_lunes)
    proxima = proxima.replace(hour=9, minute=0, second=0, microsecond=0)
    return proxima

def programar_tarea():
    """Programa la tarea para ejecutarse cada lunes a las 09:00"""
    print("✅ Script iniciado")
    print("📅 Ejecutándose cada lunes a las 09:00 AM")
    print("💡 Mantén este script corriendo en background\n")
    
    # Primera ejecución
    obtener_noticias_seo()
    
    # Mantener el script corriendo
    ejecutado_hoy = False
    while True:
        ahora = datetime.now()
        
        # Si es lunes a las 09:00 y no se ha ejecutado hoy, ejecuta
        if ahora.weekday() == 0 and 9 <= ahora.hour < 10 and not ejecutado_hoy:
            print(f"⏰ {ahora.strftime('%Y-%m-%d %H:%M')} - Ejecutando tarea...")
            obtener_noticias_seo()
            ejecutado_hoy = True
            time.sleep(3600)  # Espera 1 hora para no repetir
        elif ahora.weekday() != 0:
            ejecutado_hoy = False  # Reset al cambiar de día
        
        # Mostrar próxima ejecución
        proxima = proxima_ejecucion()
        print(f"⏳ Esperando... Próxima ejecución: {proxima.strftime('%A %d-%m-%Y a las %H:%M')}")
        time.sleep(300)  # Verifica cada 5 minutos

if __name__ == "__main__":
    programar_tarea()
