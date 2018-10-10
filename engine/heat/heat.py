class Heat:
    def __init__(self, heat_number, gateArider, gateBrider, gateCrider, gateDrider, trackSurface, trackLength):
        #heat parameters
        self.heat_number = heat_number
        #lineup (from match program)
        self.gateArider = gateArider
        self.gateBrider = gateBrider
        self.gateCrider = gateCrider
        self.gateDrider = gateDrider
        #track
        self.trackSurface = trackSurface
        self.trackLength = trackLength
        '''Current weather conditions
        self.currentTemperature = currentTemperature
        self.currentWeathCond = currentWeathCond #rain, sunny, cloudy etc
        '''
