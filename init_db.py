import asyncio
from async_easy_model import init_db, db_config
from src.modelos.diario import EntradaDiario, RegistroDiario
import os
from datetime import date

async def main():
    # Remove the existing database file if it exists
    if os.path.exists('diario.db'):
        os.remove('diario.db')
        print("Removed existing database file")

    # Configure the database
    db_config.configure_sqlite("diario.db")
    
    # Initialize the database
    await init_db()
    print("Database initialized")

    # Create a test record
    registro = await RegistroDiario.insert({
        "fecha": date(2025, 2, 27),
        "resumen_dia": "Test day summary"
    })
    print(f"Created test record with ID: {registro.id}")

    # Create a test entry
    entrada = await EntradaDiario.insert({
        "titulo": "Test Entry",
        "contenido": "This is a test entry",
        "estado_animo": "bueno",
        "etiquetas": "test,init",
        "registro_id": registro.id
    })
    print(f"Created test entry with ID: {entrada.id}")

    # We can't directly verify the relationship in this version of the library
    # Just print a success message
    print("Successfully created test data")

if __name__ == "__main__":
    asyncio.run(main())
