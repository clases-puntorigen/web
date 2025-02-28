from nicegui_router import page, ui
from modelos.diario import RegistroDiario

@page("/")
async def inicio():
    ui.label("Servidor funcionando").classes("text-h4")
    
    try:
        datos = await RegistroDiario.get_by_attribute(all=True, fecha="2025-02-27")
        # Convert the data to a string representation
        if datos:
            ui.label("Registros encontrados:").classes("text-h5 mt-4")
            for reg in datos:
                ui.label(f"El ID es: {reg.id}")
                info = f"ID: {reg.id}, Fecha: {reg.fecha}, Resumen: {reg.resumen_dia}"
                
                ui.label(info).classes("text-body1 ml-4")
        else:
            ui.label("No hay registros en la base de datos.").classes("text-body1 mt-4")
    except Exception as e:
        ui.label(f"Error al obtener datos: {str(e)}").classes("text-negative")