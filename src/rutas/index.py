from nicegui_router import page, ui
from modelos.diario import RegistroDiario

@page("/")
async def inicio():
    ui.label("Servidor funcionando").classes("text-h4")
    
    try:
        datos = await RegistroDiario.get_by_attribute(all=True)
        
        # Convert the data to a string representation
        if datos:
            ui.label("Registros encontrados:").classes("text-h5 mt-4")
            for reg in datos:
                ui.label(f"El ID es: {reg.id}")
                # Check if reg is a tuple or a RegistroDiario object
                if isinstance(reg, tuple):
                    # If it's a tuple, extract the fields based on their position
                    reg_id = reg[0] if len(reg) > 0 else "N/A"
                    reg_fecha = reg[1] if len(reg) > 1 else "N/A"
                    reg_resumen = reg[2] if len(reg) > 2 else "N/A"
                    info = f"ID: {reg_id}, Fecha: {reg_fecha}, Resumen: {reg_resumen}"
                else:
                    # If it's an object, access attributes directly
                    info = f"ID: {reg.id}, Fecha: {reg.fecha}, Resumen: {reg.resumen_dia}"
                
                ui.label(info).classes("text-body1 ml-4")
        else:
            ui.label("No hay registros en la base de datos.").classes("text-body1 mt-4")
    except Exception as e:
        ui.label(f"Error al obtener datos: {str(e)}").classes("text-negative")