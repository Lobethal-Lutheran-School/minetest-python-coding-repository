"""
 Copyright Dr Erich S. Heinzle 2021
 Licence: GNU GENERAL PUBLIC LICENCE, Version 2, June 1991

 Example python code to draw a pyramid in minetest

 requires:

 minetest luajit lua-socket lua-cjson idle3

 pip3 install miney

 install mineysocket mod in minetest
 Needs "secure.trusted_mods = mineysocket" in minetest.conf
 on starting minetest game, ensure newly installed mods are
 activated under configure tab

 recommended:

 idle3 fonts-crosextra-caladea fonts-crosextra-carlito minetest-mod-moreblocks
 minetest-mod-moreores minetest-mod-pipeworks minetest-server minetestmapper

"""

import math
import time
import miney

def draw_hollow_cube(mt, mcx, mcy, mcz, dx, dy, dz, mcblock, scale):

    positions = []
    for x in range(0, dx*scale):
        for y in range(0, dy*scale):
            for z in range(0, dz*scale):
                if (y == 0 or y == (dy*scale - 1)):
                    positions.append(
                        {
                                "x": (mcx + x),
                                "y": (mcz + z),
                                "z": (mcy + y)
                        }
                    )
                elif (x == 0 or x == (dx*scale - 1)):
                    positions.append(
                        {
                                "x": (mcx + x),
                                "y": (mcz + z),
                                "z": (mcy + y)
                        }
                    )
                elif (z == 0 or z == (dz*scale - 1)):
                    positions.append(
                        {
                                "x": (mcx + x),
                                "y": (mcz + z),
                                "z": (mcy + y)
                        }
                    )
    print("Spawning", len(positions), "cube of", mcblock)
    print(positions)
    mt.node.set(nodes=positions, name=mcblock)

def draw_cube(mt, mcx, mcy, mcz, dx, dy, dz, mcblock, scale):

    positions = []
    for x in range(0, dx*scale):
        for y in range(0, dy*scale):
            for z in range(0, dz*scale):
                positions.append(
                    {
                                "x": (mcx + x),
                                "y": (mcz + z),
                                "z": (mcy + y)
                    }
                )
    print("Spawning", len(positions), "cube of", mcblock)
    print(positions)
    mt.node.set(nodes=positions, name=mcblock)

def draw_eyes(mt,mcx, mcy, mcz, scale):
    draw_cube(mt, mcx + 2*scale, mcy + 3*scale, mcz + 10*scale, 1, 1, 1, 'wool:black', scale)
    draw_cube(mt, mcx + 1*scale, mcy + 3*scale, mcz + 10*scale, 1, 1, 1, 'wool:white', scale)
    draw_cube(mt, mcx + 2*scale, mcy + 3*scale, mcz + 11*scale, 1, 1, 1, 'wool:white', scale)
    draw_cube(mt, mcx + 3*scale, mcy + 3*scale, mcz + 10*scale, 1, 1, 1, 'default:sandstone', scale)
    draw_cube(mt, mcx + 5*scale, mcy + 3*scale, mcz + 10*scale, 1, 1, 1, 'wool:black', scale)
    draw_cube(mt, mcx + 6*scale, mcy + 3*scale, mcz + 10*scale, 1, 1, 1, 'wool:white', scale)
    draw_cube(mt, mcx + 5*scale, mcy + 3*scale, mcz + 11*scale, 1, 1, 1, 'wool:white', scale)
    draw_cube(mt, mcx + 4*scale, mcy + 3*scale, mcz + 10*scale, 1, 1, 1, 'default:sandstone', scale)

def draw_tail(mt,mcx, mcy, mcz, scale):
    draw_cube(mt, mcx + 3*scale, mcy + 21*scale, mcz + 3*scale, 2, 2, 1, 'wool:white', scale)
    draw_cube(mt, mcx + 3*scale, mcy + 21*scale, mcz + 4*scale, 2, 2, 7, 'wool:grey', scale)

def draw_leg(mt,mcx, mcy, mcz, scale):
    draw_hollow_cube(mt, mcx, mcy, mcz, 2, 2, 6, 'wool:grey', scale)

def draw_foot(mt,mcx, mcy, mcz, scale):
    draw_hollow_cube(mt, mcx, mcy, mcz, 2, 2, 1, 'wool:white', scale)

def draw_legs(mt,mcx, mcy, mcz, scale):
    draw_foot(mt, mcx + 1*scale, mcy + 7*scale, mcz, scale)
    draw_leg(mt, mcx + 1*scale, mcy + 7*scale, mcz + 1*scale, scale)
    draw_foot(mt, mcx + 1*scale, mcy + 18*scale, mcz, scale)
    draw_leg(mt, mcx + 1*scale, mcy + 18*scale, mcz + 1*scale, scale)
    draw_foot(mt, mcx + 5*scale, mcy + 7*scale, mcz, scale)
    draw_leg(mt, mcx + 5*scale, mcy + 7*scale, mcz + 1*scale, scale)
    draw_foot(mt, mcx + 5*scale, mcy + 18*scale, mcz, scale)
    draw_leg(mt, mcx + 5*scale, mcy + 18*scale, mcz + 1*scale, scale)

def draw_hindquarters(mt,mcx, mcy, mcz, scale):
    draw_hollow_cube(mt, mcx + 1*scale, mcy + 12*scale, mcz + 7*scale, 6, 9, 6, 'wool:grey', scale)

def draw_ruff(mt,mcx, mcy, mcz, scale):
    draw_hollow_cube(mt, mcx, mcy + 7*scale, mcz + 7*scale, 8, 6, 7, 'wool:grey', scale)

def draw_collar(mt,mcx, mcy, mcz, scale):
    draw_cube(mt, mcx, mcy + 6*scale, mcz + 7*scale, 8, 1, 7, 'wool:blue', scale)

def draw_jowls(mt,mcx, mcy, mcz, scale):
    draw_cube(mt, mcx + 1*scale, mcy + 3*scale, mcz + 7*scale, 1, 1, 3, 'default:sandstone', scale)
    draw_cube(mt, mcx + 1*scale, mcy + 4*scale, mcz + 7*scale, 1, 1, 2, 'default:sandstone', scale)
    draw_cube(mt, mcx + 6*scale, mcy + 3*scale, mcz + 7*scale, 1, 1, 3, 'default:sandstone', scale)
    draw_cube(mt, mcx + 6*scale, mcy + 4*scale, mcz + 7*scale, 1, 1, 2, 'default:sandstone', scale)

def draw_ears(mt,mcx, mcy, mcz, scale):
    draw_cube(mt, mcx + 1*scale, mcy + 5*scale, mcz + 13*scale, 2, 1, 2, 'wool:grey', scale)
    draw_cube(mt, mcx + 5*scale, mcy + 5*scale, mcz + 13*scale, 2, 1, 2, 'wool:grey', scale)

def draw_head(mt,mcx, mcy, mcz, scale):
    draw_hollow_cube(mt, mcx + 1*scale, mcy + 3*scale, mcz + 7*scale, 6, 4, 6, 'wool:grey', scale)

def draw_muzzle(mt,mcx, mcy, mcz, scale):
    draw_cube(mt, mcx + 2*scale, mcy, mcz + 7*scale, 4, 3, 1, 'wool:dark_grey', scale)
    draw_cube(mt, mcx + 3*scale, mcy + 1, mcz + 7*scale, 2, 2, 1, 'wool:grey', scale)
    draw_cube(mt, mcx + 2*scale, mcy, mcz + 8*scale, 4, 3, 2, 'default:sandstone', scale)
    draw_cube(mt, mcx + 3*scale, mcy, mcz + 9*scale, 1, 1, 1, 'wool:black', scale)
    draw_cube(mt, mcx + 4*scale, mcy, mcz + 9*scale, 1, 1, 1, 'wool:black', scale)

def draw_plinth(mt,mcx, mcy, mcz, scale, plinth_block):
    plinth = []
    plinth_levels = 4
    plinth_width_x = 8
    plinth_length_y = 23
    for z in range(0, plinth_levels*scale):
        for y in range(-plinth_levels*scale + z, plinth_length_y*scale + plinth_levels*scale - z):
            for x in range(-plinth_levels*scale + z, plinth_width_x*scale + plinth_levels*scale - z):
                plinth.append(
                    {
                                "x": (mcx + x),
                                "y": (mcz - plinth_levels*scale + z),
                                "z": (mcy + y)
                    }
                )
        mt.node.set(nodes=plinth, name=plinth_block)
        plinth = []
    for z in range(1, plinth_levels*scale):
        for y in range(-plinth_levels*scale, plinth_length_y*scale + plinth_levels*scale):
            for x in range(-plinth_levels*scale, plinth_width_x*scale + plinth_levels*scale):
                if (y == -plinth_levels*scale or y == plinth_length_y*scale + plinth_levels*scale - 1):
                    plinth.append(
                        {
                                "x": (mcx + x),
                                "y": (mcz - plinth_levels*scale - z),
                                "z": (mcy + y)
                        }
                    )
                elif (x == -plinth_levels*scale or x == plinth_width_x*scale + plinth_levels*scale - 1):
                    plinth.append(
                        {
                                "x": (mcx + x),
                                "y": (mcz - plinth_levels*scale - z),
                                "z": (mcy + y)
                        }
                    )
        mt.node.set(nodes=plinth, name=plinth_block)
        plinth = []
    

def draw_wolf(mt,mcx, mcy, mcz, scale):
    draw_tail(mt, mcx, mcy, mcz, scale)
    draw_legs(mt, mcx, mcy, mcz, scale)
    draw_hindquarters(mt, mcx, mcy, mcz, scale)
    draw_ruff(mt, mcx, mcy, mcz, scale)
    draw_collar(mt, mcx, mcy, mcz, scale)
    draw_head(mt, mcx, mcy, mcz, scale)
    draw_jowls(mt, mcx, mcy, mcz, scale)
    draw_muzzle(mt, mcx, mcy, mcz, scale)
    draw_ears(mt, mcx, mcy, mcz, scale)
    draw_eyes(mt, mcx, mcy, mcz, scale)

if miney.is_miney_available():
    plinth_block = 'default:mese'
    mt = miney.Minetest()
    playerPos = mt.player[0].position
    wolf_scale = 3
    mcx = playerPos["x"]
    mcy = playerPos["z"]
    mcz = playerPos["y"]
    draw_wolf(mt, mcx, mcy, mcz, wolf_scale)
    mt.chat.send_to_all(mt.node.type.default.mese + " wolf done")
    print("wolf done")
    draw_plinth(mt, mcx, mcy, mcz, wolf_scale, plinth_block)
    print("plinth done")
    print("Player position: %f %f %f" % (playerPos["x"], playerPos["y"], playerPos["z"]))

else:
    raise miney.MinetestRunError("Please start Minetest with the miney game")
