FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python3 -m prisma generate
EXPOSE 5000
CMD python ./run.py
# FROM python:3.9