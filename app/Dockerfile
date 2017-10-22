FROM python:2.7-onbuild
RUN touch /usr/src/app/requirements.txt
COPY . /usr/src/app
CMD ["python", "app.py"]

EXPOSE 8888
