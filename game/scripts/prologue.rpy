label prologue:
    play music mainTheme loop
    scene bp1

    show char1 at truecenter

    d "This is the prologue"

    d "Checking to see if we can jump between scenes easily"

    show char1 at left with move

    show NPC1 at right

    d "set for extra delay here"

    e "hohoho you're approaching me?"

    menu:
        "Good Ending Choice":
            $ intimacyFlag+=1
            b "This is the good ending choice."
        "Bad Ending Choice":
            b "This is the bad ending choice."


    if intimacyFlag == 0:
        jump badEnding
    else:
        jump goodEnding

    #renpy.movie_cutscene(filename)
    stop music fadeout 3.0
    $ renpy.pause(3.0)
    jump credits

    return