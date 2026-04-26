bash

cat /home/claude/seo_local_noticias_lunes.py
Salida

import time
import webbrowser
from datetime import datetime, timedelta

def obtener_noticias_seo_local():
    """Busca y abre las últimas novedades de SEO Local"""
    print("\n" + "="*60)
    print("🗺️  BUSCANDO NOVEDADES DE SEO LOCAL...")
    print("="*60 + "\n")
    
    # Portales de SEO Local principales
    sitios_seo_local = [
        ("Local SEO Guide", "https://www.localseoguide.com/"),
        ("BrightLocal", "https://www.brightlocal.com/blog/"),
        ("Google Business Profile", "https://business.google.com/"),
        ("Local Search Forum", "https://www.localsearchforum.com/"),
        ("Whitespark Blog", "https://www.whitespark.ca/blog/"),
        ("LinkedIn - SEO Local", "https://www.linkedin.com/feed/?keywords=local%20seo"),
    ]
    
    print("📌 Portales de SEO Local a revisar:\n")
    for nombre, url in sitios_seo_local:
        print(f"   ✓ {nombre}")
        print(f"     🔗 {url}\n")
    
    print("\n" + "="*60)
    print("🌐 Abriendo portales en navegador...")
    print("="*60 + "\n")
    
    for nombre, url in sitios_seo_local:
        print(f"   📂 Abriendo {nombre}...")
        try:
            webbrowser.open(url)
            time.sleep(1.5)
        except Exception as e:
            print(f"   ⚠️ Error al abrir {url}: {e}")
    
    print("\n✅ Novedades de SEO Local cargadas correctamente")
    print(f"⏰ Próxima actualización: próximo lunes a las 09:30 AM\n")

def proxima_ejecucion():
    """Calcula la próxima ejecución (próximo lunes 09:30)"""
    ahora = datetime.now()
    dias_hasta_lunes = (7 - ahora.weekday()) % 7
    if dias_hasta_lunes == 0:
        dias_hasta_lunes = 7
    
    proxima = ahora + timedelta(days=dias_hasta_lunes)
    proxima = proxima.replace(hour=9, minute=30, second=0, microsecond=0)
    return proxima

def programar_tarea():
    """Programa la tarea para ejecutarse cada lunes a las 09:00"""
    print("✅ Script iniciado")
    print("📅 Ejecutándose cada lunes a las 09:00 AM")
    print("💡 Mantén este script corriendo en background\n")
    
    # Primera ejecución
    obtener_noticias_seo_local()
    
    # Mantener el script corriendo
    ejecutado_hoy = False
    while True:
        ahora = datetime.now()
        
        # Si es lunes a las 09:00 y no se ha ejecutado hoy, ejecuta
        if ahora.weekday() == 0 and 9 <= ahora.hour < 10 and not ejecutado_hoy:
            print(f"⏰ {ahora.strftime('%Y-%m-%d %H:%M')} - Ejecutando tarea...")
            obtener_noticias_seo_local()
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
