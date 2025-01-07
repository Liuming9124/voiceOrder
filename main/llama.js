async function run(model, input) {
    const response = await fetch(
        `https://api.cloudflare.com/client/v4/accounts/ca277e8ebbda38d0e97fab9d8868d9c8/ai/run/${model}`,
        {
            headers: { Authorization: "Bearer WCRQ8kr4ebB8tWe-2k2YJnblTkNN-ncBJXEHH22V" },
            method: "POST",
            body: JSON.stringify(input),
        }
    );
    const result = await response.json();
    return result;
}


run("@cf/meta/llama-3-8b-instruct", {
    messages: [
        {
            role: "system",
            content: "You are a friendly assistan that helps write stories",
        },
        {
            role: "user",
            content:
                "Write a short story about a llama that goes on a journey to find an orange cloud ",
        },
    ],
}).then((response) => {
    console.log(JSON.stringify(response));
});