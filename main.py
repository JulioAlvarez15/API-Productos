
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, dtos
import Productos.crud as crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/productos", response_model=list[dtos.ProductoResponse]) 
def get_all_productos(db: Session = Depends(get_db)):
    productos = crud.get_productos(db)
    return productos

@app.get("/productos/{producto_id}", response_model=dtos.ProductoResponse) 
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.find_producto(db, producto_id)
    
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.post("/productos", response_model=dtos.ProductoResponse)
def add_producto(producto: dtos.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, producto)

@app.put("/productos/{producto_id}", response_model=dtos.ProductoResponse)
def update_producto(producto_id: int, producto: dtos.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.actualizar_producto(db, producto_id, producto)
    
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.delete("/productos/{producto_id}", response_model=dtos.ProductoResponse)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.eliminar_producto(db, producto_id)
    
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto