# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Terry Davis")

transform bg_fit:
    xysize (config.screen_width, config.screen_height)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cat at bg_fit

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show holyc

    # These display lines of dialogue.

    play music "audio/elephant.mp3"

    t "I like elephants and God likes elephants!"

    t "Here's a uhh"

    scene elephant at bg_fit

    show terry davis

    t "a realistic elephant."

    t "It's done with interpolation with.."

    hide terry davis
    show vector

    t "vectors.."

    hide vector
    show terry davis

    t "Sometimes it works, it's kinda... limited."

    t "Anyway uhh, so if you dont wanna go for realism.."

    t "you can go for BETTER than realism!"

    t "Wdym better than realism?"

    scene elephantwithblueeyes at bg_fit

    t "How about an elephant with 0x0000ff eyes!"

    stop music fadeout 2.0

    # This ends the game.

    return
