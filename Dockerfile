FROM selenium/standalone-firefox:4.1.2-20220131

USER root
RUN apt-get update -yqq && \
    apt-get install -yqq python3-pip python-is-python3 && \
    pip install requests selenium lxml

USER seluser
COPY scrape_quotes.py /home/seluser
WORKDIR /home/seluser

ENTRYPOINT [ "python", "/home/seluser/scrape_quotes.py"]
