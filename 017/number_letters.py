#!/usr/bin/env python

from math import floor as floor

limit=1000

# Off the internet because lazy
dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: ''}


def generate_words(n):
    # Figured I might as well make a properly functioning word generator
    st=""
    and_toggle=0
    if floor(n/1000) > 0:
        st+=dict[floor(n/1000)]+" thousand "
        n-=floor(n/1000)*1000
    if floor(n/100) > 0:
        st+=dict[floor(n/100)]+" hundred "
        n-=floor(n/100)*100
    if n > 19:
        if st!="" and n!=0: st,and_toggle=st+"and ",1
        else: and_toggle=1
        st+=dict[floor(n/10)*10]
        n-=floor(n/10)*10
        if n!=0: st+="-"
    if n <= 19:
        if st!="" and and_toggle!=1 and n!=0: st+=" and "
        st+=dict[n]
    return st

    
tot=0
for i in range(1, limit+1):
    newline=filter(lambda ch: ch not in " -", generate_words(i))
    tot+=len(newline)    

print "Total characters: ", tot
