FROM python:3.9-slim

WORKDIR /lab_1

COPY . .

RUN FROM python:3.9-slim

WORKDIR /lab_1

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-m", "unittest", "code_unittest.py"]

CMD ["python", "-m", "unittest", "code_unittest.py"]