class CalculateHeatTime:

    def __init__(self, rider, track):

        self.rider = rider
        self.track = track

    def get_after_start_time(self, after_start_time, rider, track):
        #liczy dojazd do pierwszego luku, dla uproszczenia 30 metrow po starcie
        return after_start_time

    def get_first_lap_time(self, first_lap_time, rider, track):

        return first_lap_time

    def get_second_lap_time(self, second_lap_time, rider, track):
        return second_lap_time

    def get_third_lap_time(self, third_lap_time, rider, track):
        return third_lap_time

    def get_fourth_lap_time(self, fourth_lap_time, rider, track):
        return fourth_lap_time

    def get_heat_time(self, first_lap_time, second_lap_time, third_lap_time, fourth_lap_time):
        heat_time = first_lap_time + second_lap_time + third_lap_time + fourth_lap_time+
        return heat_time
