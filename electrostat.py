import math

class electro():
    ''' Please Provide only charge in coulomb and r in meters only. '''
    def __init__(self):
        ''' The Electric Force Constant '''
        self.k = 9 * pow(10,9)
        ''' Absolute electric permitivity of space or vaccum '''
        self._e = 8.85 * pow(10,-12) 

    def ColoumbForce(self, q1, q2, r):
        Force = 9 *pow(10,9) * q1 * q2 / pow(r, r)
        return Force

    def ElectricFieldIntensity(self, q, r):
        '''
            This function will take charge and distance as arguments.
            And output will be the Electric field intensity.
            And will be str in nature.
            The output will be in dimensions of C/m.
        '''
        intensity = 9 * pow(10,9) * q / r
        return intensity

    def voltage0(self, workdone, charge):
        ''' If workdone and charge is given.... Supply workdone or Potential Energy and charge as arguments..
         Findign Voltage by supplying workdone and charge as Argument. 
         Potential Energy can also be supplyied in place of workdone. 
         As the Potential Energy is equals to Workdone. '''
        voltage = workdone/charge
        return voltage
    
    def voltage1(self, charge, distance):
        ''' Voltage Due to point charge. By supplying charge and distance as Arguments. '''
        ''' Finding Voltage by supllying charge and distance as Arguments.  '''
        ''' The Real Formula is V = Q/4*pi*e0*r '''
        voltage = charge * 9 * pow(10,9)/distance * pow(10,-2) 
        return voltage

    def volatage2(self, capacity, charge):
        ''' This function takes two arguments that are capacity and charge.
            And return output as voltage.
            By The formula of Capactity.
        '''
        voltage = charge/capacity
        return voltage
    
    def potentialGradient(self, volatage, distance):
        ''' Finding Potential Gradient by supplying volate and distance as arguments. '''
        potentilgrid = volatage/distance
        return potentilgrid

    def potentialEnergy(self, q1, q2, distance):
        ''' Finding potential Energy by supplying first two arguments as charges and thrid as distance.. '''
        energy  = self.k * q1 * q2 / distance
        return energy
    
    def potentialEnergy1(self, voltage, charge):
        ''' Finding potenial energy by supplying Voltage and charge as Arguments. '''
        ''' The Unit will be S.I.'''
        energy = voltage * charge
        return energy
    

    def electricFlux1(self, intensity, surfaceArea, theta):
        ''' Finding Electric Flux by supplying Electric field intenstiy, SurfaceArea and theata. 
         Theata is the small Angle between the surface area and the field intensity. '''
        electricflux = intensity * surfaceArea * math.cos(theta)
        return electricflux
    
    def electricFlux2(self, charge):
        ''' Finding electric flux by Supplying charge as Argument. 
         Here the Gauss\'s Theorm is used. 
         Electic Flux  is equals 1/e0 times the charge 
         The Output will be in the S.I units. '''
        electricflux = charge/self._e
        return electricflux

    def capacity(self, charge, voltage):
        ''' As we know that the amount of charge supplied is directly,
            Proportional to the increase in Volatge. 
            Q = C.V
            Where Q = Charge supllied.
                  C = Constant of proportionality and is know as the Capactiy of that conductor.
                  V = Increase in the Volatage/Potential Difference.
            Return Element will be a constant term.
            '''
        capacti = charge/voltage
        return capacti
    






