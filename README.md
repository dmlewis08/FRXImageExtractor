This python script can extract an image file from a visual basic `.frx` file.  
The command-line prompts will ask for the file path to the `.frx` file, and then for the offset for the image (these must be obtained from the corresponding `.frm` file).  
The offset can be entered in decimal format or as hexadecimal - if hexadecimal, use the prefix `0x` before the number (e.g., "0x0000").

## IMPORTANT NOTES:
- This has only been tested using bitmap files.
- This was written using Python version 3.8.10
- This requires the PIL package, which can be obtained through PIP as "pillow" (at the time of writing, pillow version 10.2.0 was used)  
```
pip install pillow==10.2.0
```
