from nicegui_router import page, ui
from nicegui import app
from modelos.diario import RegistroDiario, EntradaDiario
from pathlib import Path
from datetime import datetime

static_path = Path(__file__).parent.parent / "otros"
print("El ****static path**** es:",static_path)
app.add_static_files("/otros", static_path)

def lottie(src, classes="w-24"):
    ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>')
    ui.html(f'<lottie-player src="{src}" loop autoplay />').classes(classes)

@page("/", title="Diario de Vida")
async def inicio():
    fecha_hoy = datetime.today().date()

    with ui.header(fixed=True):
        lottie('/otros/librito.json')
        ui.label("Diario de Vida").classes("text-h4 mt-6")
        ui.space()
        ui.button(text="Registrar Evento").props("flat").classes("text-white mt-6")
    
    try:
        @ui.refreshable
        async def informe_del_dia(fecha="2025-02-27"):
            with ui.element("p"):
                ui.label("Informe del día").classes("text-h4 mb-4")
                dia = await RegistroDiario.get_by_attribute(fecha=fecha)
                with ui.timeline(side="right", color="cyan"):
                    if dia:
                        datos = await EntradaDiario.get_by_attribute(all=True, registro=dia)
                        if datos:
                            for dato in datos:
                                fechahora_formateada = dato.fecha_creacion.strftime("%d %b, %Y %H:%M") 
                                ui.timeline_entry(title=dato.titulo, subtitle=fechahora_formateada, body=dato.contenido)
                        else:
                            ui.timeline_entry(subtitle="No hay entradas para esta fecha.")
                    else:
                        ui.timeline_entry(subtitle="No hay registros para esta fecha.")

        @ui.refreshable
        async def resumen_del_dia(fecha="2025-02-27"):
            with ui.element("div").classes("w-full flex justify-center"):
                with ui.element("div").classes("text-center"):
                    datos = await RegistroDiario.get_by_attribute(fecha=fecha)
                    if datos:
                        ui.markdown("**Resumen del dia**").classes("text-h6")
                        ui.label(f"{datos.resumen_dia}").classes("text-body1")            
                    else:
                        ui.label("No hay registros para esta fecha.").classes("text-body1")

        async def on_date_change(e):
            # Don't await the refresh calls since they don't return anything
            resumen_del_dia.refresh(e.value)
            informe_del_dia.refresh(e.value)

        with ui.row():
            with ui.column():
                ui.date(value=fecha_hoy, on_change=on_date_change) 
                await resumen_del_dia(fecha_hoy)
            await informe_del_dia(fecha_hoy)

    except Exception as e:
        ui.label(f"Error al obtener datos: {str(e)}").classes("text-negative")