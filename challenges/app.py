from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# For demo purposes, store partial codes in memory.
# In a real environment, you might store them in a database or generate them dynamically.
PARTIAL_CODES = {
    "challenge1": "elsys{R0l3s_4r3_FuN}",                   # Example partial code for Challenge 1
    "challenge2": "elsys{Who_Tought_you_decrypting}",       # Placeholder for Challenge 2
    "challenge3": "elsys{WHATT_YOU_ALSO_KNOW_ABOUT_THIS}",  # Placeholder for Challenge 3
    "challenge4": "elsys{sofia_tech_park}"                 # Placeholder for Challenge 4
}

@app.route("/")
def index():
    """
    Storyline introduction page.
    """
    # You can create a separate template or return text here. 
    # We'll render 'index.html' for a nicer layout.
    return render_template("index.html")

# --------------------
# CHALLENGE 1 - URL Manipulation
# --------------------
@app.route("/challenge1")
def challenge1():
    """
    URL manipulation challenge.
    The user must change '?role=guest' to '?role=admin' to get the partial code.
    """
    role = request.args.get("role", "guest")  # default to 'guest' if param not set
    if role.lower() == "admin":
        # If correct, show success
        partial_code = PARTIAL_CODES["challenge1"]
        return render_template(
            "challenge1.html",
            success=True,
            partial_code=partial_code
        )
    else:
        # If not correct, show 'Access Denied' style
        return render_template(
            "challenge1.html",
            success=False,
            partial_code=""
        )

# --------------------
# CHALLENGE 2 - Multi-encoding + Caesar Cipher (Placeholder)
# --------------------
@app.route("/challenge2", methods=["GET", "POST"])
def challenge2():
    """
    Placeholder for the multi-encoding + Caesar cipher challenge.
    - Show a text snippet that is partially Base64 encoded, partially Caesar-shifted.
    - The user decodes it to get the partial code.
    For now, we just display a placeholder page.
    """
    # If you want to let them submit their found code, you can handle it here:
    if request.method == "POST":
        user_solution = request.form.get("solution", "")
        # Check if user_solution matches PARTIAL_CODES["challenge2"] (or a derived correct answer).
        if user_solution == PARTIAL_CODES["challenge2"]:
            return redirect(url_for("challenge3"))
        else:
            return render_template("challenge2.html", error=True)
    
    return render_template("challenge2.html", error=False)

# --------------------
# CHALLENGE 3 - Image Steganography / EXIF (Placeholder)
# --------------------
@app.route("/challenge3", methods=["GET", "POST"])
def challenge3():
    """
    Placeholder for steganography/EXIF challenge.
    - Provide an image or a link to an image for participants to analyze.
    - The hidden data reveals PARTIAL_CODES["challenge3"].
    """
    # If participant tries to submit the discovered partial code:
    if request.method == "POST":
        user_solution = request.form.get("solution", "")
        if user_solution == PARTIAL_CODES["challenge3"]:
            return redirect(url_for("challenge4"))
        else:
            return render_template("challenge3.html", error=True)
    
    return render_template("challenge3.html", error=False)

# --------------------
# CHALLENGE 4 - Geolocation (Placeholder)
# --------------------
@app.route("/challenge4", methods=["GET", "POST"])
def challenge4():
    """
    Placeholder for the geolocation puzzle.
    - Show an image or description of an unusual landmark.
    - The participant uses reverse image search or clues to figure out location => partial code.
    """
    if request.method == "POST":
        user_solution = request.form.get("solution", "")
        if user_solution.lower().strip() == PARTIAL_CODES["challenge4"].lower().strip():
            return redirect(url_for("submit_solution"))
        else:
            return render_template("challenge4.html", error=True)
    
    return render_template("challenge4.html", error=False)

# --------------------
# FINAL SUBMISSION
# --------------------
@app.route("/submit", methods=["GET", "POST"])
def submit_solution():
    """
    Final page where the user enters all partial codes to claim the prize.
    Or, if you're collecting each partial code at the challenge route, 
    you might not need this. 
    """
    if request.method == "POST":
        code1 = request.form.get("code1", "")
        code2 = request.form.get("code2", "")
        code3 = request.form.get("code3", "")
        code4 = request.form.get("code4", "")
        
        # Simple check if all codes are correct
        if (code1 == PARTIAL_CODES["challenge1"] and
            code2 == PARTIAL_CODES["challenge2"] and
            code3 == PARTIAL_CODES["challenge3"] and
            code4 == PARTIAL_CODES["challenge4"]):
            
            # If correct, show success
            return render_template("success.html")
        else:
            # Otherwise, show an error
            return render_template("submit.html", error=True)
    
    return render_template("submit.html", error=False)

if __name__ == "__main__":
    app.run(debug=True)