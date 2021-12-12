
# SQL Server Command Line Tools
FROM cap-base:latest
ARG DEBIAN_FRONTEND=noninteractive

# # adding custom MS repository
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
#
RUN apt-get update
#
# # install SQL Server drivers and tools
# RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# RUN /bin/bash -c "source ~/.bashrc"
#
#
#
# RUN apt-get -y install locales
# RUN locale-gen en_US.UTF-8
# RUN update-locale LANG=en_US.UTF-8
#


CMD /bin/bash
