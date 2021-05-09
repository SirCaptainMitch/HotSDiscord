import re

def findTexts(message):
    allTexts = []
    wholeText = message.content.lower()
    for text in wholeText.split('\n'):
        if '>' in text and '<' not in text:  # This line is a quote
            continue
        # Must escape brackets when using regex
        leftBrackets = [1+m.start() for m in re.finditer('\[', text)]
        rightBrackets = [m.start() for m in re.finditer('\]', text)]
        texts = [text[leftBrackets[i]:rightBrackets[i]].split(
            '/') for i in range(len(rightBrackets))]
        if len(leftBrackets) > len(rightBrackets):  # One extra unclosed at end
            texts.append(text[leftBrackets[-1]:].split('/'))
        allTexts += texts
    return allTexts