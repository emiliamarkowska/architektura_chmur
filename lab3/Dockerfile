FROM openjdk

WORKDIR /usr/src/app
RUN microdnf install findutils

COPY ./source/ ./
EXPOSE 4080

CMD [ "/bin/bash", "start.sh" ]

