from nicegui_router import page, ui

@page('/')
def logged():
    with ui.header(elevated=True):
        ui.button(icon="menu", on_click=lambda: left_drawer.toggle())

    with ui.left_drawer(fixed=True).classes("bg-secondary").props("bordered") as left_drawer:
        with ui.list().props("w-full"):
            with ui.item().classes("w-full"):
                with ui.item_section():
                    ui.item_label("Boton 1")
                    ui.item_label("Boton 1")
                    ui.item_label("Boton 1")
