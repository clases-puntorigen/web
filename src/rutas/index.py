from nicegui_router import page, ui
from nicegui import app
from modelos.diario import RegistroDiario
from pathlib import Path

static_path = Path(__file__).parent.parent / "otros"
print("El ****static path**** es:",static_path)
app.add_static_files("/otros", static_path)

def lottie(src, classes="w-24"):
    ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>')
    ui.html(f'<lottie-player src="{src}" loop autoplay />').classes(classes)

@page("/", title="Diario de Vida")
async def inicio():
    with ui.header(fixed=True):
        lottie('/otros/librito.json')
        ui.label("Diario de Vida").classes("text-h4 mt-6")
        ui.space()
        ui.button(text="Registrar Evento").props("flat").classes("text-white mt-6")
    
    try:
        datos = await RegistroDiario.get_by_attribute(all=True, fecha="2025-02-27")
        ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
        result = ui.label()

        # Convert the data to a string representation
        if datos:
            ui.label("Registros encontrados:").classes("text-h5 mt-4")
            for reg in datos:
                info = f"ID: {reg.id}, Fecha: {reg.fecha}, Resumen: {reg.resumen_dia}"
                
                ui.label(info).classes("text-body1 ml-4")
        else:
            ui.label("No hay registros en la base de datos.").classes("text-body1 mt-4")
    except Exception as e:
        ui.label(f"Error al obtener datos: {str(e)}").classes("text-negative")