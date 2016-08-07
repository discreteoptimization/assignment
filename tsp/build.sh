cd ..
rm starter_files/tsp.zip

cd handouts
rm tsp.pdf
rm *.aux *.dvi *.log
pdflatex tsp.tex
pdflatex tsp.tex
cp tsp.pdf ../tsp/handout.pdf
cd ..

cp submit.py tsp

zip tsp.zip tsp/solver.py tsp/submit.py tsp/_coursera tsp/handout.pdf tsp/data/tsp_*
mv tsp.zip starter_files
rm tsp/submit.py
rm tsp/handout.pdf

cd tsp
