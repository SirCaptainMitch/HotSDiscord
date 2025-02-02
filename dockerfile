
# # SQL Server Command Line Tools
FROM cap-base:latest
ARG DEBIAN_FRONTEND=noninteractive
ARG ACCEPT_EULA=Y

# # adding custom MS repository

RUN apt-get update

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/msprod.list


# # install SQL Server drivers and tools
RUN apt-get update &&  apt-get install -y mssql-tools unixodbc-dev
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"


RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

COPY . /app
WORKDIR /app

EXPOSE 50001
RUN pip install -r requirements.txt
# CMD tail -f /dev/null
ENTRYPOINT [ "python" ]
CMD [ "application.py" ]
