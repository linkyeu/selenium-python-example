FROM ubuntu:latest
RUN apt-get update && apt-get install -y software-properties-common wget unzip openjdk-11-jdk python3 python3-pip
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
ENV PATH $JAVA_HOME/bin:$PATH

# Добавление ключа Google и репозитория Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

RUN apt-get update && apt-get install -y google-chrome-stable
WORKDIR /usr/src/app

RUN wget https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.zip -O /tmp/allure.zip && \
    unzip /tmp/allure.zip -d /opt/ && \
    rm -f /tmp/allure.zip

ENV PATH="/opt/allure-2.13.8/bin:${PATH}"
COPY docker .
RUN pip install -r requirements.txt
CMD ["bash"]
