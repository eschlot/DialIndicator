include <BOSL2/std.scad>
include <BOSL2/fnliterals.scad>
include <BOSL2/gears.scad>



translate([0,0,0])
worm(circ_pitch=4, d=27.3, l=50,pressure_angle=20,  $fn=72);


translate([12.3+53.1/2,0,0])
rot([0,360/40/4,0])
rot([90,0,0])
worm_gear(circ_pitch=4, teeth=40, worm_diam=53.1);
