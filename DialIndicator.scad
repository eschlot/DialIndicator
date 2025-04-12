include <BOSL2/std.scad>
include <BOSL2/fnliterals.scad>
include <BOSL2/gears.scad>

stext = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19" ];

translate([26.3,0,0])
rot([0,360/20/4,0])
rot([90,0,0])
union()
{
  worm_gear(circ_pitch=4, teeth=40, worm_diam=53.1, crowning=1,slices=10, worm_arc=24,$fn=360);
    
  translate([0,0,30]) { cyl(l=60, d=10, $fn=360);}
  translate([0,0,47]) { tube(h=10, or1=5,or2=15,wall=5 );}
  
  translate([0,0,60]) {
    union(){

      difference() {
	cyl(l=16, d=30, $fn=360);
	union() {
	  for(i=[0:1:19]) {
	    rotate([180,0,-360/20*i-1.8]) {
	      translate( [15*.95,0,6*(i % 2)-3])
		rotate([90,0,90])
		linear_extrude(height=1)
		text(stext[i],size=4.5,valign="center",halign="center");
	    }
	  }
	  for(i=[0:1:19]) {
	    rotate([180,0,360/20*i]) {
	      translate( [15*0.95,0,6])
		rotate([90,0,90])
		cube([1,10,10]);
	    }
	  }
	}
      }
    }
  }
}


// translate([0,0,0])
// worm(circ_pitch=4, d=27.3, l=50,pressure_angle=20); // ,  $fn=72


// translate([12.3+53.1/2,0,0])
// rot([0,360/40/4,0])
// rot([90,0,0])
// worm_gear(circ_pitch=4, teeth=40, worm_diam=53.1);
