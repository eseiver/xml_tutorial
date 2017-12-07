# Tutorial for 2017 allofplos presentation at UC BIDS
allofplos: www.github.com/PLOS/allofplos  
event info: http://www.thehackerwithin.org/berkeley/posts/2017-11-29-allofplos-f17.html

## To run the slideshow in reveal.js

### Python packages needed
* nbconvert

### Run
```
git clone eseiver/xml_tutorial
cd xml_tutorial
jupyter nbconvert --to slides allofplos_presentation.ipynb --post serve --config=hidecodeconfig.py --no-prompt
```
Note that the first slide is blank.
