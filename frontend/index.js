async function main() {
    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: "How can I make my CV more ATS friendly?"
        })
    });

    const data = await response.json();

    console.log(data);
}

main();