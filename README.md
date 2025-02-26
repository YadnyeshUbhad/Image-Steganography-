🖼️ Image Steganography Web App 🔒


📌 Overview

This project implements Image Steganography, allowing users to hide secret messages inside images securely. It provides a web-based interface built with Flask, OpenCV, and JavaScript for encrypting and decrypting messages from images.


Steganography is a method of concealing secret information inside multimedia files like images, making communication undetectable. This project ensures secure and private message transmission using a password-protected encoding system.



✨ Features

✅ Encrypt Messages: Hide a text message inside an image securely.

✅ Decrypt Messages: Extract hidden messages using the correct password.

✅ User-Friendly UI: A simple web interface to perform encryption & decryption.

✅ Password Protection: Ensures only authorized users can decrypt the message.

✅ Secure Communication: Messages are embedded without noticeable changes to the image.

✅ Lightweight & Fast: Works efficiently with minimal system requirements.



🛠️ Technologies Used

Backend

Python

Flask (Microframework for handling API requests)

OpenCV (For image processing)

NumPy (For numerical computations)

Werkzeug (For file handling)


Frontend

HTML, CSS, JavaScript (For web interface)

Fetch API (To communicate with Flask backend)




🚀 Installation & Setup

Follow these steps to set up and run the project:


1️⃣ Clone the Repository


git clone https://github.com/YadnyeshUbhad/image-steganography.git
cd image-steganography


2️⃣ Create a Virtual Environment (Optional but Recommended)


python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows


3️⃣ Install Required Dependencies


pip install flask opencv-python numpy werkzeug


4️⃣ Run the Flask Application


python app.py


5️⃣ Open the Web App

Visit http://127.0.0.1:5000/ in your browser.



🖥️ How to Use the Web App


🔹 Encryption (Hiding a Message in an Image)
Upload an image (.png, .jpg, etc.).
Enter the secret message you want to hide.
Provide a password for extra security.
Click "Encrypt" and download the encrypted image.


🔹 Decryption (Extracting a Message from an Image)
Upload the previously encrypted image.
Enter the correct password.
Click "Decrypt" to reveal the hidden message.


📸 Screenshots


🔹 Encryption Page



🔹 Decryption Page

![image](https://github.com/user-attachments/assets/c233baea-64a2-44bb-8a87-e1c003488ded)




🔐 Security Features

Uses steganography techniques to embed messages securely.

Only password-matching decryption reveals the hidden message.

Stores messages inside the blue color channel of image pixels, making them invisible to the naked eye.

🛠️ Project Structure



/image-steganography

│── /uploads              # Folder for uploaded images

│── /output               # Folder for encrypted images

│── /templates

│    ├── index.html       # Frontend UI

│── app.py                # Flask backend

│── README.md             # Project Documentation

│── requirements.txt      # Python dependencies


📌 Contributing

Want to improve this project? Follow these steps:


Fork the repository

Create a new feature branch

git checkout -b feature-branch
Commit your changes



git commit -m "Added a new feature"
Push to GitHub



git push origin feature-branch


Create a Pull Request 🚀


📄 License

This project is licensed under the MIT License. Feel free to modify and distribute it.

