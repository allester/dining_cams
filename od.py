#import tensorflow as tf
'''
import matplotlib.pyplot as plt
import numpy as np
import time
import os
from PIL import Image

print('he;')

image = Image.open("/Users/allester/Documents/dining_cams/data/bee1.png")
image.thumbnail((64,64))
imgplot = plt.imshow(image)
imgplot

'''

4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
def get_list_avg(nums):
    positives = []
    
    if len(nums) == 0:
        return -1
        
    for i in range(len(nums)):
        if nums[i] < 0:
            break
        else:
            positives.append(nums[i])
     
    return sum(positives)/len(positives)
    
if __name__ == "__main__":
    assert get_list_avg([10, 1, 6, 3, -1, 5, 9]) == 5
    assert get_list_avg([]) == -1
    assert get_list_avg([1,2,3,-1]) == 2
def get_list_avg(nums):
    positives = []
    
    if len(nums) == 0:
        return -1
        
    for i in range(len(nums)):
        if nums[i] < 0:
            break
        else:
            positives.append(nums[i])
     
    return sum(positives)/len(positives)
    
if __name__ == "__main__":
    assert get_list_avg([10, 1, 6, 3, -1, 5, 9]) == 5
    assert get_list_avg([]) == -1
    assert get_list_avg([1,2,3,-1]) == 2
