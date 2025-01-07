import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/ca277e8ebbda38d0e97fab9d8868d9c8/ai/run/"
headers = {"Authorization": "Bearer SIz_6SJHZgNOmExgGNyNC24KaO53oaQIuEnTQucl"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)