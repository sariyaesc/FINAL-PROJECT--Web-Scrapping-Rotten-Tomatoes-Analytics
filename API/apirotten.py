from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3


app=FastAPI()

class Datos(BaseModel):
    id:int
    titulo:str
    critica:int or str
    audiencia:int or str
    estreno: str 

@app.post("/agregar/")
async def agregar_datos(datos: Datos):
    conn=sqlite3.connect('pruebatomato.db')
    cursor=conn.cursor()
    cursor.execute("INSERT INTO datos (titulo,critica,audiencia,estreno) VALUES (?, ?, ?,?)",(datos.titulo,datos.critica,datos.audiencia,datos.estreno))
    conn.commit()
    conn.close()    
    return {"mensaje":"Datos agregados exitosamente"}

@app.get("/datos/")
async def obtener_todos_datos():
    conn = sqlite3.connect('pruebatomato.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"id": resultado[0], "titulo": resultado[1], "critica": resultado[2], "audiencia": resultado[3], "estreno": resultado[4]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

@app.put("/actualizar/{id}/")
async def actualizar_datos(id: int,datos:Datos):
    conn=sqlite3.connect("billboard100.db")
    cursor=conn.execute()
    cursor.execute("UPDATE usuarios SET titulo=?,critica=?,audiencia=?,estreno=? WHERE id=?",{datos.titulo, datos.critica, datos.audiencia, datos.estreno,id})

@app.delete ("/eliminar/{id}/")
async def eliminar_datos(id:int):
    conn=sqlite3.connect("billboard100.db") 
    cursor=conn.execute()
    cursor.execute("DELETE FROM usuarios WHERE id-?",(id,))
    conn.commit()
    conn.close()
    return {"mensaje":"Datos eliminados exitosamente"}  