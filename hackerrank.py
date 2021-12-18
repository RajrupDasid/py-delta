year=int(input("Eneter here"))
def is_leap(year):
    leap=False
    if year%4==0 or year % 400==0 or year%100==0:
        leap=True
    return leap