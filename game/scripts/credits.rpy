label credits:
    play music "audio/music/forest-lullaby.mp3"
    scene black with fade
    call screen credits
    stop music fadeout 3.0
    $ renpy.pause(3.0)
    return


transform credits_scroll(speed):
    ypos 600
    linear speed ypos -26000

screen credits():

    ## Ensure that the game_menu screens can't be stopped
    #key "K_ESCAPE" action NullAction()
    #key "K_MENU" action NullAction()
    #key "mouseup_3" action NullAction()

    style_prefix "credits"

    timer 12.0 action Return() ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(65.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Credits" xalign 0.5
            null height 75
            label "Aeolian Chimes Presents" xalign 0.5
            null height 75
            text "Light Upon Sandblooms"
            null height 150
            label "Art" xalign 0.5
            null height 10
            text "Haruki"
            null height 10
            text "Kasumi"
            null height 10
            text "Ally"
            null height 150
            label "Gallery Art" xalign 0.5
            null height 75
            text "Kasumi"
            null height 10
            text "EanSze"
            null height 150
            label "Programming" xalign 0.5
            null height 75
            text "BadMustard"
            null height 150
            label "Chief Editor" xalign 0.5
            null height 75
            text "Saniya"
            null height 150
            label "Discord MOD" xalign 0.5
            null height 75
            text "BTLD"
            null height 150
            label "Special Thanks" xalign 0.5
            null height 10
            label "To all" xalign 0.5
            null height 10
            label "my patron's" xalign 0.5
            null height 10
            text "My friends"
            null height 10
            text "My enemies"
            null height 10
            text "Everybody else"
            null height 10  
            label "Thanks for Playing!" xalign 0.5
            

style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    text_align 0.5

style credits_label_text:
    xalign 0.5
    justify True
    size 125
    text_align 0.5
    color "#ff0000"

style credits_text:
    xalign 0.5
    size 60
    justify True
    text_align 0.5
    color "#ffffff"