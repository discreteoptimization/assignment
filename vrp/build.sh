cd ..
rm starter_files/vrp.zip

cd handouts
rm vrp.pdf
rm *.aux *.dvi *.log
pdflatex vrp.tex
pdflatex vrp.tex
cp vrp.pdf ../vrp/handout.pdf
cd ..

cp submit.py vrp

zip vrp.zip vrp/solver.py vrp/submit.py vrp/_coursera vrp/handout.pdf vrp/data/vrp_*
mv vrp.zip starter_files
rm vrp/submit.py
rm vrp/handout.pdf

cd vrp
