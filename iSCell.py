import numpy as np
import math

class Cell:
    
    def __init__( self, 
            name = None,
            symbols = None,
            typat = None,
            lattice = None,
            positions = None,
            lat_velo = None,
            atom_cart_velo = None,
            atom_cart_velo = None,
            stress = None):

        if name == None:
            self.name = None
        else:
            self.name = str( name )

        if typat == None:
            self.typat = None
        else:
            self.typat = np.array( typat )

        if lattice == None:
            self.lattice = None
        else:
            self.lattice = np.array( lattice )

        if positions == None:
            self.positions = None
        else:
            self.positions = np.array( positions )

    def set_name( self, name ):
        self.name = str( name )

    def get_name( self ):
        return self.name

    def set_lattice( self, lat ):
        self.lattice = np.array( lat )

    def get_lattice( self ):
        return self.lattice

    def set_positions( self, pos ):
        self.positions = np.array( pos )

    def get_frac_positions( self ):
        return self.positions

    def get_cart_positions( self ):
        return np.dot(self.positions, self.lattice)

    def set_typat( self, typ):
        self.typat = np.array( typ )

    def get_typat( self ):
        return self.typat

    def set_symbols( self, symb ):
        self.symbols = symb

    def get_symbols( self ):
        return self.symbols

    def set_lat_velo( self, v ):
        self.lat_velo = np.array(v)

    def get_lat_velo( self ):
        return self.lat_velo

    def set_atom_cart_velo( self, v):
        self.atom_cart_velo = np.array(v)

    def get_atom_cart_velo( self ):
        return self.atom_cart_velo
        
    def set_atom_frac_velo( self, v):
        self.atom_frac_velo = np.array(v)

    def get_atom_frac_velo( self ):
        return self.atom_frac_velo        

    def get_volume( self ):
        return np.linalg.det( self.lattice )

    def set_stress( self, stres):
        self.stress = np.array(stres)

    def get_stress( self ):
        return self.stress

def lat2vec( lat ):
    return np.array([ lat[0][0], lat[1][1], lat[2][2], 
                      lat[1][0], lat[2][0], lat[2][1] ], float)

def vec2lat( vec ):
    return np.array([ [vec[0], 0., 0.],
                      [vec[3], vec[1], 0.],
                      [vec[4], vec[5], vec[2]] ], float)

def lat2lcons(lat):
    ra = math.sqrt(lat[0][0]**2 + lat[0][1]**2 + lat[0][2]**2)
    rb = math.sqrt(lat[1][0]**2 + lat[1][1]**2 + lat[1][2]**2)
    rc = math.sqrt(lat[2][0]**2 + lat[2][1]**2 + lat[2][2]**2)

    cosa = (lat[1][0]*lat[2][0] + lat[1][1]*lat[2][1] + lat[1][2]*lat[2][2])/rb/rc
    cosb = (lat[0][0]*lat[2][0] + lat[0][1]*lat[2][1] + lat[0][2]*lat[2][2])/rb/rc
    cosc = (lat[0][0]*lat[1][0] + lat[0][1]*lat[1][1] + lat[0][2]*lat[1][2])/rb/rc

    alpha = math.acos(cosa)
    beta = math.acos(cosb)
    gamma = math.acos(cosc)

    return np.array([ra, rb, rc, alpha, beta, gamma], float)