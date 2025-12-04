from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.database.connection import Base

class Paquete(Base):
    __tablename__ = "paquetes"

    # Campos existentes y correctos
    id = Column(Integer, primary_key=True, index=True)
    
    # Campo 1: CORRECCIÓN. El modelo lo llama 'codigo', la DB lo llama 'id_unico_paquete'.
    # Usaremos el nombre de la DB para la columna, manteniendo el nombre 'codigo' si es necesario para el ORM
    # La forma más simple es renombrar el atributo Python para que coincida con la DB.
    id_unico_paquete = Column(String(50), unique=True, index=True, nullable=False)
    
    descripcion = Column(String(255), nullable=True)
    direccion_destino = Column(Text, nullable=False)
    
    # Campos que la DB NO tiene, eliminados o comentados para evitar el error 1054
    # ciudad = Column(String(100), nullable=True) 
    # estado_region = Column(String(100), nullable=True)
    # codigo_postal = Column(String(20), nullable=True)
    
    # Campo 2: CORRECCIÓN. El modelo lo llama 'nombre_destinatario', la DB lo llama 'destinatario_nombre'.
    destinatario_nombre = Column(String(100), nullable=True) 
    
    # Campo 3: CORRECCIÓN. El modelo lo llama 'creado_en', la DB lo llama 'created_at'.
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    
    # NOTA: Tu tabla 'paquetes' también tiene 'agente_id', 'estado', y 'fecha_asignacion'. 
    # Asegúrate de que estos estén también en tu modelo si son requeridos por SQLAlchemy.
    # agente_id = Column(Integer, ForeignKey("agentes.id"), nullable=True)
    # estado = Column(Enum('ASIGNADO', 'EN_TRANSITO', 'ENTREGADO', 'FALLIDO'), nullable=False, server_default='ASIGNADO')
    # fecha_asignacion = Column(DateTime, nullable=False, server_default=func.now())
