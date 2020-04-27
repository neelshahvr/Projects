#Caroline Parsons
#parsonsc
#Diego Hagans
#2019-4-18
#Final Project

"""
Space Invaders Final Project Code.
"""
import arcade
import random
import os

#Set the screen size and title of the screen
screen_width = 700
screen_height = 600
screen_title = "Space Invaders"
column_spacing = 60
row_spacing = 50
left_margin = 70
bottom_margin = 250
explosion_duration = 13

#Class directly adapted from example code in Arcade Academy:
#http://arcade.academy/examples/sprite_explosion.html#sprite-explosion
#Small adaptations and edits were made to fit the design elements of the project
class Explosion(arcade.Sprite):
    """ 
    Creates an explosion animation when an enemy is killed by the user.
    """

    def __init__(self, texture_list):
        super().__init__("explosions.png")

        # Start at the first frame
        self.current = 0
        self.textures = texture_list

    def update(self):

        # Update to the next frame of the animation.
        self.current = self.current + 1
        if self.current < len(self.textures):
            self.set_texture(self.current)
        else:
            self.kill()

#Class directly adapted from example code in Arcade Academy:
#http://arcade.academy/examples/gui_text_button.html#gui-text-button
#Small adaptations and edits were made to fit the design elements of the project
#Docstrings were added to follow the dtyle guide
class TextButton:
    """
    Text-based button class for GUI.
    """
    #Initialization of variables
    def __init__(self, center_x, center_y, width, height, text, font_size=18,
                 font_face="Arial", face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        """
        Initializes class variables.
        """
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """
        Draw the button.
        """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)
        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color
        #Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2,
                        self.center_y - self.height / 2,
                        self.center_x + self.width / 2,
                        self.center_y - self.height / 2,
                         color, self.button_height)
        #Right vertical
        arcade.draw_line(self.center_x + self.width / 2,
                        self.center_y - self.height / 2,
                        self.center_x + self.width / 2,
                        self.center_y + self.height / 2,
                         color, self.button_height)
        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color
        #Top horizontal
        arcade.draw_line(self.center_x - self.width / 2,
                        self.center_y + self.height / 2,
                        self.center_x + self.width / 2,
                        self.center_y + self.height / 2,
                         color, self.button_height)
        #Left vertical
        arcade.draw_line(self.center_x - self.width / 2,
                        self.center_y - self.height / 2,
                        self.center_x - self.width / 2,
                        self.center_y + self.height / 2,
                         color, self.button_height)
        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height
        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        """
        Check to see if button is pressed.
        """
        self.pressed = True

    def on_release(self):
        """
        Check to see if button is released.
        """
        self.pressed = False

def check_mouse_press_for_buttons(x, y, button_list):
    """
    Given an x, y, see if we need to register any button clicks.

    Args:
        x(float): X position of mouse.
        y(float): Y position of mouse.
        button_list(list): List of buttons.
    """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(x, y, button_list):
    """
    If a mouse button has been released, see if we need to process
    any release events.
    """
    for button in button_list:
        if button.pressed:
            button.on_release()

class StartTextButton(TextButton):
    """
    Text-based button for GUI, resumes game from parent button class.
    """
    #Initialization of variables
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "RESUME", 14, "Arial")
        """
        Initializes class variables.
        """
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class StopTextButton(TextButton):
    """
    Text-based button for GUI, pauses game from parent button class.
    """
    #Initialization of variables
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "PAUSE", 14, "Arial")
        """
        Initializes class variables.
        """
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()
#END OF CODE DIRECTLY USED FROM ARCADE ACADEMY FOR A GUI INTERFACE
###############################################################################



###############################################################################
#Start of code by Caroline Parsons
###############################################################################
class Sprite(arcade.Sprite):
    """
    Sprite class for Space Invaders"
    """
    def __init__(self):
        self.player_list = None
        self.enemy_list = None
        self.enemy_list2 = None
        self.bullet_list = None
        self.player = None
        self.death_list = None

class Game(arcade.Window):
    """
    Main game class for Space Invaders.
    """
    #Initialization of variables
    def __init__(self, width, height, title):
        """
        Initializes class variables.

        Args:
            width(int): Width of screen.
            height(int): Height of screen.
            title(string): Title of game.
        """
        super().__init__(width, height, title)
        #If neccessary in the future make the mouse not visible on the screen
        #self.set_mouse_visible(False)
        self.pause = False
        self.background = None
        self.frame_count = 0
        self.score = 0
        self.explosion_list = []

        for x in range(explosion_duration):
            texture = "explosions.png"
            self.explosion_list.append(arcade.load_texture(texture))
  

    #Setup function
    def setup(self):
        """
        Setup the game to render.
        """
        #Set up the background of the screen
        self.background = arcade.load_texture("backgroundGScreen.png")
        #Technique from:
        #http://arcade.academy/arcade.html#module-arcade.sprite_list
        Sprite.player_list = arcade.SpriteList()
        Sprite.enemy_list = arcade.SpriteList()
        self.enemy_list2 = arcade.SpriteList()
        Sprite.bullet_list = arcade.SpriteList()
        Sprite.enemy_bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        #Set the score to 0
        self.score = 0
        self.counts = 0
        #Add user ship
        Sprite.player = arcade.Sprite("ship.png", 0.05)
        Sprite.player_list.append(Sprite.player)
         # Create our on-screen GUI buttons
        self.button_list = []

        play_button = StartTextButton(60, 570, self.resume_program)
        self.button_list.append(play_button)

        quit_button = StopTextButton(60, 515, self.pause_program)
        self.button_list.append(quit_button)
        #Add enemy aliens with a for loop
        #Technique from:
        #http://arcade.academy/examples/nested_loops_box.html#nested-loops-box
        #For loop over the x
        for row in range(3):
            #For loop over the y
            for column in range(10):
                #Calculate the location
                x = column * column_spacing + left_margin
                y = row * row_spacing + bottom_margin
                #make the alien sprite
                enemy = arcade.Sprite("alien.png", 0.20)
                enemy.center_x = x
                enemy.center_y = y
                Sprite.enemy_list.append(enemy)

        for row in range(1):
            #For loop over the y
            for column in range(10):
                #Calculate the location
                x = column * column_spacing + left_margin
                y = row * row_spacing + bottom_margin
                #make the alien sprite
                enemy = arcade.Sprite("ye.png", 0.125)
                enemy.center_x = x
                enemy.center_y = 400
                Sprite.enemy_list.append(enemy)

        #Play background song
        #arcade.play_sound(arcade.sound.load_sound("mo_bamba.wav"))
        #arcade.play_sound(arcade.sound.load_sound("hbfs.wav"))
        arcade.play_sound(arcade.sound.load_sound("digi.wav"))

    #on_draw is already estblished in the acrade package
    #In the arcade.Window class
    #Technique from:
    #http://arcade.academy/arcade.html#module-arcade.draw_commands
    def on_draw(self):
        """
        Render the screen before drawing.
        """
        #Gets ready to start the render
        #Must be called before drawing on the screen
        #Technique from:
        #http://arcade.academy/arcade.html#module-arcade.window_commands
        arcade.start_render()
        #Create the background for the game
        arcade.draw_texture_rectangle(screen_width // 2, screen_height // 2,
                            screen_width, screen_height, self.background)
        # Draw the buttons
        for button in self.button_list:
            button.draw()
        #Create the Sprites
        Sprite.enemy_list.draw()
        self.enemy_list2.draw()
        Sprite.bullet_list.draw()
        Sprite.player_list.draw()
        Sprite.enemy_bullet_list.draw()
        self.explosions_list.draw()

        #Set the score on the screen
        score_txt = f"SCORE: {self.score}"
        #Set the number of shots on the screen
        number_shots = f"SHOTS: {self.counts}"
        arcade.draw_text(score_txt, 300, 550, arcade.color.WHITE, 20)
        arcade.draw_text(number_shots, 550, 550, arcade.color.WHITE, 20)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.

        Args:
            x(float): X position of mouse.
            y(float): Y position of mouse.
            delta_x(float): Change in x.
            delta_y(float): Change in y.
        """
        Sprite.player.center_x = x
        Sprite.player.center_y = 20

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Shoots bullet on press of the mouse.

        Args:
            x(foat): X position of the mouse
            y(float): Y position of the mouse
            button(int): Mouse hit
            modifiers(int): Shift/click, ctrl/click, etc.
        """
        check_mouse_press_for_buttons(x, y, self.button_list)
        #Make the shots fired noise when pressed
        arcade.sound.play_sound(arcade.sound.load_sound("shoot.wav"))
        ship_bullet = arcade.Sprite("green_bullet.png", 0.03)
        ship_bullet.change_y = 8
        #Make the center of the bullet equal to the center of the ship
        ship_bullet.center_x = Sprite.player.center_x
        ship_bullet.bottom = Sprite.player.top
        Sprite.bullet_list.append(ship_bullet)
        #keep count of each bullet
        self.counts += 1

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def pause_program(self):
        """
        Pauses game.
        """
        self.pause = True

    def resume_program(self):
        """
        Resumes game.
        """
        self.pause = False

    def update(self, delta_time):
        """
        Update/play the game once it is setup and rendered.

        Args:
            #http://arcade.academy/arcade.html
            delta_time(float): Moves everything, collision checks
        """
        if self.pause:
            return
        #Loop through the enemies
        for enemy in Sprite.enemy_list:
            #http://arcade.academy/arcade.html#module-arcade.sprite_list
            # Have a random 1 in 2000 change of shooting each frame
            if random.randrange(2000) == 0:
                #Set the bullet sprite to a picture and designate the size
                enemy_bullet = arcade.Sprite("bullet.png", 0.07)
                #Shoot the bullet from the center of the enemy
                enemy_bullet.center_x = enemy.center_x
                enemy_bullet.top = enemy.bottom
                enemy_bullet.change_y = -8
                Sprite.enemy_bullet_list.append(enemy_bullet)
        #Remove bullet when it goes off the screen
        for bullet in Sprite.enemy_bullet_list:
            if bullet.top <0:
                bullet.kill()
        #Update the bullet lists
        Sprite.enemy_bullet_list.update()
        self.explosions_list.update()
        Sprite.bullet_list.update()
        #Loop through each bullet
        for bullet in Sprite.bullet_list:
            #Check each bullet for a collision with an enemy
            hits_list = arcade.check_for_collision_with_list(bullet,
                        Sprite.enemy_list)
            #If there is a hit
            if len(hits_list) > 0:
            	#Have the explosion png appear in the location of the enemy
                explosion = Explosion(self.explosion_list)
                explosion.center_x = hits_list[0].center_x
                explosion.center_y = hits_list[0].center_y
                self.explosions_list.append(explosion)
                #Get the bullet of the screen
                bullet.kill()
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > screen_height:
                #Get the bullet of the screen
                bullet.kill()
            #For every enemy in the hit list
            for enemy in hits_list:
                #Kill the enemy
                enemy.kill()
                #Increase the score
                self.score += 10
                #Hit Sound
                arcade.sound.play_sound(arcade.sound.load_sound("inKilled.wav"))

        for bullet in Sprite.bullet_list:
            #Check each bullet for a collision with an enemy
            hits_list = arcade.check_for_collision_with_list(bullet,
                        self.enemy_list2)

            #If there is a hit
            if len(hits_list) > 0:
                #Get the bullet of the screen
                bullet.kill()
            #For every enemy we hit

            for enemy2 in hits_list:
                #Kill the enemy
                enemy2.kill()
                #Increase the score
                self.score += 10

                #Hit Sound
                arcade.sound.play_sound(arcade.sound.load_sound("inKilled.wav"))
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > screen_height:
                #Get the bullet of the screen
                bullet.kill()

#Main fuction
def main():
    """
    Main method to run game.
    """
    window = Game(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
