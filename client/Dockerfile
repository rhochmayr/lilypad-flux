FROM fluxwebui
RUN mkdir /output
WORKDIR /app
RUN pip3 install gradio_client
RUN echo -e '#!/bin/sh\npython3 app.py & python3 client/cli.py' > /app/run.sh
RUN chmod +x /app/run.sh
ENTRYPOINT  "/app/run.sh" 
#  [ "python3", "/cli/client/cli.py" ]