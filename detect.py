#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging

from tutorons.core.extractor import Region
from insights import INSIGHTS

logging.basicConfig(level=logging.INFO, format="%(message)s")


java_class_patterns = []

for insight in INSIGHTS:
    if insight['class'] not in java_class_patterns:
        java_class_patterns.append(insight['class'])


class JavaClassesExtractor(object):
    ''' Finds regions of explainable code in HTML elements. '''

    def extract(self, node):
        '''
        Detect explainable regions of code in an HTML element.

        Args:
            node: an HTML element (it's a node created by BeautifulSoup
                  parsing HTML)

        Returns:
            A list of `Region`s, each containing a piece of detected code and
            a link to its unique location in the page.
        '''
        
        # Get the text contained in the HTML element
        text = node.text

        # Initialize the list of regions outside of the for-loop: this list 
        # should contain regions found for *all* patterns.
        regions = []

        for pattern in java_class_patterns:
            
            # Reset pointer for substring match to the beginning of the text,
            # for each class.
            last_match_end = 0

            # The entirety of the `while True` loop will need to be indented
            # inside this for loop. The `return` statement should be outside of
            # the for loop.
            while True:

                # Although the pattern detection shown here is specific to this
                # example, this code computes offsets and makes regions in a way 
                # you'll have to do in your own code.

                # You need to detect the index of the character where the code
                # was detected.
                match_start = text.find(pattern, last_match_end)
                if match_start == -1:
                    break

                # You also need to detect the index where the code stops.  Make
                # sure this points to the last character in the code and not
                # to the first character after the code.
                match_end = match_start + len(pattern) - 1

                # Every region needs to include a reference to the node it was 
                # extracted from, the index of the first character where the code
                # was detected within that element, the index of the last character
                # of the detected code, and the code itself.
                matching_region = Region(
                    node=node,
                    start_offset=match_start,
                    end_offset=match_end,
                    string=pattern,
                )

                regions.append(matching_region)

                # Save the end index of this match so it can be used to advance
                # the text search in the next loop iteration.
                last_match_end = match_end

        return regions
