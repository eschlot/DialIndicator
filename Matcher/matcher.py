import io
import csv
from fractions import Fraction
from decimal import Decimal

# BSD 3-Clause License
# 
# Copyright (c) 2023, eckar
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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