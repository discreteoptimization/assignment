cd ..
rm starter_files/facility.zip

cd handouts
rm facility.pdf
rm *.aux *.dvi *.log
pdflatex facility.tex
pdflatex facility.tex
cp facility.pdf ../facility/handout.pdf
cd ..

cp submit.py facility

zip facility.zip facility/solver.py facility/submit.py facility/_coursera facility/handout.pdf facility/data/fl_*
mv facility.zip starter_files
rm facility/submit.py
rm facility/handout.pdf

cd facility
