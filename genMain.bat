xelatex -output-driver="xdvipdfmx -V 5" main.tex
bibtex main.aux
xelatex -output-driver="xdvipdfmx -V 5" main.tex
