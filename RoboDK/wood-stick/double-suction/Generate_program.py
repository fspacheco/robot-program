# Create program to run in the robot
#
# Fernando Pacheco
# 2024-01

num_new=2 # number of new objects that were created

from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
RDK = robolink.Robolink()

frame = RDK.Item('RefSuctionCup', robolink.ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception('RefFrame RefSuctionCup is not valid')

# How to create attach and detach events
# From https://robodk.com/forum/Thread-Attach-an-object-in-python
INS_TYPE_EVENT = 7
EVENT_ATTACH = 0
EVENT_DETACH = 1
tool = RDK.Item('Suction Cup', robolink.ITEM_TYPE_TOOL)
if not tool.Valid():
    raise Exception('Tool Suction Cup is not valid')
frameWorld = RDK.Item('World', robolink.ITEM_TYPE_FRAME)
if not frameWorld.Valid():
    raise Exception('RefFrame World is not valid')
ins_event_attach = {'Type': INS_TYPE_EVENT, 'Behavior': EVENT_ATTACH, 'ToolPtr': str(tool.item)}
ins_event_detach = {'Type': INS_TYPE_EVENT, 'Behavior': EVENT_DETACH, 'ToolPtr': str(tool.item), 'FramePtr': str(frameWorld.item)}
    
# The program to move from targets A to targets B
prog = RDK.AddProgram('AutoMove')

prog.setPoseFrame(frame)
tool = RDK.Item('Suction Cup')
prog.setPoseTool(tool)

itemlist = RDK.ItemList(filter=robolink.ITEM_TYPE_TARGET)
for i in range(num_new):
    for item in itemlist:
        if item.Name()=='PickA'+str(i+1):
            print(f'Move PickA{i+1}')
            prog.MoveJ(item.Pose()*robomath.transl(0,0,-20))
            prog.MoveL(item)
            prog.setParam("Add",ins_event_attach) # ATTACH simulation only
            prog.setDO('1', 1) # turn ON vacuum
            prog.Pause(1000) # then wait
            prog.MoveL(item.Pose()*robomath.transl(0,0,-20)) # go up first
    for item in itemlist:
        if item.Name()=='PickB'+str(i+1):
            prog.MoveJ(item.Pose()*robomath.transl(0,0,-20))
            prog.MoveL(item)
            prog.setParam("Add",ins_event_detach) # DETACH simulation only
            prog.setDO('1', 0) # turn OFF vacuum
            prog.Pause(1000) # then wait
            prog.MoveL(item.Pose()*robomath.transl(0,0,-20))

