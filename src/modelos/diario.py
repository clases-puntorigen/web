from async_easy_model import EasyModel, db_config, init_db
from sqlmodel import Relationship, Field
from typing import List, Optional
from datetime import datetime, date
from enum import Enum
#from sqlalchemy import Enum

db_config.configure_sqlite("diario.db")

class EstadoAnimo(str, Enum):
    """Enumeración para representar el estado de ánimo."""
    EXCELENTE = "excelente"
    BUENO = "bueno"
    NEUTRAL = "neutral"
    REGULAR = "regular"
    MALO = "malo"

class EntradaDiario(EasyModel, table=True):
    """
    Representa una entrada individual en el diario.
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    titulo: str = Field(..., min_length=3, description="Título de la entrada")
    contenido: str = Field(..., min_length=10, description="Contenido de la entrada")
    #type: str = Field(default='user', sa_column=Enum('user', 'admin', name='user_type'))
    estado_animo: str = Field(
        default="neutral",
        sa_column=Enum("excelente","bueno","neutral","regular","malo"),
        description="Estado de ánimo al momento de escribir"
    )
    fecha_creacion: datetime = Field(
        default_factory=datetime.now,
        description="Fecha y hora de creación",
        exclude=True  # No pedir al usuario
    )
    etiquetas: str = Field(
        description="Lista de etiquetas separadas por comas (opcional)"
    )
    registro_id: Optional[int] = Field(default=None, foreign_key="registrodiario.id")
    registro: Optional["RegistroDiario"] = Relationship(back_populates="entradas")

class RegistroDiario(EasyModel, table=True):
    """
    Representa el registro completo del diario, organizado por fecha.
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    fecha: date = Field(
        default_factory=date.today,
        description="Fecha del registro"
    )
    entradas: List["EntradaDiario"] = Relationship(back_populates="registro")
    resumen_dia: Optional[str] = Field(
        None,
        description="Resumen opcional del día completo"
    )