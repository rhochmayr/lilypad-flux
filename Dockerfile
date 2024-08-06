
FROM pytorch/pytorch:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
RUN pip install --upgrade torch torchvision

# Set the entry point for your application
CMD ["python3", "app.py"]