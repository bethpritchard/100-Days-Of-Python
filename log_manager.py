"""
Produces 10 day log for 100DaysOfCode
"""

from datetime import date, timedelta
import os,sys
import os.path
from os import path

START_DAY = 31
end_day = START_DAY + 10


if path.exists(f'log/days{START_DAY}-{end_day - 1}.md'):
    print("File already exists.")

else:
    with open(f"log/days{START_DAY}-{end_day - 1}.txt", "a") as new_log:
        for i in range(10):
            d = date.today() + timedelta(days=i)
            d2 = d.strftime("%d %B %Y")
            new_day = f"""
### Day {START_DAY + i}: {d2}
**Today's progress:**
    
**Today I've learned about:**
    
**Thoughts:**
    
**Link to work:**

* [](https://github.com/bethpritchard/100DaysOfCodeBootcamp/blob/master/)
    \n
    """
            new_log.write(new_day)

# ----------- Change to md file ------------
folder = 'log'
try:

    for filename in os.listdir(folder):
           infilename = os.path.join(folder,filename)
           if not os.path.isfile(infilename): continue
           oldbase = os.path.splitext(filename)
           newname = infilename.replace('.txt', '.md')
           output = os.rename(infilename, newname)
except FileExistsError:
    print("File already exists")