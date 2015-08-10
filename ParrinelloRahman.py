#!/usr/bin/python 

import numpy as np
import Cell


def PRMD():
    # assign masses to each atom for MD
    cell.set_atom_mass()
    

    # covert the velocitis into fractional coordinates
    atomVeloCurrent = cell.get_atom_frac_velo()
    latVeloCurrent = cell.get_lat+velo()
    
    # compute f0
    sigma = np.zeros((3,3))
    sigma[0,:] = np.cross(lat[1,:], lat[2,:])
    sigma[1,:] = np.cross(lat[2,:], lat[0,:])
    sigma[2:,] = np.cross(lat[0,:], lat[1,:])
    f0 = sigma.transpose()*sigma
    
    # calculate the initial kinetic energy
    
    rkin = 0.
    for iat in range(nat):
        atomVeloCurrentTmp = latCurrent * atomVeloCurrent[iat][:]
        rkin += amass(iat)*(atomVeloCurrentTmp[0]**2+atomVeloCurrentTmp[1]**2+atomVeloCurrentTmp[2]**2)
    eKineticAtom = 0.5*rkin
    rkin = 0.
    for i in range(3):
        rkin += (latVeloCurrent[i][0]**2+latVeloCurrent[i][1]**2+latVeloCurrent[i][2]**2)
    eKineticLatt = 0.5*rkin
    
    print("PRESSURE, ENERGY", pressure, etot_in)
    # vol = det(lat)
    enthalpy = energy + pressure*vol
    
    if verb > 0:
        print(' ')
        
    #acceleration()
    
    # fix lat
    
    for itime in range(ntime):
        # torque_cell
        # perform the step
        # Beeman integration scheme
        
        dlatvec = dt*latVeloCurrent + dt*dt/6.*(4.*latAccCurrent-latAccPrev)
        for iat in range(nat):
            dx[iat,:] = dt*atomVeloCurrent[iat,:] + dt*dt/6.*(4.*atomAccCurrent[iat,:]-atomAccPrev[iat,:])
        
        # propagate()
    
def acc():
    volume = cell.get_volume()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    