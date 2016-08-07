cd ..
rm starter_files/setcover.zip

cd handouts
rm setcover.pdf
rm *.aux *.dvi *.log
pdflatex setcover.tex
pdflatex setcover.tex
cp setcover.pdf ../setcover/handout.pdf
cd ..

cp submit.py setcover

rm setcover.zip
zip setcover.zip setcover/solver.py setcover/submit.py setcover/_coursera setcover/handout.pdf setcover/data/sc_*
mv setcover.zip starter_files
rm setcover/submit.py
rm setcover/handout.pdf

cd setcover
