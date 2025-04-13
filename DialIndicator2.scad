include <BOSL2/std.scad>
include <BOSL2/fnliterals.scad>
include <BOSL2/gears.scad>

stext = ["0","2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36","38"];

//stext = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39" ];

translate([26.3,0,0])
rot([0,360/20/4,0])
rot([90,0,0])
union()
{
  worm_gear(circ_pitch=4, teeth=40, worm_diam=53.1, crowning=1,slices=10, worm_arc=24,$fn=360);
    

  translate([0,0,30])   { cyl(l=60, d=10, $fn=360);} // axle
  // 69-16/2-19 --> 69 Base position of the center of the body with text - half of the size of that - the height of the cylinder itself
  translate([0,0,69-16/2-19])   { cylinder(h=19, r1=5,  r2=24, $fn=360 );}

  translate([0,0,69]) { 
    union(){

      difference() { // d = 30 --> d = 48 oder auch r= 15 --> r= 24
	cyl(l=16, d=48, $fn=360);
	union() {
	  for(i=[0:1:19]) {
	    rotate([180,0,-360/20*i-1.8]) {
	      translate( [(48/2)*.95,0,6*(i % 2)-3])
		rotate([90,0,90])
		linear_extrude(height=1.5)
		text(stext[i],size=4.5,valign="center",halign="center");
	    }
	  }
	  for(i=[0:1:39]) {
	    rotate([180,0,360/40*i]) {
	      translate( [24*0.95,0,6])
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
