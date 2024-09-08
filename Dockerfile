FROM python:3.10-slim
WORKDIR /app
COPY ./app .

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000