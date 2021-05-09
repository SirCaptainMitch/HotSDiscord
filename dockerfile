FROM python:3
COPY . /app
WORKDIR /app
# Update Ubuntu Software repository
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get -y install \
    apt-transport-https \
    apt-utils \
    autoconf \
    curl \
    libcurl4 \
    g++ \
    gcc    \
    git \
    lcov \
    libxml2-dev \
    locales \
    make \
    python-pip \
    re2c \
    unixodbc-dev \
    unzip && apt-get clean && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get -y update && \
    export ACCEPT_EULA=Y && apt-get -y install msodbcsql17 mssql-tools

# update PATH after ODBC driver and tools are installed
ENV PATH="/opt/mssql-tools/bin:${PATH}"	
EXPOSE 5001
RUN pip install -r requirements.txt 
# CMD tail -f /dev/null
ENTRYPOINT [ "python" ]
CMD [ "application.py" ]