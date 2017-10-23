FROM jenkins/jenkins:2.73.2
USER root
RUN apt-get update
RUN apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common -y
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install docker-ce -y
RUN usermod -a -G docker jenkins

EXPOSE 8080
