courseraprogramming sanity -f Dockerfile 

docker build -t coursera_do_grader .
#docker run coursera_do_grader

# test it locally
#courseraprogramming grade local coursera_do_grader ../knapsack/_AKXWc AKXWc
./test_docker_container.py

# save it
#docker save coursera_do_grader > coursera_do_grader.v<x>.tar

# upload tar and update all graders
