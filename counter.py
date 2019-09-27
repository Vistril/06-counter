#Name
#Period

def count(start, end, step):
    ints = []
    sep = ' '
    if step == -1 and start > end:
        return ""
    else: 
        for i in range(start, end, step):
            ints.append(str(i))
         
    return sep.join(ints) + " "




def main():
    start = int(input("What is the starting number? "))
    end = int(input("What is the ending number? "))
    step = int(input("How much should I cound by? "))
    print(count(start,end,step))
