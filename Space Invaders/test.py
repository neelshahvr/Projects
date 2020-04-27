import unittest
import unittest.mock

from ex import setup
from ex import update
from ex import on_mouse_press
from ex import __init__


class Tests_Game(unittest.TestCase):

#add enemy to list
    def test_setup(self):
        self.assertEqual(setup(self.enemy_list), enemy_list==7, 'Seven enemies')

#number of shots being updated correctly
    def test_update(self):
        self.assertEqual(on_mouse_press(x, y, 1, 0), counts==1, 'One shot')


#score
    def test_score(self):
        self.assertEqual(update(self.hits_list==100), score==100, '100 score')


if __name__ == '__main__':
    unittest.main()

"""
def on_mouse_motion(self, x, y, delta_x, delta_y):
This function is called when the mouse in moved. Since this requires real-time
human input, it cannot be automatically tested. I tested two things from this
function: the location of the player’s ship and the aim of the bullets. The
first thing I checked was the location of the player’s ship. The player’s ship
was anchored at the bottom of the screen and could not be brought up the y-axis
 of the screen by moving the mouse. If the mouse is dragged off the game
 screen, the player’s ship does not move. As soon as the mouse enters the game
 screen, the player’s ship moved directly to where the mouse was located on the
  x-axis. The second thing I checked was the aim of the bullets. The player’s
  bullets were always aimed where the mouse was located on the game screen
  (and thus always right ahead of the player’s ship).

def on_mouse_press(self, x, y, button, modifiers):
This function is called when the mouse is pressed and then shoots bullets.
Since this requires real-time human input, it cannot be automatically tested.
I tested two things from this function: if a bullet was shot every time the
mouse was pressed and if the “shot counter” updated correctly. The first thing
I checked was if a bullet was shot every time the mouse was pressed. If the
mouse was dragged and then pressed off the game screen, it would not shoot nor
would the counter go up. Every time the mouse was pressed on the game screen
(no matter its location on said game screen), a bullet would be shot.
The second thing I checked was making sure that the “shot counter” counted
every time I pressed the mouse and didn’t stop counting if the starting number
or the counting interval were changed. I went through and temporarily changed
some of the code to make sure that the “shot counter” did start where it was
supposed to start and increased by the assigned interval. I did this for
multiple different cases (some examples being starting the counter at 10 and
increasing it by 5 or starting counter at 100 and decreasing it by 1). The
“shot counter” did not break for any of the adjustments.

def update(self, delta_time):
This function updates and plays the game once it’s set up and rendered.
However, this function is dependent on the
on_mouse_motion(self, x, y, delta_x, delta_y) and the
on_mouse_press(self, x, y, button, modifiers). The other tests I conducted
were dependent on this function working properly. If the other tests did not
work, I would have checked both functions to make sure where the problem was
occurring (not just one or the other).

def check_mouse_press_for_buttons(x, y, button_list):
AND
def check_mouse_release_for_buttons(x, y, button_list):
AND
def on_release(self, x, y, self.button_list):
These three functions worked hand-in-hand to make sure that the buttons in the 
game worked properly. The two buttons we had were the "start" and "pause"
buttons. I tested this by making sure that the intended functions of the
buttons only occurred when that button was pressed and not anywhere else on
the screen. The test was meant to do three things:
1. make sure the program knew the location of the buttons
2. the buttons performed their intended purpose
3. you could only use the buttons to perform the function assigned to the
specific function

(NOTE: functions such as pause_program(self) and resume_program(self) were
tested on the basis that the check_mouse_press_for_buttons(x, y, button_list),
check_mouse_release_for_buttons(x, y, button_list), and
on_release(self, x, y, self.button_list) working as that the only way to
test them was to visually see if the game paused or resumed anywhere that was
not a button.

(NOTE: functions such as on_draw(self) and __init__(self) can not be tested.
on_draw(self) makes the sprites that are in the folder appear on screen while
__init__(self) is just used to set up what variables will be recurring in the
class (most of these variables are either 0 or None).)
"""
