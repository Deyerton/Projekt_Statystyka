FROM python:3.8
COPY web /web
WORKDIR /web
RUN pip install -r requirements.txt
CMD ["python", "model.py"]