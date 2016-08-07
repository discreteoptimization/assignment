cd ..
rm starter_files/coloring.zip


cd handouts
rm coloring.pdf
rm *.aux *.dvi *.log
pdflatex coloring.tex
pdflatex coloring.tex
cp coloring.pdf ../coloring/handout.pdf
cd ..

cp submit.py coloring

zip coloring.zip coloring/submit.py coloring/solver.py coloring/_coursera coloring/handout.pdf coloring/data/gc_*
mv coloring.zip starter_files
rm coloring/submit.py
rm coloring/handout.pdf

cd coloring
