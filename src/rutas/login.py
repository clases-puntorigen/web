from nicegui_router import page, ui, component, use_state

def formulario_login(on_submit):
    def on_login():
        if username.value and password.value:
            on_submit({"username": username.value, "password": password.value})

    with ui.card(align_items="center").classes(
        "absolute-center w-[300px] ma-0"
    ).style(
        "background-color: #FFF; padding:0 0 0 0;"
    ):
        with ui.card_section().classes("w-full pa-0").style("background-color: #000; margin: 0;"):            
            ui.label("Acceso Restringido").classes("text-h6 q-mb-xs text-center text-white")
            #ui.image("assets/logo/rect.png").classes('w-full object-cover')

        with ui.card_section().classes("w-full").style("background-color: #FFF; padding-top: 20px; padding-bottom: 20px;"):
            username = ui.input("Usuario")
            password = ui.input(
                "Contraseña", password=True, password_toggle_button=True
            ).on("keydown.enter", on_login)
        with ui.card_actions().style("background-color: #fff; padding-bottom: 10px;"):
            ui.button("Ingresar", on_click=on_login).props("flat") 

@page("/")
async def login():
    with ui.image("https://picsum.photos/seed/13/800/600?blur=1").classes(
        "absolute-full object-cover"
    ):
        def form_enviado(datos):
            ui.notify(f"Username: {datos["username"]}, Password: {datos["password"]}")
            ui.navigate.to("/logged")

        formulario_login(form_enviado)