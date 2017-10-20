FROM python:3-onbuild
COPY app/  /usr/src/app
CMD ["python", "app.py"]

EXPOSE 8888
