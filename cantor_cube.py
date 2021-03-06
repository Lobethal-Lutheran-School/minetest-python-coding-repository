"""
 Copyright Dr Erich S. Heinzle 2021
 Licence: GNU GENERAL PUBLIC LICENCE, Version 2, June 1991

 Example python code to draw a cantor cube in minetest

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

def draw_cantor_cube(mt, mcx, mcy, mcz, dx, mcblock):

    positions = []
    finish = dx + 1
    for z in range(1, finish):
        for x in range(1, finish):
            for y in range(1, finish):
                block = 1
                max_exp = int(math.log(dx,3))
                for w in range(0, max_exp):
                    if (x%(3**(max_exp-w)) > 3**(max_exp-w-1) and x%(3**(max_exp-w)) < (2*3**(max_exp-w-1)+1)):
                        block = 0
                    if (y%(3**(max_exp-w)) > 3**(max_exp-w-1) and y%(3**(max_exp-w)) < (2*3**(max_exp-w-1)+1)):
                        block = 0
                    if (z%(3**(max_exp-w)) > 3**(max_exp-w-1) and z%(3**(max_exp-w)) < (2*3**(max_exp-w-1)+1)):
                        block = 0
                if (block == 1):
                    positions.append(
                        {
                                "x": (mcx + x),
                                "y": (mcy + z),
                                "z": (mcz + y)
                        }
                    )
    print("Spawning", len(positions), "nodes of", mcblock)
    print(positions)
    mt.node.set(nodes=positions, name=mcblock)

if miney.is_miney_available():
    mt = miney.Minetest()
    playerPos = mt.player[0].position
    power_of_three = 3
    cantor_edge_length = 3**power_of_three
    cantor_start_height = 5
    draw_cantor_cube(mt, playerPos["x"], playerPos["y"]+ cantor_start_height, playerPos["z"], cantor_edge_length, 'default:mese')
    mt.chat.send_to_all(mt.node.type.default.mese + " cantor cube done")
    print(mt.node.type.default.mese + " cantor cube done")
    print("Player position: %f %f %f" % (playerPos["x"], playerPos["y"], playerPos["z"]))

else:
    raise miney.MinetestRunError("Please start Minetest with the miney game")
