import os
from src.utils.db import engine
from src.utils.dicts import repairs_, instances_
from src.classes.Plots import Plots

if __name__ == '__main__':
   
    plots = ['DiverisityPlot']
    experiments = ['WOA_SCP_SAR_C']
    path_reports = os.environ['PATH_REPORTS']
    
    for exp in experiments:
    
        experiment = exp.split('_')
        metaheuristic = '_'.join(experiment[0:3])
        
        # Limpiamos nombre
        repair = repairs_[experiment[3]]
        path_reports += metaheuristic
        
        try:
            os.makedirs(str(path_reports))
        except OSError:
            print("Directory exists %s " % path_reports)
            
        plot = Plots(engine)
        
        for instance in instances_(): 
            plot.diversityPlots(instance,metaheuristic)
            break