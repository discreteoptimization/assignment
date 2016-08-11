cd ..
rm starter_files/anyint.zip

cd handouts
rm anyint.pdf
rm *.aux *.dvi *.log
pdflatex anyint.tex
pdflatex anyint.tex
cp anyint.pdf ../anyint/handout.pdf
cd ..

cp submit.py anyint

rm anyint.zip
zip anyint.zip anyint/solver.py anyint/submit.py anyint/_coursera anyint/handout.pdf 
mv anyint.zip starter_files
rm anyint/submit.py
rm anyint/handout.pdf

cd anyint
