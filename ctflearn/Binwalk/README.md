## Binwalk
#### To solve this challenge it helps to have Binwalk installed. On the Command Line, type:
> $ binwalk --extract --dd=".*" PurpleThing.jpeg 
#### This will create a new directory. Go into the directory and you will see a file called 25795. Rename this file to a .png file.
> $ mv 25795 25795.png
#### The image will have the flag.