from nicegui_router import Server
from pathlib import Path

# Initialize the router with the directory containing your route files
server = Server(
    title='Servidor de Jose', 
    routes_dir=Path(__file__).parent / "rutas"
)

# Get the Fastapi app instance (for advanced use cases)
app = server.app

# Start the server if the script is run directly
if __name__ == '__main__':
    server.listen(port=8080)