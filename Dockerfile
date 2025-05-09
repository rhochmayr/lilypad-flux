
FROM pytorch/pytorch:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y git
RUN pip install uv
RUN uv pip install -r requirements.txt --system
RUN uv pip install --upgrade torch torchvision --system

# Set the entry point for your application
CMD ["python3", "app.py","--gradio"]