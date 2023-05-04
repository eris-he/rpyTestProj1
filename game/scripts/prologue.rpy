label prologue:
    play music mainTheme loop
    scene bg1_desert:
        zoom 1.5

    show char1 at truecenter
    $ renpy.pause(3.0)
    hide char1

    d "This is the prologue"

    d "Checking to see if we can jump between scenes easily"

    show ah_neutral at left with moveinleft:
        zoom 0.75

    a "Checking transition between faces"

    show ah_pleased at left:
        zoom 0.75
    
    hide ah_neutral
    d "set for extra delay here"

    e "hohoho you're approaching me?"

    hide ah_pleased
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