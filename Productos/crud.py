
from sqlalchemy.orm import Session
from models import Producto
import dtos

def get_productos(db: Session):
    return db.query(Producto).all()

def find_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, producto: dtos.ProductoCreate):
    db_producto = Producto(nombre=producto.nombre, precio=producto.precio)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def actualizar_producto(db: Session, producto_id: int, producto: dtos.ProductoCreate):
    db_producto = find_producto(db, producto_id)
    
    if db_producto is None:
        return None
    
    db_producto.nombre = producto.nombre
    db_producto.precio = producto.precio
    db.commit()
    db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = find_producto(db, producto_id)
    
    if db_producto is None:
        return None
    
    db.delete(db_producto)
    db.commit()
    return db_producto

