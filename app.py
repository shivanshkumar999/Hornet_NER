from flask import Flask, render_template, request
import spacy

# Create Flask objection with name parameter 
app = Flask(__name__)


# create app default route
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        output = []
        # try except for any exceptions to be entered as in errors
        try:
            # User input fetching
            query = request.form.get("query")

            # Model Loading
            ner = spacy.load("en_core_web_sm")

            # Final Query execution
            query_res = ner(query)

            for entity in query_res.ents:
                output.append(entity.text)

            # Storing data
            final_output = {
                "pii_identified" : output,
                "error":"nill"
            }

        except Exception as error:
            # return an exception if any
            final_output = {
                "pii_identified" : "",
                "error": error
            }

        return render_template('index.html', output=final_output)
    return render_template('index.html')

# Driver function
if __name__=='__main__':
    app.run(debug=True)
