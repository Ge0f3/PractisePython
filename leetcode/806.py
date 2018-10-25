def numberOfLines(widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line =0
        line_len=0
        for c in S:
            char_width= widths[ord(c)-97]
            if(line_len+char_width >100):
                line+=1
                line_len=char_width
            if(line_len<100):
                line_len+=char_width
        if(line_len<100):
        	line+=1
        return [line,line_len]


widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
def main():
	print(numberOfLines(widths,S))


if __name__ == '__main__':
	main()