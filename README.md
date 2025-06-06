# DialIndicator
 Dial Indicator for a Crouzet Valence TC125 - 3D printable


The dial indicator can be used on a Crouzet Valence TC125 lathe. 
It is used to reengage the thread cut leaver of the saddle to the lead screw when cutting threads. This makes it easy to cut till a shoulder and still never run into a risk to damage a thread. 

It uses a 40 teeth gear that is used also on the main saddle of the lathe. When disengaging the tooth gear from the lead screw on the Crouzet Valence  lathe there are 40 different positions in which one can reengage. So without a dial indicator it is nearly impossible to do this right. 

## Usage

When the dial indicator is already 3D printed and mounted to the lathe and the DialIndicatorUsage.pdf is available, the usage is as follows: 

### Assuming the thread to cut is a thread that is marked as cyclic in the DialIndicatorUsage.pdf:

Engage the thread lever of the saddle at position 0 (zero). Cut the first path, possibly using the automatic disengagement feature of the Crouzet Valence lathe. This will cut immediatly already the recess at the end of a screw twords the head. Stop the motor and rewind the saddle to the beginning. Reengage, when the Dial Indicator shows zero or any of the indexes given in the table. 

**Example:**

For an M5 thread the positions 0, 8, 16, 24, 32 and on any next turn of the dial indicator will reengage correctly. 

### Assuming the thread is a thread that is not cyclic in the DialIndicatorUsage.pdf

Start in the same way: 
    
#### Safe way: 
    
Engage the thread lever of the saddle at position 0 (zero). Cut the first path, possibly using the automatic disengagement feature of the Crouzet Valence lathe. After disengangement stop the lathe and switch to turn the direction and reverse till the dial indicator shows zero again. Move the saddle backwards under motor and by this keep track of the position. 
    
#### More advanced: 

Take care to keep track of the number of turns of the Dial Indicator. 
You can also re-engage on any index of the table, but keep in mind that after a full turn of the dial indicator the relative positions change. 
    
**Example:**

M8 thread can start at index 0 and also use index 25 or 50 (aka. a full turn +10). Moving backwards also index 15 (aka. -25) or "a full turn and 30" (aka -50) can be used. Since this is error proune, using the same index 0 on the same relative position of the dial indicator may be simpler. 


## Printing:

The parts were printed in PLA with a fine surface. 

- The gear part is printed with the gear down. The overhangs are limited to 45° and by this can be printed without problems under normal circumstances.  
- The clamp is printed with the inverse cylinder to the top. 
- The base part has the half tube of the axle to the top. 

The parts are mounted to the saddle of the lathe with M4 screws. The original protection of the saddle is removed for the time of the usage. The clamp part is mounted after cutting threads in to the base part.

The Dial Indicator is removed after usage, because the gear can crash into the disengagement mechanism of the lathe. So it is worth to mount it for the usage. 

## Credits:

OpenScad (https://openscad.org/) and the BOSL2 (https://github.com/BelfrySCAD/BOSL2) package made this possible. The gear is calculated automatically and this is amazing. All the rest of the work is only simple handwork. 

The base part and the clamp were modelled in FreeCad 1.0. Very nice: https://www.freecad.org/




