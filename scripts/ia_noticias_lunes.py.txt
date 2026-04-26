bash

cat /home/claude/ia_noticias_lunes.py
Salida

import time
import webbrowser
from datetime import datetime, timedelta

def obtener_noticias_ia():
    """Busca y abre las últimas novedades de IA para marketing/SEO"""
    print("\n" + "="*60)
    print("🤖 BUSCANDO NOVEDADES DE IA (Claude + Herramientas)...")
    print("="*60 + "\n")
    
    # Portales de IA principales
    sitios_ia = [
        ("Anthropic - Claude", "https://www.anthropic.com/"),
        ("Product Hunt", "https://www.producthunt.com/"),
        ("The Verge - AI", "https://www.theverge.com/ai-artificial-intelligence"),
        ("Hacker News", "https://news.ycombinator.com/"),
        ("AI News", "https://www.artificialintelligence-news.com/"),
        ("LinkedIn - AI News", "https://www.linkedin.com/feed/?keywords=artificial%20intelligence"),
    ]
    
    print("📌 Portales de IA a revisar:\n")
    for nombre, url in sitios_ia:
        print(f"   ✓ {nombre}")
        print(f"     🔗 {url}\n")
    
    print("\n" + "="*60)
    print("🌐 Abriendo portales en navegador...")
    print("="*60 + "\n")
    
    for nombre, url in sitios_ia:
        print(f"   📂 Abriendo {nombre}...")
        try:
            webbrowser.open(url)
            time.sleep(1.5)
        except Exception as e:
            print(f"   ⚠️ Error al abrir {url}: {e}")
    
    print("\n✅ Novedades de IA cargadas correctamente")
    print(f"⏰ Próxima actualización: próximo lunes a las 10:00 AM\n")

def proxima_ejecucion():
    """Calcula la próxima ejecución (próximo lunes 10:00)"""
    ahora = datetime.now()
    dias_hasta_lunes = (7 - ahora.weekday()) % 7
    if dias_hasta_lunes == 0:
        dias_hasta_lunes = 7
    
    proxima = ahora + timedelta(days=dias_hasta_lunes)
    proxima = proxima.replace(hour=10, minute=0, second=0, microsecond=0)
    return proxima

def programar_tarea():
    """Programa la tarea para ejecutarse cada lunes a las 09:00"""
    print("✅ Script iniciado")
    print("📅 Ejecutándose cada lunes a las 09:00 AM")
    print("💡 Mantén este script corriendo en background\n")
    
    # Primera ejecución
    obtener_noticias_ia()
    
    # Mantener el script corriendo
    ejecutado_hoy = False
    while True:
        ahora = datetime.now()
        
        # Si es lunes a las 09:00 y no se ha ejecutado hoy, ejecuta
        if ahora.weekday() == 0 and 9 <= ahora.hour < 10 and not ejecutado_hoy:
            print(f"⏰ {ahora.strftime('%Y-%m-%d %H:%M')} - Ejecutando tarea...")
            obtener_noticias_ia()
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



