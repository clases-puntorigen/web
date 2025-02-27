from nicegui_router import Server
from pathlib import Path
import asyncio
from async_easy_model import init_db, db_config
from modelos.diario import EntradaDiario, RegistroDiario

# Define the startup function before using it
async def startup_db_client():
    # The database is already configured in the models file
    # Just initialize the database
    await init_db()
    print("Database initialized")

# Initialize the router with the directory containing your route files
server = Server(
    title='Servidor de Jose', 
    routes_dir=Path(__file__).parent / "rutas",
    on_startup=startup_db_client
)

# Get the Fastapi app instance (for advanced use cases)
app = server.app

# Start the server if the script is run directly
if __name__ == '__main__':
    server.listen(port=8080)