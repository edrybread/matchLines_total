#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:13:13 2021

@author: erik
"""
import numpy as np

def matchLines_total(model, data, output):
    
    '''
    Takes two 2D arrays as inputs. Compares the two arrays by matching the
    values of the first column of the two arrays and outputs the values of the 
    second column of the second array and then combines that with the first 
    column of the second array. This is being specifically used to compare the
    wavelengths of the models and the observed data and then outputs the flux 
    values from the model that align with wavelengths that only occur in both 
    arrays. It then returns a 2D array containing the wavelengths present in 
    both arrays in the first column and the flux values present in both arrays
    in the second column. Any non-matching values are given a zero value and 
    then removed before the final 2D array is constructed. Output can be 
    chosen, either data flux or model flux. 1 for data and 0 for model.
    '''
    
    #observed wavelengths
    datawave = np.asarray(data[:, 0])
    # print('datawave =', datawave.size)
    #observed fluxes
    dataflux = np.asarray(data[:, 1])
    # print('dataflux =', dataflux.size)
    #model wavelengths
    modelwave = np.asarray(model[:, 0])
    # print('modelwave =', modelwave.size)
    #model fluxes
    modelflux = np.asarray(model[:, 1])
    # print('modelflux =', modelflux.size)

    
    #empty arrays
    arr = np.array([])
    CorrectedFlux = np.array([])
    CorrectedWave = np.array([])
    if output == 1:
        
        for i in datawave:
    
            Match = (np.absolute(i - modelwave) < 1).nonzero()

            Match = np.array(Match)

            if Match.size == arr.size:
                
                CorrectedFlux = np.append(CorrectedFlux, np.PZERO)

            if Match.size == arr.size:
                
                CorrectedWave = np.append(CorrectedWave, np.PZERO)

            # print('i =', i)
            CorrectedFlux = np.append(CorrectedFlux, dataflux[Match[0]])
            CorrectedWave = np.append(CorrectedWave, modelwave[Match[0]]) 
            # print('Corrected Wave =', CorrectedWave)
             
            
            
        CorrectedFlux = np.delete(CorrectedFlux, np.asarray(CorrectedFlux == 0).nonzero(), axis = 0)
        CorrectedWave = np.delete(CorrectedWave, np.asarray(CorrectedWave == 0).nonzero(), axis = 0)
        
        Corrected_output_data = np.column_stack((CorrectedWave, CorrectedFlux))

        return Corrected_output_data
    
    if output == 2:
        
        for i in modelwave:
            # print('i =', i)
            Match = (np.absolute(i - datawave) < 1).nonzero()
            # print('data wave =', datawave.size)

            # print('Match =', Match)
            # print('data flux =', dataflux.size)
            Match = np.array(Match)
            
            if Match.size == arr.size:
                
                CorrectedFlux = np.append(CorrectedFlux, np.PZERO)

            if Match.size == arr.size:
                
                CorrectedWave = np.append(CorrectedWave, np.PZERO)
                # print('Corrected Wave =', CorrectedWave)
                
            CorrectedFlux = np.append(CorrectedFlux, dataflux[Match[0]]) 
            CorrectedWave = np.append(CorrectedWave, datawave[Match[0]]) 
            
            
            
        CorrectedFlux = np.delete(CorrectedFlux, np.asarray(CorrectedFlux == 0).nonzero(), axis = 0)
        CorrectedWave = np.delete(CorrectedWave, np.asarray(CorrectedWave == 0).nonzero(), axis = 0)
        
        Corrected_output_data = np.column_stack((CorrectedWave, CorrectedFlux))

        return Corrected_output_data
    else:
        for i in datawave:
            Match = (np.absolute(i - modelwave) < 1).nonzero()
            Match = np.array(Match)
         
            if Match.size == arr.size:
                
                CorrectedFlux = np.append(CorrectedFlux, np.PZERO)
        
            if Match.size == arr.size:
                
                CorrectedWave = np.append(CorrectedWave, np.PZERO)
                
            CorrectedFlux = np.append(CorrectedFlux, modelflux[Match[0]]) 
            CorrectedWave = np.append(CorrectedWave, modelwave[Match[0]]) 
            
        CorrectedFlux = np.delete(CorrectedFlux, np.asarray(CorrectedFlux == 0).nonzero(), axis = 0)
        CorrectedWave = np.delete(CorrectedWave, np.asarray(CorrectedWave == 0).nonzero(), axis = 0)
        
        Corrected_output_model = np.column_stack((CorrectedWave, CorrectedFlux))

        return Corrected_output_model