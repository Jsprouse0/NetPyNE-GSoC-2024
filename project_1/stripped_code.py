"""
# ----------------------------------------------------------------------------------------------
# EPSPs via NetStim (batch.py)
# ----------------------------------------------------------------------------------------------
def EPSPs():
    params = specs.ODict()

    params['groupWeight'] = [x*0.05 for x in np.arange(1, 8, 1)]
    params['ihGbar'] = [0.0, 1.0]
 
    
    # initial config
    initCfg = {}
    initCfg['duration'] = 0.5*1e3
    initCfg['addIClamp'] = False
    initCfg['addNetStim'] = True
    initCfg[('GroupNetStimW1', 'pop')] = 'PT5B'
    initCfg[('analysis','plotTraces','timeRange')] = [0, 500]
    initCfg['excTau2Factor'] = 2.0
    initCfg['weightNorm'] = True
    initCfg['stimSubConn'] = False
    initCfg['ihGbarZD'] = None

    groupedParams = [] 

    b = Batch(params=params, netParamsFile='netParams_cell.py', cfgFile='cfg_cell.py', initCfg=initCfg,
              groupedParams=groupedParams)

    return b
"""


"""
# ----------------------------------------------------------------------------------------------
# f-I curve (batch.py)
# ----------------------------------------------------------------------------------------------
def fIcurve():
    params = specs.ODict()

    params[('IClamp1', 'pop')] = ['IT2', 'IT4', 'IT5A', 'IT5B', 'PT5B', 'IT6', 'CT6', 'PV2', 'SOM2']
    params[('IClamp1', 'amp')] = list(np.arange(0.0, 6.5, 0.5)/10.0) 
    #params['ihGbar'] = [0.0, 1.0, 2.0]
    # params['axonNa'] = [5, 6, 7, 8] 
    # params['gpas'] = [0.6, 0.65, 0.70, 0.75] 
    # params['epas'] = [1.0, 1.05] 
    # params['ihLkcBasal'] = [0.0, 0.01, 0.1, 0.5, 1.0] 

    # initial config
    initCfg = {}
    initCfg['duration'] = 1.5*1e
    initCfg['addIClamp'] = True
    initCfg['addNetStim'] = False
    initCfg['weightNorm'] = True
    initCfg[('IClamp1','sec')] = 'soma'
    initCfg[('IClamp1','loc')] = 0.5
    initCfg[('IClamp1','start')] = 500
    initCfg[('IClamp1','dur')] = 1000
    initCfg[('analysis','plotTraces','timeRange')] = [0, 1500]

    groupedParams = [] 

    b = Batch(params=params, netParamsFile='netParams_cell.py', cfgFile='cfg_cell.py', initCfg=initCfg, groupedParams=groupedParams)

    return b

"""


"""
# ----------------------------------------------------------------------------------------------
# Custom (batch.py)
# ----------------------------------------------------------------------------------------------
def custom():
    params = specs.ODict()
    # # long-range inputs
    # params[('weightLong', 'TPO')] = [0.25, 0.5, 0.75]
    # params[('weightLong', 'TVL')] = [0.25, 0.5, 0.75]
    # params[('weightLong', 'S1')] =  [0.25, 0.5, 0.75]
    # params[('weightLong', 'S2')] =  [0.25, 0.5, 0.75]
    # params[('weightLong', 'cM1')] = [0.25, 0.5, 0.75]
    # params[('weightLong', 'M2')] =  [0.25, 0.5, 0.75]
    # params[('weightLong', 'OC')] =  [0.25, 0.5, 0.75]

    # EEgain
    params['EEGain'] = [1.0]

    # IEgain
    ## L2/3+4
    params[('IEweights', 0)] = [1.0]
    ## L5
    params[('IEweights', 1)] = [1.0]  # [0.8, 1.0]
    ## L6
    params[('IEweights', 2)] = [1.0]  # [0.8, 1.0]

    # IIGain
    params['IIGain'] = [1.0]

    groupedParams = [('weightLong', 'TPO'),
                     ('weightLong', 'TVL'),
                     ('weightLong', 'S1'),
                     ('weightLong', 'S2'),
                     ('weightLong', 'cM1'),
                     ('weightLong', 'M2'),
                     ('weightLong', 'OC')]

    # --------------------------------------------------------
    # initial config
    initCfg = {}
    initCfg['duration'] = 1000
    initCfg['printPopAvgRates'] = [500, 1000]
    initCfg['dt'] = 0.025

    initCfg['scaleDensity'] = 1.0

    # cell params
    initCfg['ihGbar'] = 0.75  # ih (for quiet/sponti condition)
    initCfg['ihModel'] = 'migliore'  # ih model
    initCfg['ihGbarBasal'] = 1.0  # multiplicative factor for ih gbar in PT cells
    initCfg['ihlkc'] = 0.2  # ih leak param (used in Migliore)
    initCfg['ihLkcBasal'] = 1.0  # multiplicative factor for ih lk in PT cells
    initCfg['ihLkcBelowSoma'] = 0.01  # multiplicative factor for ih lk in PT cells
    initCfg['ihlke'] = -86  # ih leak param (used in Migliore)
    initCfg['ihSlope'] = 28  # ih leak param (used in Migliore)

    initCfg['somaNa'] = 5.0  # somatic Na conduct
    initCfg['dendNa'] = 0.3  # dendritic Na conduct (reduced to avoid dend spikes)
    initCfg['axonNa'] = 7  # axon Na conduct (increased to compensate)
    initCfg['axonRa'] = 0.005
    initCfg['gpas'] = 0.5
    initCfg['epas'] = 0.9

    # long-range input params
    initCfg['numCellsLong'] = 1000
    initCfg[('pulse', 'pop')] = 'None'
    initCfg[('pulse', 'start')] = 1000.0
    initCfg[('pulse', 'end')] = 1100.0
    initCfg[('pulse', 'noise')] = 0.8

    # conn params
    initCfg['IEdisynapticBias'] = None

    initCfg['weightNormThreshold'] = 4.0
    initCfg['IEGain'] = 1.0
    initCfg['IPTGain'] = 1.0
    initCfg['IIweights'] = [1.0, 1.0, 1.0]

    # plotting and saving params
    initCfg[('analysis', 'plotRaster', 'timeRange')] = initCfg['printPopAvgRates']
    initCfg[('analysis', 'plotTraces', 'timeRange')] = initCfg['printPopAvgRates']

    initCfg[('analysis', 'plotTraces', 'oneFigPer')] = 'trace'

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg,
              groupedParams=groupedParams)
    b.method = 'grid'

    return b
"""


"""
# ----------------------------------------------------------------------------------------------
# Evol (batch.py)
# ----------------------------------------------------------------------------------------------
def evolRates():
    # --------------------------------------------------------
    # parameters
    params = specs.ODict()

    # long-range inputs
    params[('weightLong', 'TPO')] = [0.25, 0.75]
    params[('weightLong', 'TVL')] = [0.25, 0.75]
    params[('weightLong', 'S1')] = [0.25, 0.75]
    params[('weightLong', 'S2')] = [0.25, 0.75]
    params[('weightLong', 'cM1')] = [0.25, 0.75]
    params[('weightLong', 'M2')] = [0.25, 0.75]
    params[('weightLong', 'OC')] = [0.25, 0.75]

    # EEgain
    params[('EEGain')] = [0.5, 1.5]

    # IEgain
    ## L2/3+4
    params[('IEweights', 0)] = [0.5, 1.5]
    ## L5
    params[('IEweights', 1)] = [0.5, 1.5]  # [0.8, 1.0]
    ## L6
    params[('IEweights', 2)] = [0.5, 1.5]  # [0.8, 1.0]

    # IIGain
    ## L2/3+4
    params[('IIweights', 0)] = [0.5, 1.5]
    ## L5
    params[('IIweights', 1)] = [0.5, 1.5]  # [0.8, 1.0]
    ## L6
    params[('IIweights', 2)] = [0.5, 1.5]  # [0.8, 1.0]

    groupedParams = []

    # --------------------------------------------------------
    # initial config
    initCfg = {}
    initCfg['duration'] = 1500
    initCfg['printPopAvgRates'] = [500, 1500]
    initCfg['dt'] = 0.025

    initCfg['scaleDensity'] = 1.0

    # cell params
    initCfg['ihGbar'] = 0.75  # ih (for quiet/sponti condition)
    initCfg['ihModel'] = 'migliore'  # ih model
    initCfg['ihGbarBasal'] = 1.0  # multiplicative factor for ih gbar in PT cells
    initCfg['ihlkc'] = 0.2  # ih leak param (used in Migliore)
    initCfg['ihLkcBasal'] = 1.0  # multiplicative factor for ih lk in PT cells
    initCfg['ihLkcBelowSoma'] = 0.01  # multiplicative factor for ih lk in PT cells
    initCfg['ihlke'] = -86  # ih leak param (used in Migliore)
    initCfg['ihSlope'] = 28  # ih leak param (used in Migliore)

    initCfg['somaNa'] = 5.0  # somatic Na conduct
    initCfg['dendNa'] = 0.3  # dendritic Na conduct (reduced to avoid dend spikes)
    initCfg['axonNa'] = 7  # axon Na conduct (increased to compensate)
    initCfg['axonRa'] = 0.005
    initCfg['gpas'] = 0.5
    initCfg['epas'] = 0.9

    # long-range input params
    initCfg['numCellsLong'] = 1000
    initCfg[('pulse', 'pop')] = 'None'
    initCfg[('pulse', 'start')] = 1000.0
    initCfg[('pulse', 'end')] = 1100.0
    initCfg[('pulse', 'noise')] = 0.8

    # conn params
    initCfg['IEdisynapticBias'] = None

    initCfg['weightNormThreshold'] = 4.0
    initCfg['IEGain'] = 1.0
    initCfg['IIGain'] = 1.0
    initCfg['IPTGain'] = 1.0

    # plotting and saving params
    initCfg[('analysis', 'plotRaster', 'timeRange')] = initCfg['printPopAvgRates']
    initCfg[('analysis', 'plotTraces', 'timeRange')] = initCfg['printPopAvgRates']

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    # --------------------------------------------------------
    # fitness function
    fitnessFuncArgs = {}
    pops = {}

    ## Exc pops
    Epops = ['IT2', 'IT4', 'IT5A', 'IT5B', 'PT5B', 'IT6', 'CT6']

    Etune = {'target': 5, 'width': 5, 'min': 0.5}
    for pop in Epops:
        pops[pop] = Etune

    ## Inh pops
    Ipops = ['PV2', 'SOM2',
             'PV5A', 'SOM5A',
             'PV5B', 'SOM5B',
             'PV6', 'SOM6']

    Itune = {'target': 10, 'width': 15, 'min': 0.25}
    for pop in Ipops:
        pops[pop] = Itune

    fitnessFuncArgs['pops'] = pops
    fitnessFuncArgs['maxFitness'] = 1000

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        popFitness = [min(np.exp(abs(v['target'] - simData['popRates'][k]) / v['width']), maxFitness)
                      if simData['popRates'][k] > v['min'] else maxFitness for k, v in pops.items()]
        fitness = np.mean(popFitness)

        popInfo = '; '.join(
            ['%s rate=%.1f fit=%1.f' % (p, simData['popRates'][p], popFitness[i]) for i, p in enumerate(pops)])
        print('  ' + popInfo)
        return fitness

    # from IPython import embed; embed()

    b = Batch(params=params, groupedParams=groupedParams, initCfg=initCfg)
    b.method = 'evol'

    # Set evol alg configuration
    b.evolCfg = {
        'evolAlgorithm': 'custom',
        'fitnessFunc': fitnessFunc,  # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'pop_size': 15,
        'num_elites': 2,
        'mutation_rate': 0.5,
        'crossover': 0.5,
        'maximize': False,  # maximize fitness function?
        'max_generations': 100,
        'time_sleep': 3 * 300,  # 5min wait this time before checking again if sim is completed (for each generation)
        'maxiter_wait': 3 * 64,  # (5h20) max number of times to check if sim is completed (for each generation)
        'defaultFitness': 1000,  # set fitness value in case simulation time is over
        'scancelUser': 'ext_romanbaravalle_gmail_com'
    }

    return b
"""


"""
# ----------------------------------------------------------------------------------------------
# v56_batch7 - Figure 2 (Control Quiet) (5*5 seeds) (batch.py)
#
# Note: v56_batch18 is the same but recording only 1 seed and more voltage traces
# ----------------------------------------------------------------------------------------------
def v56_batch7():

    params = specs.ODict()

    params['ihGbar'] = [1e-6, 0.25, 0.5, 0.75, 1.0] #, 0.25, 0.5, 0.75, 1.0]   #[0.25] # [0, 0.25] 
    
    params[('seeds', 'conn')] = [4321+(17*i) for i in range(5)]
    params[('seeds', 'stim')] = [1234+(17*i) for i in range(5)]
    
    groupedParams = []

    # initial config
    initCfg = {}
    duration = 5*1e3
    initCfg['duration'] = duration
    initCfg[('analysis', 'plotRaster', 'timeRange',0)] = 1000
    initCfg[('analysis', 'plotLFP', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotTraces', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotRaster', 'timeRange',1)] = duration
    initCfg[('analysis', 'plotLFP', 'timeRange', 1)] = duration
    initCfg[('analysis', 'plotTraces', 'timeRange', 1)] = duration

    initCfg['ihGbar'] = 0.75
    # initCfg[('modifyMechs', 'startTime')] = 1500
    # initCfg[('modifyMechs', 'endTime')] = 3000
    # initCfg[('modifyMechs', 'origFactor')] = initCfg['ihGbar']

    initCfg['weightNormThreshold'] = 4.0
    initCfg['EEGain'] = 0.5 
    initCfg['IEGain'] = 1.0
    initCfg['IIGain'] = 1.0
    initCfg['IPTGain'] = 1.0

    #initCfg[('ratesLong', 'TPO', 1)] = 5
    #initCfg[('ratesLong', 'TVL', 1)] = 2.5
    #initCfg[('ratesLong', 'S1', 1)] = 5
    #initCfg[('ratesLong', 'S2', 1)] = 5
    #initCfg[('ratesLong', 'cM1', 1)] = 2.5
    #initCfg[('ratesLong', 'M2', 1)] = 2.5
    #initCfg[('ratesLong', 'OC', 1)] = 5
    
    # initCfg[('pulse', 'pop')] = 'TVL'
    # initCfg[('pulse', 'rate')] = [0, 10.0]
    # initCfg[('pulse', 'start')] = 1500.0
    # initCfg[('pulse', 'end')] = 3000.0
    # initCfg[('pulse', 'noise')] = 1.0

    # # L2/3+4
    initCfg[('IEweights',0)] =  0.8
    initCfg[('IIweights',0)] =  1.2 
    # L5
    initCfg[('IEweights',1)] = 0.8   
    initCfg[('IIweights',1)] = 1.0
    # L6
    initCfg[('IEweights',2)] =  1.0  
    initCfg[('IIweights',2)] =  1.0

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    groupedParams = [] #('IEweights',0), ('IIweights',0), ('IEweights',1), ('IIweights',1), ('IEweights',2), ('IIweights',2)]

    b = Batch(params=params, initCfg=initCfg, groupedParams=groupedParams)
    b.batchLabel = 'v56_batch7'

    return b

"""


"""
# ----------------------------------------------------------------------------------------------
# v56_batch19 - Figure 3 (Control Quiet+Move) (batch.py)
#
# Note: v56_batch23 is the same but recording LFPs
# Note: v56_batch39 is the same but recording population LFPs and with recordStep=0.025
#
# ----------------------------------------------------------------------------------------------
def v56_batch19():
    params = specs.ODict()
    
    params[('modifyMechs', 'newFactor')] = [0.25]
    params[('pulse', 'rate', 1)] = [10]

    params[('seeds', 'conn')] = [4321+(17*i) for i in range(5)]
    params[('seeds', 'stim')] = [1234+(17*i) for i in range(5)]

    groupedParams = []

    # initial config
    initCfg = {}
    duration = 13*1e3
    initCfg['duration'] = duration
    initCfg[('analysis', 'plotRaster', 'timeRange',0)] = 1000
    initCfg[('analysis', 'plotLFP', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotTraces', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotRaster', 'timeRange',1)] = duration
    initCfg[('analysis', 'plotLFP', 'timeRange', 1)] = duration
    initCfg[('analysis', 'plotTraces', 'timeRange', 1)] = duration

    initCfg['ihGbar'] = 0.75
    initCfg[('modifyMechs', 'startTime')] = 5000
    initCfg[('modifyMechs', 'endTime')] = 9000
    initCfg[('modifyMechs', 'origFactor')] = initCfg['ihGbar']

    initCfg['weightNormThreshold'] = 4.0
    initCfg['EEGain'] = 0.5 
    initCfg['IEGain'] = 1.0
    initCfg['IIGain'] = 1.0
    initCfg['IPTGain'] = 1.0

    #initCfg[('ratesLong', 'TPO', 1)] = 5
    #initCfg[('ratesLong', 'TVL', 1)] = 2.5
    #initCfg[('ratesLong', 'S1', 1)] = 5
    #initCfg[('ratesLong', 'S2', 1)] = 5
    #initCfg[('ratesLong', 'cM1', 1)] = 2.5
    #initCfg[('ratesLong', 'M2', 1)] = 2.5
    #initCfg[('ratesLong', 'OC', 1)] = 5
    
   # initCfg[('pulse', 'pop')] = 'TVL'
    #initCfg[('pulse', 'rate')] = [0, 10.0]
    #initCfg[('pulse', 'start')] = 5000.0
    #initCfg[('pulse', 'end')] = 9000.0
    #initCfg[('pulse', 'noise')] = 1.0

    # # L2/3+4
    initCfg[('IEweights',0)] =  0.8
    initCfg[('IIweights',0)] =  1.2 
    # L5
    initCfg[('IEweights',1)] = 0.8   
    initCfg[('IIweights',1)] = 1.0
    # L6
    initCfg[('IEweights',2)] =  1.0  
    initCfg[('IIweights',2)] =  1.0

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    groupedParams = [] #('IEweights',0), ('IIweights',0), ('IEweights',1), ('IIweights',1), ('IEweights',2), ('IIweights',2)]

    b = Batch(params=params, initCfg=initCfg, groupedParams=groupedParams)
    b.batchLabel = 'v56_batch19'

    return b

"""


"""

# ----------------------------------------------------------------------------------------------
# v56_batch20 - Figure 5 (MTh Inact Quiet+Move) (batch.py)
# ----------------------------------------------------------------------------------------------

def v56_batch20():
    params = specs.ODict()

    params[('ratesLong', 'TVL', 1)] = [0.01]  #[2.5] # [0.01, 2.5] #[2.5]  #
    params[('ratesLong', 'M2', 1)] = [0.01, 2.5]
    params[('modifyMechs', 'newFactor')] = [0.25] # , 0.5, 0.75, 1.0]  #0.5, 0.75, 1.0]

    params[('seeds', 'conn')] = [4321+(17*i) for i in range(5)]
    params[('seeds', 'stim')] = [1234+(17*i) for i in range(5)]

    groupedParams = []

    # initial config
    initCfg = {}
    duration = 13*1e3
    initCfg['duration'] = duration
    initCfg[('analysis', 'plotRaster', 'timeRange',0)] = 1000
    initCfg[('analysis', 'plotLFP', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotTraces', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotRaster', 'timeRange',1)] = duration
    initCfg[('analysis', 'plotLFP', 'timeRange', 1)] = duration
    initCfg[('analysis', 'plotTraces', 'timeRange', 1)] = duration

    initCfg['ihGbar'] = 0.75
    initCfg[('modifyMechs', 'startTime')] = 5000
    initCfg[('modifyMechs', 'endTime')] = 9000
    initCfg[('modifyMechs', 'origFactor')] = initCfg['ihGbar']

    initCfg['weightNormThreshold'] = 4.0
    initCfg['EEGain'] = 0.5 
    initCfg['IEGain'] = 1.0
    initCfg['IIGain'] = 1.0
    initCfg['IPTGain'] = 1.0

    initCfg[('ratesLong', 'TPO', 1)] = 5 	
    initCfg[('ratesLong', 'TVL', 1)] = 0.01
    initCfg[('ratesLong', 'S1', 1)] = 5
    initCfg[('ratesLong', 'S2', 1)] = 5 
    initCfg[('ratesLong', 'cM1', 1)] = 2.5
    initCfg[('ratesLong', 'M2', 1)] = 2.5
    initCfg[('ratesLong', 'OC', 1)] = 5
    
    initCfg[('pulse', 'pop')] = 'None'
    initCfg[('pulse', 'rate')] = [0, 10.0]
    initCfg[('pulse', 'start')] = 5000.0
    initCfg[('pulse', 'end')] = 9000.0
    initCfg[('pulse', 'noise')] = 1.0

    # # L2/3+4
    initCfg[('IEweights',0)] =  0.8
    initCfg[('IIweights',0)] =  1.2 
    # L5
    initCfg[('IEweights',1)] = 0.8   
    initCfg[('IIweights',1)] = 1.0
    # L6
    initCfg[('IEweights',2)] =  1.0  
    initCfg[('IIweights',2)] =  1.0

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False


    b = Batch(params=params, initCfg=initCfg, groupedParams=groupedParams)
    b.batchLabel = 'v56_batch20'
    
    return b


"""


"""
# ----------------------------------------------------------------------------------------------
# v56_batch22 - Figure 5 (MTh Inact Quiet+Move) (batch.py)
# ----------------------------------------------------------------------------------------------

def v56_batch22():
    params = specs.ODict()

    params[('seeds', 'conn')] = [4321+(17*i) for i in range(5)]
    params[('seeds', 'stim')] = [1234+(17*i) for i in range(5)]

    groupedParams = []

    # initial config
    initCfg = {}
    duration = 13*1e3
    initCfg['duration'] = duration
    initCfg[('analysis', 'plotRaster', 'timeRange',0)] = 1000
    initCfg[('analysis', 'plotLFP', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotTraces', 'timeRange', 0)] = 1000
    initCfg[('analysis', 'plotRaster', 'timeRange',1)] = duration
    initCfg[('analysis', 'plotLFP', 'timeRange', 1)] = duration
    initCfg[('analysis', 'plotTraces', 'timeRange', 1)] = duration

    initCfg['ihGbar'] = 1.0

    initCfg['weightNormThreshold'] = 4.0
    initCfg['EEGain'] = 0.5 
    initCfg['IEGain'] = 1.0
    initCfg['IIGain'] = 1.0
    initCfg['IPTGain'] = 1.0

    initCfg[('ratesLong', 'TPO', 1)] = 5 	
    initCfg[('ratesLong', 'TVL', 1)] = 2.5
    initCfg[('ratesLong', 'S1', 1)] = 5
    initCfg[('ratesLong', 'S2', 1)] = 5 
    initCfg[('ratesLong', 'cM1', 1)] = 2.5
    initCfg[('ratesLong', 'M2', 1)] = 2.5
    initCfg[('ratesLong', 'OC', 1)] = 5
      initCfg[('pulse', 'noise')] = 1.0

    # # L2/3+4
    initCfg[('IEweights',0)] =  0.8
    initCfg[('IIweights',0)] =  1.2 
    # L5
    initCfg[('IEweights',1)] = 0.8   
    initCfg[('IIweights',1)] = 1.0
    # L6
    initCfg[('IEweights',2)] =  1.0  
    initCfg[('IIweights',2)] =  1.0

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    groupedParams = [] #('IEweights',0), ('IIweights',0), ('IEweights',1), ('IIweights',1), ('IEweights',2), ('IIweights',2)]

    b = Batch(params=params, initCfg=initCfg, groupedParams=groupedParams)
    b.batchLabel = 'v56_batch22'

    return b
"""


"""
# ----------------------------------------------------------------------------------------------
# v56_batch5b - Figure 6 (VL vs Ih Quiet+Move) (batch.py)
# ----------------------------------------------------------------------------------------------
def v56_batch5b():
    params = specs.ODict()

    params[('modifyMechs', 'newFactor')] = [1e-6, 0.25, 0.5, 0.75, 1.0]  
    params[('pulse', 'rate', 1)] = [0.01, 2.5, 5, 10, 15, 20, 30] 

    groupedParams = []

    # initial config
    initCfg = {}
    duration = 5*1e3
    initCfg['duration'] = duration
    initCfg[('analysis', 'plotRaster', 'timeRange',0)] = 0
    #initCfg[('analysis', 'plotLFP', 'timeRange', 0)] = 0
    initCfg[('analysis', 'plotTraces', 'timeRange', 0)] = 0
    initCfg[('analysis', 'plotRaster', 'timeRange',1)] = duration
    #initCfg[('analysis', 'plotLFP', 'timeRange', 1)] = duration
    initCfg[('analysis', 'plotTraces', 'timeRange', 1)] = duration

    initCfg['ihGbar'] = 0.75
    initCfg[('modifyMechs', 'startTime')] = 1500
    initCfg[('modifyMechs', 'endTime')] = 3000
    initCfg[('modifyMechs', 'origFactor')] = initCfg['ihGbar']

    initCfg['weightNormThreshold'] = 4.0
    initCfg['EEGain'] = 0.5 
    initCfg['IEGain'] = 1.0
    initCfg['IIGain'] = 1.0
    initCfg['IPTGain'] = 1.0

    initCfg[('ratesLong', 'TPO', 1)] = 5 	
    initCfg[('ratesLong', 'TVL', 1)] = 2.5
    initCfg[('ratesLong', 'S1', 1)] = 5
    initCfg[('ratesLong', 'S2', 1)] = 5 
    initCfg[('ratesLong', 'cM1', 1)] = 2.5
    initCfg[('ratesLong', 'M2', 1)] = 2.5
    initCfg[('ratesLong', 'OC', 1)] = 5
    
    initCfg[('pulse', 'pop')] = 'TVL'
    initCfg[('pulse', 'rate')] = [0, 10.0]
    initCfg[('pulse', 'start')] = 1500.0
    initCfg[('pulse', 'end')] = 3000.0
    initCfg[('pulse', 'noise')] = 1.0

    # # L2/3+4
    initCfg[('IEweights',0)] =  0.8
    initCfg[('IIweights',0)] =  1.2 
    # L5
    initCfg[('IEweights',1)] = 0.8   
    initCfg[('IIweights',1)] = 1.0
    # L6
    initCfg[('IEweights',2)] =  1.0  
    initCfg[('IIweights',2)] =  1.0

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    groupedParams = [] #('IEweights',0), ('IIweights',0), ('IEweights',1), ('IIweights',1), ('IEweights',2), ('IIweights',2)]

    b = Batch(params=params, initCfg=initCfg, groupedParams=groupedParams)

    return b
"""

# ===================================================================================================

# netParams.py stripped code
"""
(netParams_cell.py) Line 83
# cellRule['secs']['axon_0']['geom']['pt3d'] = [[1e30, 1e30, 1e30, 1e30]] #stupid workaround that should be fixed in NetPyNE
# cellRule['secs']['axon_1']['geom']['pt3d'] = [[1e30, 1e30, 1e30, 1e30]] #breaks in simulations btw.


"""


