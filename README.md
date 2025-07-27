long string = ADOBECODEBANC
target string = ABC

Find the smallest possible stretch of the long string that has every letter from the target string at least once. I am assuming that the target string does not contain duplicate letters.

![solution for example](image.png)

The problem is solved because Tech for Tim suggests that a smart solution can get me a job at NVidia. 

https://www.youtube.com/shorts/dvJ5IRtlyec

I chose to use a dictionary in order to define a sliding window. If the same letter occurs twice, then the first occurrence is overridden. Thus, I do not have to check for duplicates in the long_string and the substring is automatically shortened. The maximum length of the dictionary is automatically equal to the length of the target string. 