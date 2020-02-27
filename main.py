import sys
import carla
import random
import time

class Simulation:

    def __init__(self, world, num_vehicles):
        self.world = world
        self.blueprint_library = world.get_blueprint_library()
        self.actors = []
        self.num_vehicles = num_vehicles

class Vehicle:

    def __init__(self, simulation, filter='vehicle', spawn_point=None):
        self.filter = filter
        self.spawn_point = None

    def spawn(self):
        vehicle_blueprint = random.choice(simulation.blueprint_library.filter(filter))

        if spawn_point is not None:
            pass
            # Implement dynamic spawn_point later
        else:
            spawn_point = random.choice(simulation.world.get_map().get_spawn_points())
        
        try:
            vehicle = self.world.spawn_actor(vehicle_blueprint, spawn_point)
        except:
            # Use try_spawn_actor. If the spot is already occupied by another object, 
            # the function will return None.
            vehicle = self.world.try_spawn_actor(vehicle_blueprint, spawn_point)

        if vehicle:
            simulation.actors.append(vehicle)
            print(f'Spawned vehicle: {vehicle.type_id)')

        return vehicle
    
    def attach_camera(self, camera_type='rgb'):
        camera = None

        if camera_type == 'rgb':
            camera_bp = blueprint_library.find('sensor.camera.rgb')
            camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
            camera = world.spawn_actor(camera_bp, camera_transform, attach_to=self)

            simulation.actors.append(camera)

        print(f'Attached {camera_type} camera')

        return camera  

def main():
    actor_list = []

    # Connect to client
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)

    # Retrieve the world
    world = client.get_world()

    # Setup the Simulation
    simulation = Simulation(world)

    # Spawn a Tesla
    tesla = Vehicle(simulation, filter='vehicle.tesla.model3')
    tesla.spawn()
    tesla.set_autopilot()

    # Attach an RGB camera
    camera = tesla.attach_camera('rbg')

    # Register a callback to save images to disk (TBD: analyze in real time)
    cc = carla.ColorConverter.LogarithmicDepth
    camera.listen(lambda image: image.save_to_disk('_out/%06d.png' % image.frame_number, cc))

    #  Spawn NPC vehicles
    for i in range(simulation.num_vehicles):
        v = Vehicle(simulation)
        if v is not not None:
            v.set_autopilot()
        
    






if __name__ == "__main__":
    main()