# PyComputerVisionLines
This is two simple programs that use computer vision to detect lines, one outputs a screenshot overlayed with red lines, the other outputs only the red lines on a black background.

+ Created using www.perplexity.ai

# Settings
+ You can set the delay before a screenshot is taken here (10):
    time.sleep(10)
    
+ You can set the filtering for line detection here (50, 150, apertureSize=3 or 5 or 7):
    edges = cv2.Canny(equ, 50, 150, apertureSize=3)
