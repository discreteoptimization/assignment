# Fetch latest ubuntu docker image
FROM gcc:latest

# Install Python on the ubuntu image.
RUN \
  apt-get update && \
  apt-get install -y python2.7 && \
  apt-get install -y unzip

#COPY execute_grader.sh /

# Setup directories
RUN mkdir /grader

# Setup grader
COPY do_grader.zip  /grader

RUN cd grader && unzip -o do_grader.zip && rm do_grader.zip

# Needed so grader can write mzn files
# RUN chmod a+rwx -R /grader/

# Setup the command that will be invoked when your docker image is run.
ENTRYPOINT ["grader/do_grader.py"]
