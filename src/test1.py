from nicegui import ui

# Codigo nativo de nicegui

@ui.page("/", title="Mi pagina")
def index():
    ui.colors(accent='#6AD4DD')

    with ui.page_sticky(x_offset=18, y_offset=18) as sticky:
        ui.button(icon='home', on_click=lambda: ui.notify('home')) \
            .props('fab color=accent')
        
@ui.page("/otra")
def otradiferente():
    with ui.row():
        ui.button("Este es el boton")
        ui.label(f"Hola soy otra pagina").style("color: red")
        ui.button("Este es el boton")

ui.run(port=3000)