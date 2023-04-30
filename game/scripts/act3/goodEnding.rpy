label goodEnding:
    b "This is the good ending"
    "This is test text for the good ending"

    $ choiceCounter = 0;
    $ choice1 = False
    $ choice2 = False
    $ choice3 = False

    #Section to test multiple choices that split off
    if choiceCounter == 3:
        menu withChoice4:
            "This is Choice 1":
                jump choice1text
            "This is Choice 2":
                jump choice2text
            "This is Choice 3":
                jump choice3text
            "This is Choice 4":
                jump choice4text
    else:
        menu choiceSection:
            "This is Choice 1":
                if choice1 == False:
                    $ choice1 = True
                    $ choiceCounter += 1
                jump choice1text
            
            "This is Choice 2":
                if choice2 == False:
                    $ choice2 = True
                    $ choiceCounter += 1 
                jump choice2text

            "This is Choice 3":
                if choice3 == False:
                    $ choice3 = True
                    $ choiceCounter += 1
                jump choice3text
            
            

label choice1text:
    a "choice1"
    if choiceCounter == 3:
        jump withChoice4
    else:
        jump choiceSection

label choice2text:
    b "choice2"
    if choiceCounter == 3:
        jump withChoice4
    else:
        jump choiceSection

label choice3text:
    c "choice3"
    if choiceCounter == 3:
        jump withChoice4
    else:
        jump choiceSection

label choice4text:  
    d "choice4 to end the section" 
    jump choiceJump
 
label choiceJump:
    "Choices section ends here"
    jump credits
    return