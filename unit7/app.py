from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "You've been imprisoned!"
    
    text = """You are a part of a criminal gang and you and your mate're arrested.
    Your are in solitary confinement with no means of speaking to your mate.

    It is a dark and cold in cell. You want to get out as soon as possible...

    The police admit they don't have enough evidence to convict you on the principal charge. 
    They plan to sentence you to a year in prison on a lesser charge.
    However, the police is kind today and offer each of you a bargain.

    The possible outcomes are:
    
    If you and your mate betray each other, each of you serves 10 years in prison
    If you betray your mate but your mate  remains silent, you will be set free and your mate will serve 5 years in prison
    If you remain silent but your mate betrays you, you will serve 5 years in prison and your mate will be set free
    If you both remain silent, both of you will serve one year in prison on the lesser charge.

    What do you do?
    """

    choices = [
        ('remain_silent',"Remain silent"),
        ('betray',"Betray your mate")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/silent")
def remain_silent():
    title = "You remained silent..."
    
    text = """... and your mate ramained silent. 
    Now police is mad, they want to convict someone on the principal charge.. 
    They start to push you and your mate... 
    You are really scared..Police offer each of you the same bargain again.

    The possible outcomes are the same:
    
    If you and your mate betray each other, each of you serves 10 years in prison
    If you betray your mate but your mate  remains silent, you will be set free and your mate will serve 5 years in prison
    If you remain silent but your mate betrays you, you will serve 5 years in prison and your mate will be set free
    If you both remain silent, both of you will serve one year in prison on the lesser charge.

    What do you do?"""

    choices = [
        ('remain_silent_still',"Still remain silent"),
        ('betray',"Betray your mate")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/betray")
def betray():
    title = "You betrayed your mate! You're screwed!"
    
    text = """Your mate betrayed you too. Police is happy, now they completely solved the case.

    You and your mate will serve 10 years!!

    Don't be selfish in your next crime!"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/stillsilent")
def remain_silent_still():
    title = "You remained silent..you were strong"
    
    text = """and your mate remained silent!
    
    Police lost the evidence for small charge.
    
    You and your mate are free! 
    
    Nice job! You win!"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
