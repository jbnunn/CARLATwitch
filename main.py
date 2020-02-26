import sys
import carla
import random
import time

blueprint_library = world.get_blueprint_library()

class Simulation:

    def __init__(self, world):
        self.world = world

    def spawn_vehicle(self, vehicle_type=None, spawn_point=None):
        if vehicle_type is not None:
            vehicle_blueprint = blueprint_library.filter(vehicle_type)
        else:
            vehicle_blueprint = random.choice(blueprint_library.filter('vehicle'))

        if spawn_point is not None:
            pass
            # Implement dynamic spawn_point later
        else:
            spawn_point = random.choice(self.world.get_map().get_spawn_points())

        self.world.spawn_actor(vehicle_blueprint, spawn_point)

def main():
    actor_list = []

    # Connect to client
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)

    # Retrieve the world
    world = client.get_world()

    # Get a vehicle blueprint
    vehicle_blueprint = get_vehicle_blueprint('model3')
    
    # Grab a random spawn point to drop the vehicle into
    spawn_point = random.choice(world.get_map().get_spawn_points())
    
    # Spawn the vehicle into the world
    vehicle = world.spawn_actor(vehicle_blueprint, spawn_point)

    # 


    print(blueprint_library)

if __name__ == "__main__":
    main()