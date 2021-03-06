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
import miney

def draw_pyramid(mt, mcx, mcy, mcz, dx, mcblock):

    positions = []
    iterations = dx;
    for z in range(0, int(dx/2)):
        for x in range(0, int(dx-2*z)):
            for y in range(0, int(dx-2*z)):
                positions.append(
                    {
                                "x": (mcx - (dx/2-z) + x),
                                "y": (mcy + z),
                                "z": (mcz - (dx/2-z) + y)
                    }
                )
    print("Spawning", len(positions), "nodes of", mcblock)
    print(positions)
    mt.node.set(nodes=positions, name=mcblock)

if miney.is_miney_available():
    mt = miney.Minetest()
    playerPos = mt.player[0].position
    pyramid_edge_length = 29
    pyramid_base_height = 10
    draw_pyramid(mt, playerPos["x"], playerPos["y"]+ pyramid_base_height, playerPos["z"], pyramid_edge_length, 'default:mese')
    mt.chat.send_to_all(mt.node.type.default.mese + " pyramid done")
    print(mt.node.type.default.mese + " pyramid done")
    print("Player position: %f %f %f" % (playerPos["x"], playerPos["y"], playerPos["z"]))

else:
    raise miney.MinetestRunError("Please start Minetest with the miney game")
