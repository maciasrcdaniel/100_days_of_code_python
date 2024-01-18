#!/usr/bin/env python3

import math

test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5

def paint_calc(height, width, cover):
    required_cans = (height * width) / coverage
    whole_cans_required = math.ceil(required_cans)
    print(f"You'll need {whole_cans_required} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)
