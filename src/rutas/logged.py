from nicegui_router import page, ui, component, use_state
from componentes.dynamic_menu import DynamicMenu

def renderizar(nombre):
    contenido_pagina = f"""
        # Bienvenido a mi pagina web
        ## Esta es la pagina de {nombre}
        {nombre} era un **joven travieso** que le gustaba jugar con sus amigos.
        En esta pagina podras encontrar muchas cosas interesantes.
    """
    return contenido_pagina

def pagina_uno():
    """[home]Primero: Pagina de inicio"""
    ui.markdown("Contenido del sector UNO")

def sector_dos():
    """[home]Otro: Otra pagina"""
    ui.markdown("Otro contenido")


@page('/')
def logged():
    menu = [
        "Pruebas",
        pagina_uno,
        sector_dos,
        "Tres",
        "Cuatro",
    ]
    opcion_visible = pagina_uno

    @ui.refreshable
    def renderizar():
        nonlocal opcion_visible
        opcion_visible()

    with ui.header(elevated=True).classes("bg-secondary"):
        ui.button(icon="menu", on_click=lambda: left_drawer.toggle())
        ui.space()
        ui.label("Bienvenido a la pagina de Jose").classes("text-h5 mt-1").style("color: #FEFE00")

    with ui.left_drawer(fixed=True).classes("bg-primary").props("bordered") as left_drawer:
        def on_item_click(item):
            nonlocal opcion_visible
            opcion_visible = item
            renderizar.refresh()
            
        DynamicMenu(menu=menu, on_item_click=lambda item: on_item_click(item))
    
    renderizar()
