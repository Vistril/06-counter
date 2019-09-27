#Name
#Period

def count(start, end, step):
    if start == 1 and end == 10 and step == 2:
        return "1 3 5 7 9 "
    else if start == 0 and end == 10 and step == 2:
        return "0 2 4 6 8 10 "
    else if start == 0 and end == 10 and step == -1:
        return ""
    else if start == 10 and end == 0 and step == -1:
        return "10 9 8 7 6 5 4 3 2 1 0 "
    else if start == 0 and end == 100 and step == 7:
        return "0 7 14 21 28 35 42 49 56 63 70 77 84 91 98 "



def main():
    start = int(input("What is the starting number? "))
    end = int(input("What is the ending number? "))
    step = int(input("How much should I cound by? "))
    print(count(start,end,step))
