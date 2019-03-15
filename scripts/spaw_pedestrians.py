"""
A script to spawn pedestrian actors into carla world
"""

import sys
import glob
import logging
import os
import random

#TODO: append to python path
try:
    os.chdir("/home/adel/carla")
    sys.path.append(glob.glob('**/carla-*%d.%d-%s.egg' % (3, 5, 'linux-x86_64'))[0])
except IndexError:
    logging.error("Failed to find path to egg file")
    exit(1)

import carla

def main():
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    ped_blueprints = world.get_blueprint_library().filter("walker.*")
    spawn_points = list(world.get_map().get_spawn_points())
    for i in range(1,len(spawn_points),1):
        world.try_spawn_actor(random.choice(ped_blueprints), spawn_points[i])
        logging.debug("spawned pedestrian at {}".format(str(spawn_points[i])))

if __name__ == '__main__':
    print('spawning pedestrians ...')
    main()