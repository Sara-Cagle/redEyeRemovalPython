fixRedEye()

This program is designed to examine photos taken with a flash and then reduce the red-eye effect.
Like any other red-eye removal program, even if red-eye exists in a photo, the program can only recognize what it is designed to recognize. Therefore, it will not be able to fix ALL red-eye problems. It also may pick up other non-red-eye sections such as dull red hair or red glasses. This is a problem seen not just in my program but also in professional programs such as Photoshop, and therefore should be disregarded.

This program works by splitting the photo into 8 parts and then subsequently covering each part. The program will ask the user each time if the red-eye has been covered by the black. If you can no longer see the red-eye in the photo due to it being covered, you should input input "yes". If you can still see the red-eye, indicating that it is in a different section, input "no" and the program will continue.

If there are multiple occurrences of red-eye or the red-eye spans multiple sections, after fixing one section, the program will ask if there is more red-eye to fix. If you input "yes", the program will run recursively until it reaches the new part. This will cover the initial areas of the photo where red-eye has been fixed, but following the simple questions, "Did I just cover up the red-eye? Yes or no:" will allow the user to run through the program to the other red-eye exposures. 

Once the user indicates that there is no more red-eye in the photo, the photo will save as "red-eye fixed.jpg".

It is important to note that if the red-eye is not detected or fixed during the program's first run through in its entirety, that specific red-eye does not fall within the program's scope and will not be detected on subsequent runs. 

I've included some example photos in a zipped file that can be used with the program. 