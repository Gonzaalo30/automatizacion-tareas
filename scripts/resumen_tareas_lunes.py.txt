bash

cat /home/claude/resumen_tareas_lunes.py
Salida

import json
import time
from datetime import datetime, timedelta
from pathlib import Path

# Archivo donde se guardan las tareas
ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    """Carga las tareas desde el archivo JSON"""
    if Path(ARCHIVO_TAREAS).exists():
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def crear_tabla(datos, headers):
    """Crea una tabla visual bonita"""
    if not datos:
        return ""
    
    # Calcular anchos de columna
    anchos = [len(h) for h in headers]
    for fila in datos:
        for i, valor in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(valor)))
    
    # Crear tabla
    separador = "┌" + "┬".join(["─" * (a + 2) for a in anchos]) + "┐"
    header_line = "│" + "│".join([f" {h:<{anchos[i]}} " for i, h in enumerate(headers)]) + "│"
    divisor = "├" + "┼".join(["─" * (a + 2) for a in anchos]) + "┤"
    pie = "└" + "┴".join(["─" * (a + 2) for a in anchos]) + "┘"
    
    tabla = separador + "\n" + header_line + "\n" + divisor + "\n"
    
    for fila in datos:
        tabla += "│" + "│".join([f" {str(v):<{anchos[i]}} " for i, v in enumerate(fila)]) + "│\n"
    
    tabla += pie
    return tabla

def mostrar_resumen_tareas():
    """Muestra el resumen de todas las tareas"""
    tareas = cargar_tareas()
    
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + " "*15 + "📋 RESUMEN DE TAREAS - LUNES 09:00 AM" + " "*25 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"📅 Fecha: {datetime.now().strftime('%A, %d de %B de %Y')} | ⏰ Hora: {datetime.now().strftime('%H:%M')}\n")
    
    if not tareas:
        print("✨ No hay tareas registradas. ¡Perfecto! 🎉\n")
        return
    
    # Separar tareas por estado
    pendientes = [t for t in tareas if t.get('estado') == 'Pendiente']
    en_progreso = [t for t in tareas if t.get('estado') == 'En progreso']
    completadas = [t for t in tareas if t.get('estado') == 'Hecho']
    
    # Función para ordenar por urgencia
    def orden_urgencia(tarea):
        urgencia = tarea.get('urgencia', 'Baja')
        orden = {'Alta': 0, 'Media': 1, 'Baja': 2}
        return orden.get(urgencia, 3)
    
    # Emojis de urgencia
    def emoji_urgencia(urgencia):
        return {'Alta': '🔴', 'Media': '🟡', 'Baja': '🟢'}.get(urgencia, '⚪')
    
    # Mostrar tareas pendientes
    if pendientes:
        pendientes.sort(key=orden_urgencia)
        print("🔴 TAREAS PENDIENTES (Ordenadas por urgencia):\n")
        
        datos = []
        for i, tarea in enumerate(pendientes, 1):
            datos.append([
                f"#{i}",
                tarea.get('nombre', 'N/A')[:30],
                tarea.get('cliente', 'N/A'),
                emoji_urgencia(tarea.get('urgencia')) + " " + tarea.get('urgencia', 'N/A'),
                tarea.get('duracion', 'N/A'),
                tarea.get('fecha_dias', 'N/A')
            ])
        
        print(crear_tabla(datos, ["#", "Tarea", "Cliente", "Urgencia", "Duración", "Fecha"]))
        print()
    
    # Mostrar tareas en progreso
    if en_progreso:
        en_progreso.sort(key=orden_urgencia)
        print("🟡 TAREAS EN PROGRESO:\n")
        
        datos = []
        for i, tarea in enumerate(en_progreso, 1):
            datos.append([
                f"#{i}",
                tarea.get('nombre', 'N/A')[:30],
                tarea.get('cliente', 'N/A'),
                emoji_urgencia(tarea.get('urgencia')) + " " + tarea.get('urgencia', 'N/A'),
                tarea.get('duracion', 'N/A'),
                tarea.get('fecha_dias', 'N/A')
            ])
        
        print(crear_tabla(datos, ["#", "Tarea", "Cliente", "Urgencia", "Duración", "Fecha"]))
        print()
    
    # Mostrar tareas completadas
    if completadas:
        print("✅ TAREAS COMPLETADAS ESTA SEMANA:\n")
        
        datos = []
        for i, tarea in enumerate(completadas, 1):
            datos.append([
                f"#{i}",
                tarea.get('nombre', 'N/A')[:30],
                tarea.get('cliente', 'N/A'),
                "✓ Completada"
            ])
        
        print(crear_tabla(datos, ["#", "Tarea", "Cliente", "Estado"]))
        print()
    
    # Resumen estadístico
    print("╔" + "═"*78 + "╗")
    print("║" + " "*29 + "📊 ESTADÍSTICAS" + " "*34 + "║")
    print("╠" + "═"*78 + "╣")
    
    stats_data = [
        ["⏳ Pendientes", f"{len(pendientes)} tareas"],
        ["🔄 En progreso", f"{len(en_progreso)} tareas"],
        ["✅ Completadas", f"{len(completadas)} tareas"],
        ["📈 Total", f"{len(tareas)} tareas"]
    ]
    
    for label, valor in stats_data:
        print(f"║ {label:<38} {valor:>37} ║")
    
    print("╚" + "═"*78 + "╝")
    print()
    
    # Resumen por cliente
    print("╔" + "═"*78 + "╗")
    print("║" + " "*28 + "👥 TAREAS POR CLIENTE" + " "*28 + "║")
    print("╠" + "═"*78 + "╣")
    
    clientes = {}
    for tarea in tareas:
        cliente = tarea.get('cliente', 'Sin cliente')
        if cliente not in clientes:
            clientes[cliente] = {'total': 0, 'pendientes': 0, 'en_progreso': 0, 'completadas': 0}
        clientes[cliente]['total'] += 1
        if tarea.get('estado') == 'Pendiente':
            clientes[cliente]['pendientes'] += 1
        elif tarea.get('estado') == 'En progreso':
            clientes[cliente]['en_progreso'] += 1
        elif tarea.get('estado') == 'Hecho':
            clientes[cliente]['completadas'] += 1
    
    if clientes:
        datos_clientes = []
        for cliente, stats in sorted(clientes.items()):
            datos_clientes.append([
                cliente,
                str(stats['total']),
                f"⏳ {stats['pendientes']}",
                f"🔄 {stats['en_progreso']}",
                f"✅ {stats['completadas']}"
            ])
        
        print(crear_tabla(datos_clientes, ["Cliente", "Total", "Pendientes", "En progreso", "Completadas"]))
    
    print("╚" + "═"*78 + "╝\n")

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
    print("✅ Script de resumen de tareas iniciado")
    print("📅 Se ejecutará cada lunes a las 09:00 AM")
    print("💡 Mantén este script corriendo en background\n")
    
    # Primera ejecución
    mostrar_resumen_tareas()
    
    # Mantener el script corriendo
    ejecutado_hoy = False
    while True:
        ahora = datetime.now()
        
        # Si es lunes a las 09:00 y no se ha ejecutado hoy, ejecuta
        if ahora.weekday() == 0 and 9 <= ahora.hour < 10 and not ejecutado_hoy:
            print(f"⏰ {ahora.strftime('%Y-%m-%d %H:%M')} - Ejecutando resumen de tareas...")
            mostrar_resumen_tareas()
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
