# from flask import Flask, jsonify, make_response, request, 
from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)

@app.route("/")
def index():
	return "hello world"

@app.route("/no_content")
def no_content():
	return jsonify({"message": "No content found."}), 204

@app.route("/exp")
def index_explicit():
	msg = {"massage": "Hello World"}
	code = 200
	resp = make_response(msg,code)
	return resp

@app.route('/name_search')
def search_name():
	first_name = request.args.get("q")
	try:
		if first_name is not None:
			for item in data:
				if item["first_name"].lower() == first_name.lower():
					return item, 200
			return {"message": "not found"}, 404
	except:
		return {"message": "something went wrong"}, 500
	
@app.route("/count")
def count():
	try:
		return {"len": len(data)}
	except:
		return {"message": "server error"}, 500

#proplem!!
@app.route("/person/<uuid>")
def get_person(uuid):
	try:
		for person in data:
			if person["id"] == uuid:
				resp = make_response(person['first_name'])
				return resp
		return {"message": "not found"}, 404
	except:
		return {"message": "server error"}, 500

@app.route('/data')
def get_data():
	try:
		if data and len(data) > 0:
			return {"massage": "data found"}
		else:
			return {"massage": "data is empty"}, 500
	except:
		return {f"massage": "data not found"}, 404


@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
	for person in data:
		if person["id"] == str(id):
			data.remove(person)
			return {"message": "Deleted"}, 200
		pass
	else:
		return {"msg": "not found"}, 404
	
@app.route('/person', methods=['POST'])
def add_by_uuid():
    try:
        person = request.get_json()
        if not person:
            return {"message": "Invalid input"}
        data.append(person)
        return person, 202
    except:
            return {"message": "server error"}, 500

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "somthing went wrong"}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500

@app.route("/test_abort/<num>")
def test_abort(num):
    if int(num) == 4:
        abort(500, description="Error")
    return {"message": f"{num} work correctly"}, 200
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

if __name__ == "__main__":
	app.run(debug=True)
