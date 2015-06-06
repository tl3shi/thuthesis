xelatex -output-driver="xdvipdfmx -V 5"  pptWithNotes.tex
bibtex pptWithNotes.aux
xelatex -output-driver="xdvipdfmx -V 5"  pptWithNotes.tex
