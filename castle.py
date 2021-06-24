"""
 Copyright Dr Erich S. Heinzle 2021
 Licence: GNU GENERAL PUBLIC LICENCE, Version 2, June 1991

 Example python code to draw a castle in minetest

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

# our basic function used to create volumes of wall, and pillars
def draw_wall(mt, mcx, mcy, mcz, width, length, height, mcblock):
    positions = []
    for x in range(0, width):
        for y in range(0, length):
            for z in range(0, height):
                positions.append(
                    {
                        "x": (mcx + x),
                        "y": (mcz + z),
                        "z": (mcy + y)
                    }
                )
    mt.node.set(nodes=positions, name=mcblock)
    print(positions)

def draw_tower_walls(mt, mcx, mcy, mcz, width, height, mcblock):
    draw_wall(mt, mcx+4, mcy, mcz, width-7, 1, height, mcblock)
    draw_wall(mt, mcx+4, mcy+width, mcz, width-7, 1, height, mcblock)
    draw_wall(mt, mcx, mcy+4, mcz, 1, width-7, height, mcblock)
    draw_wall(mt, mcx+width, mcy+4, mcz, 1, width-7, height, mcblock)

def draw_tower_pillars(mt, mcx, mcy, mcz, width, height, mcblock):
    draw_wall(mt, mcx+3, mcy+1, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+2, mcy+2, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+1, mcy+3, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+width-3, mcy+1, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+width-2, mcy+2, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+width-1, mcy+3, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+width-3, mcy+width-1, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+width-2, mcy+width-2, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+width-1, mcy+width-3, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+3, mcy+width-1, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+2, mcy+width-2, mcz, 1, 1, height, mcblock)
    draw_wall(mt, mcx+1, mcy+width-3, mcz, 1, 1, height, mcblock)

def draw_tower_floor(mt, mcx, mcy, mcz, width, height, mcblock):
    draw_wall(mt, mcx+4, mcy+1, mcz+height-1, width-7, 1, 1, mcblock)
    draw_wall(mt, mcx+3, mcy+2, mcz+height-1, width-5, 1, 1, mcblock)
    draw_wall(mt, mcx+2, mcy+3, mcz+height-1, width-3, 1, 1, mcblock)
    draw_wall(mt, mcx+4, mcy+width-1, mcz+height-1, width-7, 1, 1, mcblock)
    draw_wall(mt, mcx+3, mcy+width-2, mcz+height-1, width-5, 1, 1, mcblock)
    draw_wall(mt, mcx+2, mcy+width-3, mcz+height-1, width-3, 1, 1, mcblock)
    draw_wall(mt, mcx+1, mcy+4, mcz+height-1, width-1, width-7, 1, mcblock)

# we draw walls, then a roof
def draw_level(mt, mcx, mcy, mcz, width, height, mcblock):
    draw_tower_floor(mt, mcx, mcy, mcz, width, height, mcblock)
    draw_tower_pillars(mt, mcx, mcy, mcz, width, height, mcblock)
    draw_tower_walls(mt, mcx, mcy, mcz, width, height, mcblock)

# we need a floor as well as a roof
def draw_bottom_level(mt, mcx, mcy, mcz, width, height, mcblock):
    draw_tower_floor(mt, mcx, mcy, mcz, width, height+1, mcblock)
    draw_tower_floor(mt, mcx, mcy, mcz, width, 1, mcblock)
    draw_tower_pillars(mt, mcx, mcy, mcz, width, height+1, mcblock)
    draw_tower_walls(mt, mcx, mcy, mcz, width, height+1, mcblock)

def draw_tower(mt, mcx, mcy, mcz, width, height, level_repeats, tapered_count, mcblock):
    draw_bottom_level(mt, mcx, mcy, mcz, width, height, wall_block)
    level_count = 0;
    for sections in range(0, tapered_count):
        for repeats in range(0, level_repeats):
            if (sections == 0) & (repeats == 0):
                draw_bottom_level(mt, mcx, mcy, mcz, width, height, wall_block)
            else:
                draw_level(mt, mcx+sections, mcy+sections, mcz+level_count*height+1, width-(2*sections), height, wall_block)
            level_count += 1

def draw_perimeter_wall(mt, mcx, mcy, mcz, wall_width, wall_height, tower_width, tower_levels, level_height, mcblock):
    offset = wall_width/2
    wall_length = wall_width-tower_width
    tower_offset = tower_width/2
    draw_tower(mt, mcx-offset, mcy-offset, mcz, tower_width-1, level_height, tower_levels, 1, mcblock)
    draw_tower(mt, mcx+offset, mcy-offset, mcz, tower_width-1, level_height, tower_levels, 1, mcblock)
    draw_tower(mt, mcx-offset, mcy+offset, mcz, tower_width-1, level_height, tower_levels, 1, mcblock)
    draw_tower(mt, mcx+offset, mcy+offset, mcz, tower_width-1, level_height, tower_levels, 1, mcblock)
    draw_wall(mt, mcx-offset+tower_width, mcy-offset+tower_offset, mcz, wall_length, 1, wall_height, mcblock)
    draw_wall(mt, mcx-offset+tower_width, mcy+offset+tower_offset, mcz, wall_length, 1, wall_height, mcblock)
    draw_wall(mt, mcx-offset+tower_offset, mcy-offset+tower_width, mcz, 1, wall_length, wall_height, mcblock)
    draw_wall(mt, mcx+offset+tower_offset, mcy-offset+tower_width, mcz, 1, wall_length, wall_height, mcblock)

def draw_keep(mt, mcx, mcy, mcz, keep_width, level_height, keep_levels, mcblock):
    keep_tapered_sections = 1
    draw_tower(mt, mcx, mcy, mcz, keep_width-1, level_height, keep_levels, keep_tapered_sections, wall_block)

def draw_castle(mt, mcx, mcy, mcz, keep_width, level_height, keep_levels, wall_width, wall_height, tower_width, tower_levels, mcblock):
    keep_offset = keep_width/2-tower_width/2 
    draw_keep(mt, mcx, mcy, mcz, keep_width, level_height, keep_levels, mcblock)
    draw_perimeter_wall(mt, mcx+keep_offset, mcy+keep_offset, mcz, wall_width, wall_height, tower_width, tower_levels, level_height, mcblock)

if miney.is_miney_available():
    mt = miney.Minetest()
    playerPos = mt.player[0].position
    perimeter_wall_width = 44
    perimeter_wall_height = 8
    guard_tower_width = 9
    guard_tower_levels = 2
    keep_width = 14 # equal to width and length of bottom section of tower
    level_height = 5 # number of blocks per level, one of which is a floor
    keep_tapered_sections = 1   # number of tower sections, shrinking in width by 2 blocks per section going up
    keep_levels_per_section = 3 # number of levels per section
    wall_block = 'default:mese'
    #wall_block = 'greek:marble_polished'
    draw_castle(mt, int(playerPos["x"]), int(playerPos["z"]), int(playerPos["y"]), keep_width, level_height, keep_levels_per_section, perimeter_wall_width, perimeter_wall_height, guard_tower_width, guard_tower_levels, wall_block)
    mt.chat.send_to_all("castle done")
    print("castle done")
    print("Player position: %f %f %f" % (playerPos["x"], playerPos["y"], playerPos["z"]))

else:
    raise miney.MinetestRunError("Please start Minetest with the miney game")
