
from pyscript import document

club_members = [
    "Laine Cajanding",
    "Jaeden Del Prado",
    "Margareth Chiong",
    "Jose Salacup"
]

def check_member(event):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    messages = [
        "Sorry " + full_name + ", your name is not on the list.",
        "Congratulations " + full_name + "! You are now part of the ICT club."
    ]

    document.getElementById("result").innerText = messages[is_member]
