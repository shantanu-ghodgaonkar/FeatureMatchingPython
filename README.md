# FeatureMatchingPython
Finding Waldo — Feature Matching for OpenCV in Python

‘Where’s Wally’ is a popular British series of puzzle books. Finding Wally is not easy and OpenCV has a way that can allow us to find him quickly and easily.

OpenCV has a function, cv2.MatchTemplate() that supports template matching to identify the target image.

Template Matching is the idea of sliding a target image(template) over a source image (input). The template is compared to the input. A match is determined by the how much the neighbourhood pixels in the input matches with the template.
There are various methods as to how the calculation of similarity is determined. For this example, we will be using TM.CCOEFF_NORMED



The template patch is slid over the input with this matrix and it determines a score that will indicate whether there is a match. TM_CCOEFF_NORMED finds the average value of the template and matches it to the average of the input. A score of 1 is a perfect match, -1 is a bad match and 0 is neutral.
