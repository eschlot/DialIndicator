include <BOSL2/std.scad>
include <BOSL2/gears.scad>

stext = ["0","2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36","38"];

translate([39,0,0])
rot([0,360/40/4,0])
rot([90,0,0])
union()
{
  worm_gear(circ_pitch=4, teeth=40, worm_diam=53.1, crowning=1,slices=10, worm_arc=24,$fn=360); // The gear, centered. 

  translate([0,0,30])   { cyl(l=60, d=10, $fn=360);} // The main axle
  translate([0,0,69-16/2-19])   { cylinder(h=19, r1=5,  r2=24, $fn=360 );} //The transition from the main axle to the cylinder with the marks and the text

  translate([0,0,69]) { 
    union(){

      difference() { 
	cyl(l=16, d=48, $fn=360); // The cylinder
	union() {
	  for(i=[0:1:19]) {  // The text on the cylinder
	    rotate([180,0,-360/20*i-1.8]) {
	      translate( [(48/2)*.95,0,6*(i % 2)-3])
		rotate([90,0,90])
		linear_extrude(height=1.5)
		text(stext[i],size=4.5,valign="center",halign="center");
	    }
	  }
	  for(i=[0:1:39]) { // The tick marks on the cylinder
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

// For all who want to also see the work gear engaged.
//worm(circ_pitch=4, d=27.4, l=50,pressure_angle=20); // ,  $fn=72
