from js import document

def sub(event):
        #defines the terms n stuff for python, setting up the ifs and elifs by making their values from the ids in the html file
    regy = document.getElementById("yes")
    regn = document.getElementById("no")
    medy = document.getElementById("yes2")
    medn = document.getElementById("no2")
    g7 = document.getElementById("g7")
    g8 = document.getElementById("g8")
    g9 = document.getElementById("g9")
    g10 = document.getElementById("g10")
    ruby = document.getElementById("ruby")
    eme = document.getElementById("eme")
    saph = document.getElementById("saph")
    top = document.getElementById("top")
    jade = document.getElementById("jade")
    output = document.getElementById("out")

    if regn and medn: #checks if the user has done the registration and has filed a medical certificate.
        pass
    else:
        return
    
    if g7 and ruby: #the said chain of ifs and elifs to actually give the user their assigned teams
        print('You are a tiger!')
    elif g8 and eme:
        print('You are a tiger!')
    elif g9 and saph:
        print('You are a tiger!')
    elif g10 and saph:
        print('You are a tiger!')
    elif g7 and eme:
        print('You are a hornet!')
    elif g8 and ruby:
        print('You are a hornet!')
    elif g9 and eme:
        print('You are a hornet!')
    elif g9 and jade:
        print('You are a hornet!')
    elif g10 and ruby:
        print('You are a hornet!')
    elif g7 and saph:
        print('You are a bear!')
    elif g8 and top:
        print('You are a bear!')
    elif g9 and ruby:
        print('You are a bear!')
    elif g10 and top:
        print('You are a bear!')
    elif g7 and top:
        print('You are a dog!')
    elif g8 and jade:
        print('You are a dog!')
    elif g8 and saph:
        print('You are a dog!')
    elif g9 and top:
        print('You are a dog!')
    elif g10 and eme:
        print('You are a dog!')
