from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")
    else:
        transaction = {
            "id": len(transactions) + 1,
            "date": request.form['date'],
            "amount":float(request.form["amount"])
        }
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":
        for trans in transactions:
            if transaction_id == trans["id"]:
                return render_template("edit.html", transaction=trans)
        else:
            return {"message": "not found"}, 404
    else:
        for trans in transactions:
            if trans['id'] == transaction_id:
                trans['date'] = request.form['date']
                trans['amount'] = float(request.form['amount'])
                return redirect(url_for('get_transactions'))
        return {'message': "not found"}, 404

# Delete operation, using GET method to perform from browser
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for trans in transactions:
        if trans['id'] == transaction_id:
            transactions.remove(trans)
            return redirect(url_for("get_transactions"))
    else:
        return {"message": "note found"}, 404

#Search operation
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    if request.method == "POST":
        min = float(request.form['min_amount'])
        max = float(request.form['max_amount'])
        filtered_transactions = []
        for trans in transactions:
            amount = trans['amount']
            if amount >= min and amount <= max:
                filtered_transactions.append(trans)
        return render_template("transactions.html", transactions=filtered_transactions)
    else:
        return render_template("search.html")

#Total balance
@app.route("/balance")
def total_balance():
    return {"Total Balance": sum(item['amount'] for item in transactions)}
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)