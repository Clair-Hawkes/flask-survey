from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get('/')
def home_page():
    """Take user to home page"""

    title = survey.title
    instructions = survey.instructions

    return render_template(
        "survey_start.html",
        title=title,
        instructions=instructions)


@app.post('/begin')
def start_survey():
    """Take user to a first question page"""

    return redirect('/begin')


@app.post('/answer')
def handle_answer():
    """Log answer and redirect user to question page"""

    user_choice = request.form.get('answer')
    responses.append(user_choice)

    return redirect('/begin')


@app.get('/begin')
def handle_next():
    """Takes user to next cycled question page.
    Or take user to survey completion page"""

    questions = survey.questions

    if (len(responses) == len(questions)):
        return render_template('completion.html')

    else:

        question_num = len(responses)
        question = questions[question_num].question
        list_of_choices = survey.questions[question_num].choices

        return render_template("question.html",
        question=question,choices=list_of_choices)





# @app.post('/answer')
# def handleAnswer():
#     """Doc String"""

#     choice = request.form
#     print(choice)

#     return render_template('completion.html')



# @app.post('/begin')
# def handle_question():
#     """take user to a question page, """

#     question_num = len(responses)

#     questions = survey.questions
#     question = questions[question_num].question

#     list_of_choices = survey.questions[question_num].choices

#     return render_template("question.html",
#     question=question,choices=list_of_choices)






