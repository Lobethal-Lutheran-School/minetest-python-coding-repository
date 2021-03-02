"""
 Copyright Dr Erich S. Heinzle 2021
 Licence: GNU GENERAL PUBLIC LICENCE, Version 2, June 1991

 Example python code to draw a mandelbrot set cloud in minetest

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
import miney

def draw_mandelbrot(mt, mcx, mcy, mcz, dx, dy, mcblock):

    positions = []
    iterations = 150;
    for x in range(0, dx):
        for y in range(0, dy):
            actual_x = -2.0+x/(dx/4)
            actual_y = -2.0+y/(dy/4)
            z_old_x = 0
            z_old_y = 0
            z_new_x = 0
            z_new_y = 0
            for iter in range(0, iterations):
                z_new_x = (z_old_x*z_old_x - z_old_y*z_old_y + actual_x)
                z_new_y = (2.0*z_old_y*z_old_x + actual_y)
                z_old_x = z_new_x
                z_old_y = z_new_y
            magnitude_sq = (z_old_x*z_old_x + z_old_y*z_old_y)
            if (magnitude_sq < 4.0) :
                positions.append(
                    {
                                "x": (mcx - dx/2 + x),
                                "y": (mcy),
                                "z": (mcz - dy/2 + y)
                    }
                )
    print("Spawning", len(positions), "nodes of", mcblock)
    print(positions)
    mt.node.set(nodes=positions, name=mcblock)

if miney.is_miney_available():
    mt = miney.Minetest()
    playerPos = mt.player[0].position
    x_blocks_per_unit = 300
    y_blocks_per_unit = 300
    mandel_cloud_height = 20
    draw_mandelbrot(mt, playerPos["x"], playerPos["y"]+ mandel_cloud_height, playerPos["z"], x_blocks_per_unit, y_blocks_per_unit, 'default:mese')
    mt.chat.send_to_all(mt.node.type.default.mese + " mandelbrot cloud done")
    print(mt.node.type.default.mese + " mandelbrot cloud done")
    print("Player position: %f %f %f" % (playerPos["x"], playerPos["y"], playerPos["z"]))

else:
    raise miney.MinetestRunError("Please start Minetest with the miney game")
