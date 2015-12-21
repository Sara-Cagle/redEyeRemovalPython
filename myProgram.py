#Sara Cagle
#ID number 902939934, scagle6@gatech.edu
#CS 1301 Section B07
#Collaboration statement: I worked on this project by myself using only the materials provided to us in this semester's course materials.
#Please see the readme.txt for more information


#run the function by using fixRedEye("picturename") with "picturename" corresponding to a red-eye photo you'd like to heal.
#Be sure to specify where "picturename" is coming from. Place it in the same directory inwhich you save this program.
#follow the on-screen, recursive input directions.



from Myro import *

def fixRedEye(i0):
    pic = makePicture(i0)
    show(pic)
    pic1=copyPicture(pic)


    w = getWidth(pic)
    h = getHeight(pic)

    aList = [] #my example of a compound data type in use.

#--------------------------------------------------------------------------------
#Blocking out the top left corner

    for x in range(0,w//4):
        for y in range(0,h//2):
            pixel = getPixel(pic1, x,y)
            setRed(pixel,0)
            setGreen(pixel,0)
            setBlue(pixel,0)
    show(pic1)
    i1 = input(("Did I just cover up the red-eye? Yes or no"))

#--------------------------------------------------------------------------------
#Confirming red-eye or not block 1

    if i1 == "Yes" or i1 == "yes":
        for x in range(0,w//4):
            for y in range(0,h//2):
                pixel = getPixel(pic, x,y)
                r = getRed(pixel)
                g = getGreen(pixel)
                b = getBlue(pixel)
                if r>80 and b<50 and g<50:
                    setRed(pixel,45)
                    setGreen(pixel,45)
                    setBlue(pixel,45)

        aList.append("Block 1")
        show(pic)
        rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
        if rec == "Yes" or rec == "yes":
            print("According to you, the red-eye was found (this time around) in:", aList)
            print("Onto the next run-through!")
            fixRedEye(pic)
        elif rec == "No" or rec == "no":
            savePicture(pic,"red-eye fixed.jpg")
            print("According to you, the red-eye was found (this time around) in:", aList)
            print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
            return None


    if i1 == "No" or i1 == "no":
        pic2 = copyPicture(pic)
        for x in range(w//4,w//2):
            for y in range(0,h//2):
                pixel = getPixel(pic2, x,y)
                setRed(pixel,0)
                setGreen(pixel,0)
                setBlue(pixel,0)
        show(pic2)
        i2 = input(("Did I just cover up the red-eye? Yes or no"))

#--------------------------------------------------------------------------------
#Confirming red-eye or not block 2


        if i2 == "Yes" or i2 == "yes":
            for x in range(w//4,w//2):
                for y in range(0,h//2):
                    pixel = getPixel(pic, x,y)
                    r = getRed(pixel)
                    g = getGreen(pixel)
                    b = getBlue(pixel)
                    if r>80 and b<50 and g<50:
                        setRed(pixel,45)
                        setGreen(pixel,45)
                        setBlue(pixel,45)
            aList.append("Block 2")
            show(pic)
            rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
            if rec == "Yes" or rec == "yes":
                print("According to you, the red-eye was found (this time around) in:", aList)
                print("Onto the next run-through!")
                fixRedEye(pic)
            elif rec == "No" or rec == "no":
                savePicture(pic,"red-eye fixed.jpg")
                print("According to you, the red-eye was found (this time around) in:", aList)
                print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                return None



        if i2 == "No" or i2 == "no":
            pic3 = copyPicture(pic)
            for x in range(w//2,(w//4)*3):
                for y in range(0,h//2):
                    pixel = getPixel(pic3, x,y)
                    setRed(pixel,0)
                    setGreen(pixel,0)
                    setBlue(pixel,0)
            show(pic3)
            i3 = input(("Did I just cover up the red-eye? Yes or no"))


#--------------------------------------------------------------------------------
#Confirming red-eye or not for block 3


            if i3 == "Yes" or i3 == "yes":
                for x in range(w//2,(w//4)*3):
                    for y in range(0,h//2):
                        pixel = getPixel(pic, x,y)
                        r = getRed(pixel)
                        g = getGreen(pixel)
                        b = getBlue(pixel)
                        if r>80 and b<50 and g<50:
                            setRed(pixel,45)
                            setGreen(pixel,45)
                            setBlue(pixel,45)

                aList.append("Block 3")
                show(pic)
                rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
                if rec == "Yes" or rec == "yes":
                    print("According to you, the red-eye was found (this time around) in:", aList)
                    print("Onto the next run-through!")
                    fixRedEye(pic)
                elif rec == "No" or rec == "no":
                    savePicture(pic,"red-eye fixed.jpg")
                    print("According to you, the red-eye was found (this time around) in:", aList)
                    print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                    return None

            if i3 == "No" or i3 == "no":
                pic4 = copyPicture(pic)
                for x in range((w//4)*3,w):
                    for y in range(0,h//2):
                        pixel = getPixel(pic4, x,y)
                        setRed(pixel,0)
                        setGreen(pixel,0)
                        setBlue(pixel,0)
                show(pic4)
                i4 = input(("Did I just cover up the red-eye? Yes or no"))


#--------------------------------------------------------------------------------
#Confirming red-eye or not block 4


                if i4 == "Yes" or i4 == "yes":
                    for x in range((w//4)*3,w):
                        for y in range(0,h//2):
                            pixel = getPixel(pic, x,y)
                            r = getRed(pixel)
                            g = getGreen(pixel)
                            b = getBlue(pixel)
                            if r>80 and b<50 and g<50:
                                setRed(pixel,45)
                                setGreen(pixel,45)
                                setBlue(pixel,45)

                    aList.append("Block 4")
                    show(pic)
                    rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
                    if rec == "Yes" or rec == "yes":
                        print("According to you, the red-eye was found (this time around) in:", aList)
                        print("Onto the next run-through!")
                        fixRedEye(pic)
                    elif rec == "No" or rec == "no":
                        savePicture(pic,"red-eye fixed.jpg")
                        print("According to you, the red-eye was found (this time around) in:", aList)
                        print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                        return None

                if i4 == "No" or i4 == "no":
                    pic5 = copyPicture(pic)
                    for x in range(0,w//4):
                        for y in range(h//2,h):
                            pixel = getPixel(pic5, x,y)
                            setRed(pixel,0)
                            setGreen(pixel,0)
                            setBlue(pixel,0)
                    show(pic5)
                    i5 = input(("Did I just cover up the red-eye? Yes or no"))

#--------------------------------------------------------------------------------
#Confirming red-eye or not block 5

    
                    if i5 == "Yes" or i5 == "yes":
                        for x in range(0,w//4):
                            for y in range(h//2,h):
                                pixel = getPixel(pic, x,y)
                                r = getRed(pixel)
                                g = getGreen(pixel)
                                b = getBlue(pixel)
                                if r>80 and b<50 and g<50:
                                    setRed(pixel,45)
                                    setGreen(pixel,45)
                                    setBlue(pixel,45)

                        aList.append("Block 5")
                        show(pic)
                        rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
                        if rec == "Yes" or rec == "yes":
                            print("According to you, the red-eye was found (this time around) in:", aList)
                            print("Onto the next run-through!")
                            fixRedEye(pic)
                        elif rec == "No" or rec == "no":
                            savePicture(pic,"red-eye fixed.jpg")
                            print("According to you, the red-eye was found (this time around) in:", aList)
                            print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                            return None

                    if i5 == "No" or i5 == "no":
                        pic6 = copyPicture(pic)
                        for x in range(w//4,w//2):
                            for y in range(h//2,h):
                                pixel = getPixel(pic6, x,y)
                                setRed(pixel,0)
                                setGreen(pixel,0)
                                setBlue(pixel,0)
                        show(pic6)
                        i6 = input(("Did I just cover up the red-eye? Yes or no"))


#--------------------------------------------------------------------------------
#Confirming red-eye or not block 6

    
                        if i6 == "Yes" or i6 == "yes":
                            for x in range(w//4,w//2):
                                for y in range(h//2,h):
                                    pixel = getPixel(pic, x,y)
                                    r = getRed(pixel)
                                    g = getGreen(pixel)
                                    b = getBlue(pixel)
                                    if r>80 and b<50 and g<50:
                                        setRed(pixel,45)
                                        setGreen(pixel,45)
                                        setBlue(pixel,45)

                            aList.append("Block 6")
                            show(pic)
                            rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
                            if rec == "Yes" or rec == "yes":
                                print("According to you, the red-eye was found (this time around) in:", aList)
                                print("Onto the next run-through!")
                                fixRedEye(pic)
                            elif rec == "No" or rec == "no":
                                savePicture(pic,"red-eye fixed.jpg")
                                print("According to you, the red-eye was found (this time around) in:", aList)
                                print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                                return None
    
                        if i6 == "No" or i6 == "no":
                            pic7 = copyPicture(pic)
                            for x in range(w//2,(w//4)*3):
                                for y in range(h//2,h):
                                    pixel = getPixel(pic7, x,y)
                                    setRed(pixel,0)
                                    setGreen(pixel,0)
                                    setBlue(pixel,0)
                            show(pic7)
                            i7 = input(("Did I just cover up the red-eye? Yes or no"))


#--------------------------------------------------------------------------------
#Confirming red-eye or not block 7


                            if i7 == "Yes" or i7 == "yes":
                                for x in range(w//2,(w//4)*3):
                                    for y in range(h//2,h):
                                        pixel = getPixel(pic, x,y)
                                        r = getRed(pixel)
                                        g = getGreen(pixel)
                                        b = getBlue(pixel)
                                        if r>80 and b<50 and g<50:
                                            setRed(pixel,45)
                                            setGreen(pixel,45)
                                            setBlue(pixel,45)

                                aList.append("Block 7")
                                show(pic)
                                rec = input(("Is there still more red-eye to be fixed in the picture? Yes or no"))
                                if rec == "Yes" or rec == "yes":
                                    print("According to you, the red-eye was found (this time around) in:", aList)
                                    print("Onto the next run-through!")
                                    fixRedEye(pic)
                                elif rec == "No" or rec == "no":
                                    savePicture(pic,"red-eye fixed.jpg")
                                    print("According to you, the red-eye was found (this time around) in:", aList)
                                    print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                                    return None

                            if i7 == "No" or i7 == "no":
                                pic8 = copyPicture(pic)
                                for x in range((w//4)*3,w):
                                    for y in range(h//2,h):
                                        pixel = getPixel(pic8, x,y)
                                        setRed(pixel,0)
                                        setGreen(pixel,0)
                                        setBlue(pixel,0)
                                show(pic8)
                                i8 = input(("Did I just cover up the red-eye? Yes or no"))

#--------------------------------------------------------------------------------
#Confirming red-eye or not block 7


                                if i8 == "Yes" or i8 == "yes":
                                    for x in range((w//4)*3,w):
                                        for y in range(h//2,h):
                                            pixel = getPixel(pic, x,y)
                                            r = getRed(pixel)
                                            g = getGreen(pixel)
                                            b = getBlue(pixel)
                                            if r>80 and b<50 and g<50:
                                                setRed(pixel,45)
                                                setGreen(pixel,45)
                                                setBlue(pixel,45)

                                    aList.append("Block 8")
                                    show(pic)
                                    print("That was the end of the check! Here is your final picture.")
                                    print("According to you, the red-eye was found (this time around) in:", aList)
                                    savePicture(pic,"red-eye fixed.jpg")
                                    print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                                    return None
    
                                if i7 == "No" or i7 == "no":
                                    print("Well I guess there was no red-eye left in the photo.")
                                    print("That was the end of the check!")

                                    savePicture(pic,"red-eye fixed.jpg")
                                    print("I've saved your picture as 'red-eye fixed.jpg'. Have a nice day!")
                                    return None