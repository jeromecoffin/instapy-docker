FROM ubuntu:focal
WORKDIR /code
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt -y update && \
    apt -y upgrade && \
    apt -y install unzip python3-pip python3-dev build-essential libssl-dev libffi-dev xvfb locales wget dpkg nano && \
    pip3 install --upgrade pip && \
    export LANGUAGE=en_US.UTF-8 && \
    export LANG=en_US.UTF-8 && \
    export LC_ALL=en_US.UTF-8 && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    pip3 install --upgrade pip && \
    apt -y install firefox && \
    pip3 install instapy && \
    apt -y install firefox-geckodriver && \
    yes | pip uninstall emoji && \
    yes | pip install emoji==1.7

COPY docker_quickstart.py /code/quickstart.py
COPY login_util.py /usr/local/lib/python3.8/dist-packages/instapy/login_util.py
COPY xpath_compile.py /usr/local/lib/python3.8/dist-packages/instapy/xpath_compile.py

CMD ["python3", "quickstart.py"]
