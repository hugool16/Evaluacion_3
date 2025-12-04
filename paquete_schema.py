from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class PaqueteBase(BaseModel):
    # CORREGIDO 1: Cambiado de 'codigo' a 'id_unico_paquete' para coincidir con el modelo.
    id_unico_paquete: str = Field(..., min_length=3, max_length=50) 
    
    descripcion: Optional[str] = Field(None, max_length=255)
    direccion_destino: str
    
    # Estos campos pueden quedarse aunque la DB no los use si son opcionales, 
    # pero si dan problemas, puedes comentarlos.
    ciudad: Optional[str] = None
    estado_region: Optional[str] = None
    codigo_postal: Optional[str] = None
    
    # CORREGIDO 2: Cambiado de 'nombre_destinatario' a 'destinatario_nombre'
    destinatario_nombre: Optional[str] = None 

class PaqueteCreate(PaqueteBase):
    pass

class PaqueteOut(PaqueteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    # CORREGIDO 3: Cambiado de 'creado_en' a 'created_at' para coincidir con el modelo.
    created_at: datetime