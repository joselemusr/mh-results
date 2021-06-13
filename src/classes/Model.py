import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import LargeBinary

Base = declarative_base()

class Ejecucion(Base):
    
    __tablename__ = 'mh_ejecucion'
    id_ejecucion = Column(String(), primary_key=True)
    nombre_algoritmo = Column(String())
    parametros = Column(Text())
    inicio = Column(DateTime())
    fin = Column(DateTime())
    estado = Column(String())
    
    def toJSON(self):   
        json = {
            'id_ejecucion':self.id_ejecucion,
            'nombre_algoritmo':self.nombre_algoritmo,
            'parametros':self.parametros,
            'inicio':self.inicio,
            'fin':self.fin,
            'estado':self.estado
        }
        return json
    
class EjecucionResultado(Base):
    
    __tablename__ = 'mh_ejecucion_resultado'
    id = Column(String(), primary_key=True)
    id_ejecucion = Column(String()) #,ForeignKey('mh_ejecucion.id_ejecucion')
    fitness = Column(Float())
    inicio = Column(DateTime())
    fin = Column(DateTime())
    mejor_solucion = Column(Text())

    def toJSON(self):   
        json = {
            "id":self.id,
            "id_ejecucion":self.id_ejecucion,
            'fitness':self.fitness,
            'inicio':self.inicio,
            'fin':self.fin,
            'mejor_solucion':self.mejor_solucion
        }
        return json
    
class EjecucionIteracion(Base):
    
    __tablename__ = 'mh_ejecucion_iteracion'
    id = Column(String(), primary_key=True)
    id_ejecucion = Column(String()) # ,ForeignKey('mh_ejecucion.id_ejecucion')
    numero_iteracion = Column(Integer())
    fitness_mejor = Column(Float())
    fitness_promedio = Column(Float())
    fitness_mejor_iteracion = Column(Float())
    parametros_iteracion =  Column(Text())
    inicio = Column(DateTime())
    fin = Column(DateTime())
    datos_iternos = Column(LargeBinary())

    def toJSON(self):   
        json = {
            "id":self.id,
            "id_ejecucion":self.id_ejecucion,
            'numero_iteracion':self.numero_iteracion,
            'fitness_mejor':self.fitness_mejor,
            'fitness_promedio': self.fitness_promedio,
            'fitness_mejor_iteracion': self.fitness_mejor_iteracion,
            'parametros_iteracion':self.parametros_iteracion,
            'inicio': self.inicio,
            'fin': self.fin,
            'datos_internos':self.datos_internos
        }
        return json