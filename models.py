from sqlalchemy import Column,String , Integer 
#from db import Base,engine
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from app import db

mscotas =db.Table('mascotas',
db.Column('idmascota',db.Integer,autoincrement=True , primary_key=True),
db.Column('nombre',db.String(45)),
db.Column('tipo_mascota',db.Integer,db.ForeignKey('tipo_mascota.idtipo_mascota')),
db.Column('propietario',db.Integer,db.ForeignKey('propietario.idpropietario')),

)
class Propietario(db.Model):
    __tablename__ = 'propietario'
    idpropietario = db.Column(db.Integer,autoincrement=True , primary_key=True)
    nombre = db.Column(db.String(45),unique=True)
    direccion = db.Column(db.String(45))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.Text)
    mascotas = db.relationship('tipo_mascota',secondary=mscotas,backref=db.backref('mstas',lazy='dinamic'))
class TipoMascota(db.Model):
    __tablename__='tipo_mascota'
    idtipo_mascota = db.Column(db.Integer,autoincrement=True , primary_key=True)
    descripcion = db.Column(db.String(45))

#Base.metadata.create_all(engine)