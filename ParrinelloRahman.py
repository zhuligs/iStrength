#!/usr/bin/python 

import numpy as np


def PRMD():
    # assign masses to each atom for MD
    # for iat in range(nat):
    # amass(iat) =   

    # covert the velocitis into fractional coordinates
    vPosCurrent = cell.get_frac_velo()

    # calculate the initial kinetic energy
    
    rkin = 0.
    for iat in range(nat):
        vPosCurrentTmp = latCurrent * vPosCurrent[iat][:]
        rkin += amass(iat)*(vPosCurrentTmp[0]**2+vPosCurrentTmp[1]**2+vPosCurrentTmp[2]**2)
    eKineticAtom = 0.5*rkin
    rkin = 0.
    for i in range(3):
        rkin += (vLatCurrent[i][0]**2+vLatCurrent[i][1]**2+vLatCurrent[i][2]**2)
    eKineticLatt = 0.5*rkin
    
    print("PRESSURE, ENERGY", pressure, etot_in)
    # vol = det(lat)
    enthalpy = energy + pressure*vol
    
    if verb > 0:
        print(' ')
        
    #acceleration()
    