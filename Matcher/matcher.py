import io
import csv
from fractions import Fraction
from decimal import Decimal

# MIT License
# 
# Copyright (c) 2023 eckar
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Dictionary for thread pitch of metric screws (M1 to M36)
metric_thread_pitch = {
    "M1": Fraction(1, 4), "M1.2": Fraction(1, 4), "M1.4": Fraction(3, 10), "M1.6": Fraction(7, 20),
    "M1.8": Fraction(7, 20), "M2": Fraction(2, 5), "M2.2": Fraction(9, 20), "M2.5": Fraction(9, 20),
    "M3": Fraction(1, 2), "M3.5": Fraction(3, 5), "M4": Fraction(7, 10), "M5": Fraction(4, 5),
    "M6": Fraction(1, 1), "M7": Fraction(1, 1), "M8": Fraction(5, 4), "M10": Fraction(3, 2),
    "M12": Fraction(7, 4), "M14": Fraction(2, 1), "M16": Fraction(2, 1), "M18": Fraction(5, 2),
    "M20": Fraction(5, 2), "M22": Fraction(5, 2), "M24": Fraction(3, 1), "M27": Fraction(3, 1),
    "M30": Fraction(7, 2), "M33": Fraction(7, 2), "M36": Fraction(4, 1)
}

def main():
    """Main function"""
    with open("output.csv", mode="w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # Write the header row
        csv_writer.writerow(["Screw","Pitch (Fractional)","Pitch (Decimal)", "Indexes", "Cyclic"])
        
        for screw, pitch in metric_thread_pitch.items():
            indexes = []
            cyclic = "No"
            i = Fraction(0, 1)
            while (i * pitch) <= Fraction(4, 1):
                if ((i * pitch) / Fraction(1, 10)).is_integer():
                    if (i * pitch) == Fraction(4, 1):
                        cyclic = "Yes"
                    else:
                        indexes.append(str((i * pitch) / Fraction(1, 10)))
                i += Fraction(1, 1)
            
            # Write the row to the CSV file
            csv_writer.writerow([f"{screw}",f"{pitch} mm ",f"{pitch.numerator/pitch.denominator} mm", " ".join(indexes), cyclic])

if __name__ == "__main__":
    main()