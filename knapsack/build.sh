cd ..
rm starter_files/knapsack.zip

cd handouts
rm knapsack.pdf
rm *.aux *.dvi *.log
pdflatex knapsack.tex
pdflatex knapsack.tex
cp knapsack.pdf ../knapsack/handout.pdf
cd ..

cp submit.py knapsack

zip knapsack.zip knapsack/submit.py knapsack/solver.py knapsack/solverJava.py knapsack/Solver.java knapsack/_coursera knapsack/handout.pdf knapsack/data/ks_*
mv knapsack.zip starter_files
rm knapsack/submit.py
rm knapsack/handout.pdf

cd knapsack
