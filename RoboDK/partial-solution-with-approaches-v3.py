"""
Using Python for pick and place
Fernando Pacheco
2024-11
v3: With more tiles,
    pick and approach positions created programmaticaly
Process:
    Locate Pick 1
    Copy Pick 1
    Loop for i in range(2,num_tiles+1):
        Paste Pick 1 in the reference frame
        Change the name to Pick_i
        Move Pick_i in the y-axis
    Loop for i in range(1,num_tiles+1):
        Paste Pick 1 in the reference frame
        Change the name to Approach_i
        Move Approach_i in the y-axis and z-axis

Partial solution with approaches
"""

from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox

num_tiles=3 # number of mosaic tiles to pick

# Connect to RoboDK
RDK = robolink.Robolink()

# Get the robot
# RDK.Item searches for items in the station
robot = RDK.Item('Dobot MG400', robolink.ITEM_TYPE_ROBOT)

# Get the reference frame
frame = RDK.Item('RefSuctionCup')

# Get the target Pick 1, copy it
pick = RDK.Item('Pick 1')
pick.Copy() # equivalent to using CTRL+C

for i in range(2, num_tiles+1):
    temp = frame.Paste() # equivalent to CTRL+V
    temp.setName('Pick '+str(i))
    temp.setPose(temp.Pose()*robomath.transl(ty=-30*(i-1)))

# similar to Approach_i
for i in range(1, num_tiles+1):
    temp = frame.Paste() # equivalent to CTRL+V
    temp.setName('Approach '+str(i))
    temp.setPose(temp.Pose()*robomath.transl(ty=-30*(i-1), tz=80))

place = RDK.Item('Place in box')

# TODO: Movements
