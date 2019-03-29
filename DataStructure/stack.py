
class sumarize:

    def __init__(self):
        print("Object Created !!")

    def breif(self,file):
       f = file
       counts = dict()
       words = f.split()

       for word in words:
       	if word in counts:
       		counts[word] += 1
       	else:
       		counts[word] = 1

       return counts