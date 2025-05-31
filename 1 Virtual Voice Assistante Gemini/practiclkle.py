import webbrowser

def webpage(web):
    websites = {
        "github" : "https://github.com/Rustam-Singh-Bhadouriya"
    }

    # Convert the input to lowercase
    command = web.lower()

    for site in websites:
        if site in command:
            webbrowser.open(websites[site])
            return  # Exit once the correct site is opened

# Call the function with a command
webpage("Github")
