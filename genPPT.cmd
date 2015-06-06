xelatex -output-driver="xdvipdfmx -V 5" ppt.tex
bibtex ppt.aux
xelatex -output-driver="xdvipdfmx -V 5" ppt.tex
