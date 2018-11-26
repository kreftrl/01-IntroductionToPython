"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Robert Kreft.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()
bob=rg.SimpleTurtle('turtle')
bobjr=rg.SimpleTurtle('turtle')
bobmcbob=rg.SimpleTurtle('turtle')
bobsr=rg.SimpleTurtle('turtle')
bob.pen=rg.Pen('red',2)
bobjr.pen=rg.Pen('blue',2)
bobmcbob.pen=rg.Pen('maroon',2)
bobsr.pen=rg.Pen('purple',2)
window.tracer(5)
for k in range (100):
    bobjr.right(180)
    bobmcbob.right(90)
    bobsr.right(270)
    bob.forward(k)
    bobjr.forward(k)
    bob.right(k)
    bobjr.right(k-180)
    bobmcbob.forward(k)
    bobmcbob.right(k-90)
    bobsr.forward(k)
    bobsr.right(k-270)
window.close_on_mouse_click()
