# Duplicate objects
#
# Fernando Pacheco
# 2024-01

OBJWIDTH = 15
CLEARANCE = 10 # separation between objects

from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
RDK = robolink.Robolink()

# Locate the reference box
item = RDK.Item('Wood Stick', robolink.ITEM_TYPE_OBJECT)
if item.Valid():
    print('Item selected: ' + item.Name())
    print('Item position: ' + repr(item.Pose()))
else:
    raise Exception('Item not valid')

item.Copy() # like doing ctrl+C

# To paste, we need a reference frame
frame = RDK.Item('World', robolink.ITEM_TYPE_FRAME)
RDK.Render(False)
# paste in the frame the object
# that was previously copied
num_new = 2
step = 1.0/(num_new-1)
for i in range(num_new):
    newitem = frame.Paste()
    newitem.setName('stick'+str(i+1))
    newitem.setPose(item.Pose() * robomath.transl(0,-(OBJWIDTH+CLEARANCE)*(i+1)))
    newitem.setVisible(True, False) # item is visible, its reference frame no
    newitem.Recolor([0.3, step*i, 1 - step*i, 1])
item.setVisible(False, False) # make the reference object not visible
RDK.Render(True)

# Create source targets
item = RDK.Item('PickA_ref', robolink.ITEM_TYPE_TARGET)
item.Copy()
# for the Dobot post-processor, the reference frame should be only one
# it's not possible to change to another reference frame
# because the function to do it is not implemented
frame = RDK.Item('RefSuctionCup', robolink.ITEM_TYPE_FRAME)
RDK.Render(False)
# paste in the frame the object
# that was previously copied
for i in range(num_new):
    newitem = frame.Paste()
    newitem.setName('PickA'+str(i+1))
    newitem.setPose(item.Pose() * robomath.transl(0,-(OBJWIDTH+CLEARANCE)*(i+1)))
    newitem.setVisible(True, False) # item is visible, its reference frame no
RDK.Render(True)

# Create destination targets
item = RDK.Item('PickB_ref', robolink.ITEM_TYPE_TARGET)
item.Copy()
frame = RDK.Item('RefSuctionCup', robolink.ITEM_TYPE_FRAME)
RDK.Render(False)
# paste in the frame the object
# that was previously copied
for i in range(num_new):
    newitem = frame.Paste()
    newitem.setName('PickB'+str(i+1))
    newitem.setPose(item.Pose() * robomath.transl(0,-(OBJWIDTH+CLEARANCE)*(i+1)))
    newitem.setVisible(True, False) # item is visible, its reference frame no
RDK.Render(True)

