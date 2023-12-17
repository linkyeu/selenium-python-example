FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y software-properties-common wget unzip openjdk-11-jdk chromium-browser chromium-driver python3 python3-pip

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
ENV PATH $JAVA_HOME/bin:$PATH

WORKDIR /usr/src/app

RUN wget https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.zip -O /tmp/allure.zip && \
    unzip /tmp/allure.zip -d /opt/ && \
    rm -f /tmp/allure.zip

ENV PATH="/opt/allure-2.13.8/bin:${PATH}"

COPY requirements.txt ./
COPY reports ./reports
COPY tests/ ./tests/
COPY results/ ./results/

RUN pip install -r requirements.txt

# Команда для запуска тестов
CMD ["bash"]


