cd handouts
  ./clean.sh
cd ..


cd anyint
  ./build.sh
cd ..

cd knapsack
  ./build.sh
cd ..

cd coloring
  ./build.sh
cd ..

cd tsp
  ./build.sh
cd ..

cd facility
  ./build.sh
cd ..

cd vrp
  ./build.sh
cd ..

cd setcover
  ./build.sh
cd ..


rm docker/do_grader.zip

zip do_grader.zip do_grader.py do_grader_lib.py \
  anyint/_coursera anyint/_metadata_grader anyint/grader.py \
  knapsack/_coursera knapsack/_metadata_grader knapsack/grader.py knapsack/data/ks_* \
  coloring/_coursera coloring/_metadata_grader coloring/grader.py coloring/data/gc_* \
  facility/_coursera facility/_metadata_grader facility/grader.py facility/data/fl_* \
  setcover/_coursera setcover/_metadata_grader setcover/grader.py setcover/data/sc_* \
  tsp/_coursera tsp/_metadata_grader tsp/grader.py tsp/data/tsp_* \
  vrp/_coursera vrp/_metadata_grader vrp/grader.py vrp/data/vrp_* 

mv do_grader.zip docker

