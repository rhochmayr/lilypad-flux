import time
import requests
import shutil
from gradio_client import Client

def wait_for_server(url, timeout=60):
    """Wait for the server to be available."""
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Server is available at {url}")
                return
        except requests.ConnectionError:
            pass
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Server at {url} did not become available within {timeout} seconds")
        time.sleep(1)

# Wait for the server to be available
wait_for_server("http://localhost:7860")

client = Client("http://localhost:7860/")
result = client.predict(
		prompt="Hello!!",
		checkpoint="black-forest-labs/FLUX.1-schnell",
		seed=0,
		guidance_scale=0,
		num_images_per_prompt=1,
		randomize_seed=True,
		width=1024,
		height=576,
		num_inference_steps=4,
		api_name="/infer"
)
image_path = result[0][0]["image"]
destination_path = "/output/image.png"

# Move the file to the /output directory
shutil.move(image_path, destination_path)

print(f"Image moved to {destination_path}")