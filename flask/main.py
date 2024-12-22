from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

# Flask application setup
app = Flask(__name__, static_folder='static')  # Serve "static" folder for frontend files
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///potholes.db'
app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# Ensure required folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.static_folder, exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Pothole model
class Pothole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)



# Contractor model
class Contractor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    expertise = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    availability = db.Column(db.Boolean, default=True)



# Create database tables
with app.app_context():
    db.create_all()
    # Populate the Contractor table (only needed once)
    if not Contractor.query.first():
        contractors = [
            Contractor(name="Alice Smith", contact="1234567890", expertise="Road Repairs", rating=4.5),
            Contractor(name="Bob Johnson", contact="0987654321", expertise="Waste Management", rating=4.2),
            Contractor(name="Charlie Brown", contact="1122334455", expertise="Street Lighting", rating=4.8),
        ]
        db.session.bulk_save_objects(contractors)
        db.session.commit()

# API to report a pothole
@app.route('/reportPothole', methods=['POST'])
def report_pothole():
    title = request.form.get('title')
    description = request.form.get('description')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    image_file = request.files.get('image')

    if not (title and description and latitude and longitude and image_file):
        return jsonify({"error": "All fields are required"}), 400

    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
    image_file.save(image_path)

    # Save data to database
    pothole = Pothole(
        title=title,
        description=description,
        latitude=float(latitude),
        longitude=float(longitude),
        image=image_file.filename
    )
    db.session.add(pothole)
    db.session.commit()

    return jsonify({"message": "Pothole reported successfully!"}), 201

# API to fetch potholes based on latitude and longitude
@app.route('/potholes', methods=['POST'])
def get_potholes():
    data = request.get_json()
    latitude = float(data.get('latitude'))
    longitude = float(data.get('longitude'))

    if latitude is None or longitude is None:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    # Fetch potholes within proximity
    potholes = Pothole.query.filter(
        func.abs(Pothole.latitude - latitude) < 0.1,
        func.abs(Pothole.longitude - longitude) < 0.1
    ).all()

    results = [
        {
            "title": pothole.title,
            "description": pothole.description,
            "location": f"{pothole.latitude}, {pothole.longitude}",
            "image": f"/uploads/{pothole.image}"  # Construct full path for the image
        }
        for pothole in potholes
    ]

    return jsonify({"potholes": results}), 200

# API to fetch contractor data
@app.route('/contractors', methods=['GET'])
def get_contractors():
    contractors = Contractor.query.all()
    results = [
        {
            "name": contractor.name,
            "contact": contractor.contact,
            "expertise": contractor.expertise,
            "rating": contractor.rating,
            "availability": contractor.availability,
        }
        for contractor in contractors
    ]
    return jsonify(results), 200

# Serve uploaded images
@app.route('/uploads/<filename>')
def serve_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Serve static files as root
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    if path == "" or not os.path.exists(os.path.join(app.static_folder, path)):
        path = 'home.html'  # Default to index.html for root
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
