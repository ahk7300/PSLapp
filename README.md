# PSLapp
Developed a web app for real-time recognition of Pakistani Sign Language (PSL) using deep learning. Achieved 99.8% accuracy for static gestures and 100% for dynamic gestures via lightweight neural networks and MediaPipe. The app enhances communication and education for Pakistan's 10M hearing-impaired citizens. Deployed with Flask.
[1-s2.0-S0952197624009199-main.pdf](https://github.com/user-attachments/files/18174362/1-s2.0-S0952197624009199-main.pdf)


# Real-Time Pakistani Sign Language Recognition

This project is a **web application** designed for real-time recognition of Pakistani Sign Language (PSL), enabling effective communication and education for Pakistan's 10 million hearing-impaired citizens. It uses advanced deep learning techniques and the MediaPipe library to achieve high accuracy in both static and dynamic gesture recognition.

---

## Features
- **Real-Time Gesture Recognition:** Supports all 39 PSL gestures (36 static + 3 dynamic).
- **High Accuracy:** Achieved 99.8% accuracy for static gestures and 100% for dynamic gestures.
- **Lightweight Design:** Optimized for deployment on desktop and mobile devices.
- **Interactive UI:** Built with CSS, HTML, and JavaScript using Flask as the backend framework.

---

## Technology Stack
- **Backend:** Python, TensorFlow, MediaPipe, OpenCV, Flask
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Dataset:** PSL gestures (5120 images for static signs, 353 videos for dynamic signs)
- **Models:** 
  - Static Gesture Model: Dense Neural Network
  - Dynamic Gesture Model: LSTM-based Neural Network

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/psl-recognition.git
   cd psl-recognition
```
2.Set up a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3.Install dependencies:
  ```bash
  pip install -r requirements.txt
```
4.Run the application:
  ```bash
  flask run
```
   ## Usage
1. Access the app via your browser at `http://127.0.0.1:5000`.
2. Select the type of gesture (static or dynamic).
3. Perform gestures in front of your camera.
4. The application predicts and displays the recognized PSL letter in real time.

---

## Dataset
- **Collected from native PSL signers**, ensuring diversity in age, gender, and race.
  - **Static Data:** Hand landmarks extracted from images.
  - **Dynamic Data:** Hand landmarks extracted from videos.

---

## Results
### Static Model:
- **Training Accuracy:** 85.14%  
- **Testing Accuracy:** 99.8%  

### Dynamic Model:
- **Training Accuracy:** 89.47%  
- **Testing Accuracy:** 100%

---

## Future Work
- Extend recognition to PSL sentences and numbers.
- Expand support for other sign languages.
- Optimize for deployment on embedded devices.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Contributors
- **Amenah Abdul Mujeeb**  
- **Ali Haider Khan**  
- **Sindhu Khalid**  
- **Muhammad Shaheer Mirza**  
- **Saad Jawaid Khan**

For any questions or contributions, feel free to open an issue or contact us via email.

---

## Acknowledgments
This project was developed to address the communication challenges faced by the hearing-impaired community in Pakistan, ensuring inclusivity and accessibility for all.
