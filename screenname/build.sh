cd ..
rm starter_files/screenname.zip

cd handouts
rm screenname.pdf
rm *.aux *.dvi *.log
pdflatex screenname.tex
pdflatex screenname.tex
cp screenname.pdf ../screenname/handout.pdf
cd ..

cp submit.py screenname

rm screenname.zip
zip screenname.zip screenname/solver.py screenname/submit.py screenname/_coursera screenname/handout.pdf 
mv screenname.zip starter_files
rm screenname/submit.py
rm screenname/handout.pdf

cd screenname
