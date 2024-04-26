from flask import Flask, render_template, request
from IntervalValuedBipolarNeutrosophicSet import (
    IntervalValuedBipolarNeutrosophicSet as IVBNS,
)
from IntervalValuedBipolarNeutrosophicElement import (
    IntervalValuedBipolarNeutrosophicElement as IVBNE,
)

app = Flask(__name__)

@app.route("/")
def main():
    # Render the main HTML template
    return render_template("ivbns.html")

def extract_elements_from_set(input_set):
    # Extract elements from the input set string
    input_set = input_set.replace("\n", "").replace("\t", "").replace("\r", "")
    elements = []
    elements_string = input_set.strip("{}").split(">,<")

    for element in elements_string:
        element = element.replace("<", "").replace(">", "")

        # Split the element attributes
        parts = element.split(",")

        # Create a dictionary of element attributes
        element_attributes = {
            "parent": parts[0],
            "truth_pos_left": float(parts[1]),
            "truth_pos_right": float(parts[2]),
            "indeterminacy_pos_left": float(parts[3]),
            "indeterminacy_pos_right": float(parts[4]),
            "falsity_pos_left": float(parts[5]),
            "falsity_pos_right": float(parts[6]),
            "truth_neg_left": float(parts[7]),
            "truth_neg_right": float(parts[8]),
            "indeterminacy_neg_left": float(parts[9]),
            "indeterminacy_neg_right": float(parts[10]),
            "falsity_neg_left": float(parts[11]),
            "falsity_neg_right": float(parts[12]),
        }

        elements.append(element_attributes)

    return elements

def generate_object(extracted_elements):
    # Generate an IntervalValuedBipolarNeutrosophicSet object from extracted elements
    obj = IVBNS()

    for element in extracted_elements:
        obj.add_element(IVBNE(**element))

    return obj

@app.route("/", methods=["POST"])
def calculate():
    # Define unary and binary functions
    unary_functions = {
        "complement_1": IVBNS.complement,
        "complement_2": IVBNS.complement,
        "score_1": IVBNS.score,
        "score_2": IVBNS.score,
        "accuracy_1": IVBNS.accuracy,
        "accuracy_2": IVBNS.accuracy,
    }

    binary_functions = {
        "check_equality": IVBNS.__eq__,
        "check_subset": IVBNS.is_subset,
        "union": IVBNS.union,
        "intersection": IVBNS.intersection,
        "multiply": IVBNS.__mul__,
        "add": IVBNS.__add__,
    }

    matrix1_input = request.form.get("matrix1")
    matrix2_input = request.form.get("matrix2scalar")
    operation = request.form.get("submit_button")

    context = {"matrix1": matrix1_input, "matrix2": matrix2_input}

    # Validate input
    if not matrix1_input:
        context["alertmessage"] = True
        context["message"] = "Please check the provided inputs!"
        context["result"] = ""
        return render_template("ivbns.html", **context)

    try:
        matrix1 = generate_object(extract_elements_from_set(matrix1_input))
    except:
        context["alertmessage"] = True
        context["message"] = "Please check the provided inputs!"
        context["result"] = ""
        return render_template("ivbns.html", **context)

    if not operation:
        context["alertmessage"] = True
        context["message"] = "Please check the operation!"
        context["result"] = ""
        return render_template("ivbns.html", **context)

    # Process operation
    if matrix2_input:
        if operation != "multiply":
            try:
                matrix2 = generate_object(extract_elements_from_set(matrix2_input))
            except:
                context["alertmessage"] = True
                context["message"] = "Please check the provided inputs!"
                context["result"] = ""
                return render_template("ivbns.html", **context)

        elif operation == "multiply":
            try:
                matrix2 = generate_object(extract_elements_from_set(matrix2_input))
            except:
                try:
                    matrix2 = int(matrix2_input)
                except:
                    context["alertmessage"] = True
                    context["message"] = "Please check the provided inputs!"
                    context["result"] = ""
                    return render_template("ivbns.html", **context)

    # Execute the selected operation
    if operation.endswith("_1"):
        func = unary_functions.get(operation)
        if not func:
            context["alertmessage"] = True
            context["message"] = "Please check the operation and provided inputs!"
            context["result"] = ""
            return render_template("ivbns.html", **context)

        result = func(matrix1)
    elif operation.endswith("_2"):
        if not matrix2_input:
            context["alertmessage"] = True
            context["message"] = "Please check the provided inputs!"
            context["result"] = ""
            return render_template("ivbns.html", **context)

        func = unary_functions.get(operation)
        if not func:
            context["alertmessage"] = True
            context["message"] = "Please check the operation and provided inputs!"
            context["result"] = ""
            return render_template("ivbns.html", **context)

        result = func(matrix2)
    else:
        if not matrix2_input:
            context["alertmessage"] = True
            context["message"] = "Please check the provided inputs!"
            context["result"] = ""
            return render_template("ivbns.html", **context)
        func = binary_functions.get(operation)
        result = func(matrix1, matrix2)

    # Prepare the result for rendering
    context["result"] = str(result)
    context["change_color"] = True
    context["button_id"] = operation

    return render_template("ivbns.html", **context)

if __name__ == "__main__":
    app.run(debug=False)
