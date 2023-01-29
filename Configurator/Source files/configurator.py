import cadquery as cq
from cadquery import exporters


""" Wrist mount """
def wrist_mount_generator(wrist_size):
	wrist 	= wrist_size
	wall 	= 5.0
	length	= 25.0

	# Create half-circle
	wrist_mount = cq.Workplane("XY").radiusArc(((wrist+2*wall), 0.0), (wrist+2*wall)/2).close().extrude(length)
	# Make a wrist sized hole to create an arc
	wrist_mount = wrist_mount.faces(">Z").workplane(origin=((wrist+2*wall)/2,0,0)).hole(wrist)
	# Create two extrusions with holes used for straps
	wrist_mount = wrist_mount.faces("<Y").workplane(origin=(0, 0, 0)).lineTo(0, length).lineTo(wall, length).lineTo(wall, 0.0).close().extrude(10.0)
	wrist_mount = wrist_mount.faces("<Y").workplane(origin=(wrist+wall, 0, 0)).lineTo(0, length).lineTo(wall, length).lineTo(wall, 0.0).close().extrude(-10.0)
	wrist_mount = wrist_mount.faces("left").workplane(origin=(0,-7.5,2.5)).lineTo(-4.0,0).lineTo(-4.0, (length-(2.5*2))).lineTo(0.0, (length-(2.5*2))).close().cutThruAll()
	# Create mount for lower-arm beam
	wrist_mount = wrist_mount.faces("<Z").workplane(origin=(wrist/2+wall, wrist/2, length/2)).lineTo(-12.75-wall, 0.0).lineTo(-12.75-wall, -15.0).lineTo(-12.75, -15.0).lineTo(-12.75, -wall).lineTo(12.75, -wall).lineTo(12.75, -15.0).lineTo(12.75+wall, -15,0).lineTo(12.75+wall, 0.0).close().extrude(-length)
	wrist_mount = wrist_mount.faces("left").workplane(origin=(wrist/2-12.75,wrist/2+wall+10,0)).center(5.0, length/2-7.0).hole(4.3)
	wrist_mount = wrist_mount.faces("left").workplane(origin=(wrist/2-12.75,wrist/2+wall+10,0)).center(5.0, length/2+7.0).hole(4.3)

	exporters.export(wrist_mount, 'wrist_mount.stl')


""" Biceps mount """
def biceps_mount_generator(biceps_size):
	biceps 	= biceps_size
	wall 	= 5.0
	length = 56

	biceps_mount = cq.Workplane("XY").radiusArc(((biceps+2*wall), 0.0), (biceps+2*wall)/2).close().extrude(length)
	# Make a biceps sized hole to create an arc
	biceps_mount = biceps_mount.faces(">Z").workplane(origin=((biceps+2*wall)/2,0,0)).hole(biceps)
	# Create two extrusions with holes used for straps
	biceps_mount = biceps_mount.faces("<Y").workplane(origin=(0, 0, 0)).lineTo(0, length).lineTo(wall, length).lineTo(wall, 0.0).close().extrude(10.0)
	biceps_mount = biceps_mount.faces("<Y").workplane(origin=(biceps+wall, 0, 0)).lineTo(0, length).lineTo(wall, length).lineTo(wall, 0.0).close().extrude(-10.0)
	biceps_mount = biceps_mount.faces("left").workplane(origin=(0,-7.5,2.5)).lineTo(-4.0,0).lineTo(-4.0, (length-(2.5*2))).lineTo(0.0, (length-(2.5*2))).close().cutThruAll()
	# Create mount for side beam
	biceps_mount = biceps_mount.faces("left").workplane(origin=(0, 0, 0)).lineTo(-28.0, 0.0).lineTo(-28.0, length).lineTo(0.0, length).close().extrude('next')
	biceps_mount = biceps_mount.faces("left").workplane(origin=(0, -3.5, 0)).lineTo(-3.0, 0.0).lineTo(-3.0, length).lineTo(0.0, length).close().extrude(10)
	biceps_mount = biceps_mount.faces("left").workplane(origin=(0, 25, 0)).lineTo(-3.0, 0.0).lineTo(-3.0, length).lineTo(0.0, length).close().extrude(-10)
	biceps_mount = biceps_mount.faces("<Y").workplane(origin=(0, 0, 0)).center(-5.0, length/2-18.0).hole(4.5)
	biceps_mount = biceps_mount.faces("<Y").workplane(origin=(0, 0, 0)).center(-5.0, length/2+18.0).hole(4.5)

	exporters.export(biceps_mount, 'biceps_mount.stl')

""" Biceps side_beam """
def biceps_side_beam_generator(biceps_length):
	length = biceps_length
	width = 25
	thick = 10
	# Set points for side holes and nut cutouts
	holes = [(-length/2+8, 0), (-length/2+44, 0), (length/2-44, 0), (length/2-8, 0)]
	rect_points = [(-length/2+8, 6.5), (-length/2+44, 6.5), (length/2-44, 6.5), (length/2-8, 6.5), (-length/2+8, -6.5), (-length/2+44, -6.5), (length/2-44, -6.5), (length/2-8, -6.5)]

	# Main beam with mounting holse for biceps mount
	side_beam = cq.Workplane("XY").box(length, width, thick)
	side_beam = side_beam.faces("<Y").workplane().pushPoints(holes).hole(4.3)
	side_beam = side_beam.faces("<Z").workplane(origin=(0,0,0)).pushPoints(rect_points).rect(7,3).cutThruAll()
	
	# Mounting plate with holes for Nema 14
	nema_14 = [(13,13), (13,-13), (-13,-13), (-13,13)]
	side_beam = side_beam.faces("<Z").workplane(origin=(length/2, width/2, 0)).lineTo(0,35).lineTo(17.5,35).lineTo(17.5,0).close().extrude(-thick)
	(point_x, point_y) = (length/2 + 17.5, width/2)
	side_beam = side_beam.faces(">Z").workplane(origin=(point_x-45, point_y, 0)).lineTo(0,-35).lineTo(80,-35).lineTo(80,0).close().extrude(12.5)
	(point_x, point_y) = (length/2 + 35, width/2 - 17.5)
	side_beam = side_beam.faces(">Z").workplane(origin=(point_x,point_y,0)).cboreHole(6.0,22.5,2)
	side_beam = side_beam.faces("<Z").workplane(origin=(point_x,point_y,0),offset=-thick).pushPoints(nema_14).pushPoints(nema_14).cboreHole(3.3,6,2.5)

	# Holes for electronics enclosure
	holes = [(-15,0),(15,0)]
	side_beam = side_beam.faces("<Z").workplane(origin=(0,0,0)).pushPoints(holes).hole(4.5)
	side_beam = side_beam.faces("<Z").workplane(origin=(0,0,0)).pushPoints(holes).polygon(6, 7.3).cutBlind(-3.0)

	# Slot containing the encoder gears
	(point_x, point_y) = (length/2 + 52.5, (12.5+thick)/2)
	side_beam = side_beam.faces("<Y").workplane(origin=(point_x-33,0,point_y)).rect(60,5.2).cutThruAll()

	# Encoder and encoder gear mount
	(point_x, point_y) = (length/2+7,width/2-17.5)
	side_beam = side_beam.faces("<Z").workplane(origin=(point_x,point_y,0)).cboreHole(3.5,6.5,3) # Hole for bolt and first bearing
	side_beam = side_beam.faces(">Z").workplane(origin=(point_x,point_y,0)).rect(24,24).cutBlind(-2)
	holes = [(8,8), (-8,8), (-8,-8), (8,-8)]
	side_beam = side_beam.faces(">Z").workplane(origin=(point_x,point_y,0)).rect(16,9).pushPoints(holes).circle(3/2).cutBlind(-6) # Holer for placing the encoder IC close to the magnet
	side_beam = side_beam.faces(">Z").workplane(origin=(point_x,point_y,0),offset=-8.85).cboreHole(3.5,6.5,3) # Second bearing hole


	exporters.export(side_beam, 'biceps_side_beam.stl')

""" Lower-arm beam """
def lower_arm_beam_generator(lower_arm_length):
	length = lower_arm_length
	width = 25
	thick = 10

	# Set points for side holes and nut cutouts
	holes = [(-length/2+5.5, 0),(-length/2+19.5,0)]
	rect_points = [(-length/2+5.5, 6.0), (-length/2+5.5, -6.0), (-length/2+19.5, 6.0), (-length/2+19.5, -6.0)]

	lower_arm_beam = cq.Workplane("XY").box(length, width, thick)
	lower_arm_beam = lower_arm_beam.faces("<Y").workplane().pushPoints(holes).hole(4.3)
	lower_arm_beam = lower_arm_beam.faces("<Z").workplane(origin=(0,0,0)).pushPoints(rect_points).rect(7,3).cutThruAll()
	# Create the rounding on the edge and the "sunk" circle
	lower_arm_beam = lower_arm_beam.faces(">Z").workplane(origin=(length/2-width/2, 0, 0)).circle(width/2).cutThruAll()
	lower_arm_beam = lower_arm_beam.faces(">Z").workplane(origin=(length/2, 0, 0)).rect(width, width).cutThruAll()
	lower_arm_beam = lower_arm_beam.faces("<Z").workplane(origin=(length/2-width/2, 0, 0)).circle(width/2).extrude(-0.4*thick)

	# Holes for mounting the motor shaft
	motor_holes = [(0, 8), (-6.93, -4), (6.93, -4)]
	lower_arm_beam = lower_arm_beam.faces("<Z").workplane(origin=(length/2-width/2, 0, 0)).hole(6.3)
	lower_arm_beam = lower_arm_beam.faces("<Z").workplane(origin=(length/2-width/2, 0, 0)).pushPoints(motor_holes).cboreHole(3.3, 6.3, 2.0)

	exporters.export(lower_arm_beam, 'lower_arm_beam.stl')


""" Test section. Only used under development """
def test():
    wrist_size 	= input("Enter wrist width in mm: ")
    biceps_size = input("Enter biceps width in mm: ")
    lower_arm_length = input("Enter length of the lower_arm in mm: ")
    biceps_length = input("Enter length of the upper arm in mm: ")
    wrist_mount_generator(float(wrist_size))
    biceps_mount_generator(float(biceps_size))
    biceps_side_beam_generator(float(biceps_length))
    lower_arm_beam_generator(float(lower_arm_length))

#test()
