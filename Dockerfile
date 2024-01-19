FROM python:3
EXPOSE 8081
ADD . /torque
ENV URL="http://@/<homeassistant_ip>:8123"
ENV EMAIL="name@example.com"
ENV BEARER="xxx.xxx.xxx"

WORKDIR /torque
RUN pip3 install requests 
CMD ["python", "./torque.py"]


