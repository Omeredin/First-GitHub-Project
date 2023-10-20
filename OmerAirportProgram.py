import random
class Plane():
    def __init__(self, id, airline):
        self.airline = airline
        self.id = id

class Airport():
    def __init__(self):
        self.takeoff_queue = []
        self.landing_queue = []
        self.runways = [None, None]
        self.completed_landings = 0
        self.completed_takeoffs = 0
        self.landings_wait_time = 0
        self.takeoffs_wait_time = 0

    def add_plane_to_takeoff_queue(self, plane):
        self.takeoff_queue.append(plane)

    def add_plane_to_landings_queue(self, plane):
        self.landing_queue.append(plane)

    def clear_to_land(self, time):
        if self.landing_queue:
            plane = self.landing_queue.pop(0)
            self.completed_landings += 1
            self.landings_wait_time += time - plane.id
            print(f"The time is {time} Plane {plane.id} from {plane.airline} is cleared to land.")

    def clear_to_takeoff(self, time):
        if self.takeoff_queue:
            plane = self.takeoff_queue.pop(0)
            self.completed_takeoffs += 1
            self.takeoffs_wait_time += time - plane.id
            print(f"The time is {time}. Plane {plane.id} from {plane.airline} is cleared for takeoff")

    def print_queue(self, time):
        print(f"The time is {time}. There are {len(self.takeoff_queue)} waiting to takeoff")
        print(f"There are {len(self.landing_queue)} waiting to land")

    def simulation(self):
        for time in range(120):
            takeoff_departures = random.randint(0, 3)
            landing_arrivals = random.randint(0, 3)

            for i in range(takeoff_departures):
                plane_id = time * 2
                plane = Plane(plane_id, "American Airlines")
                self.add_plane_to_takeoff_queue(plane)

            for i in range(landing_arrivals):
                plane_id = time * 2 +1
                plane  = Plane(plane_id, "United Airlines")
                self.add_plane_to_landings_queue(plane)

            for i, runway in enumerate(self.runways):
                if runway == None:
                    if i == 0:
                        self.clear_to_land(time)
                    else:
                        self.clear_to_takeoff(time)

            self.print_queue(time)

        print(f"number of landings complete {self.completed_landings}")
        print(f"Number of takeoffs complete {self. completed_takeoffs}")

if __name__ == "__main__":
    airport = Airport()
    airport.simulation()









