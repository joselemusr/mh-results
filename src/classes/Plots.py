
from sqlalchemy import text
import json
import numpy as np

from sqlalchemy.sql import text
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.pyplot as plt

class Plots():
    """
    Clase para generar distintos plots de los experimentos
    """
    
    def __init__(self, engine):
        self.engine = engine
        
        self.diversityMetrics_ = ['DimensionalHussain',
                                  'PesosDeInercia',
                                  'LeungGaoXu',
                                  'Entropica',
                                  'Hamming',
                                  'MomentoDeInercia'
                                 ]

        
    
    def diversityPlots(self, instance, algorithm):
    
        self.sql_ = f"""
           WITH ejecucion AS (
        
                SELECT id_ejecucion
                
                FROM mh_ejecucion
                
                WHERE 1=1
                    AND mh_ejecucion.parametros ILIKE :instance
                    AND mh_ejecucion.nombre_algoritmo = :algorithm
            )

            SELECT i.parametros_iteracion
            FROM mh_ejecucion_iteracion i
            INNER JOIN ejecucion e ON e.id_ejecucion=i.id_ejecucion
            ORDER BY i.numero_iteracion ASC
        """
        params = {'instance':f"%{instance.replace('.txt','')}%", 
                  'algorithm': algorithm}
        
        data = self.engine.execute(text(self.sql_), **params)
        
        for metric in self.diversityMetrics_:
            fig, ax = plt.subplots()
            idx = 0
            diversidad = []
            for result in data:
                fila = json.loads(list(dict(result).values()))
                # print(f"fila['PorcentajeExplor']: {fila['PorcentajeExplor']}")
                # print(f"fila['PorcentajeExplor']: {list(fila['PorcentajeExplor'].replace('[','').replace(']','').split(' '))}")
                diversidadBD = list(fila['Diversidades'].replace("[","").replace("]","").split(" ")) #[0, , , ,1,2,3,4,5]
                diversidadBD = np.array([float(item) for item in diversidadBD if item != ""])                
                diversidad.append(diversidadBD)
                
            diversidadGrafico = np.array(diversidad)
        
            plt.plot(np.arange(diversidadGrafico.shape[0]),diversidadGrafico[:,idx])