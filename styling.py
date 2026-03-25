STYLE_DARK ="""
QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-family: "Segoe UI", sans-serif;
    font-size: 64px;
}

QPushButton {
    background-color: #333333;
    border: 1px solid #444444;
    border-radius: 5px;
    padding: 8px 15px;
}

QPushButton:hover {
    background-color: #454545;
    border: 1px solid #00ADB5; /* Color de acento */
}

QPushButton:pressed {
    background-color: #222222;
}

QLineEdit {
    background-color: #1E1E1E;
    border: 2px solid #333333;
    border-radius: 4px;
    padding: 5px;
    color: white;
}

QLineEdit:focus {
    border: 2px solid #00ADB5;
}
"""

STYLE_SKY="""
QMainWindow {
    background-color: #F5F7FA;
}

QFrame#container {
    background-color: white;
    border-radius: 10px;
}

QPushButton {
    background-color: #4A90E2;
    color: white;
    font-weight: bold;
    border-radius: 20px; /* Botones redondeados */
    padding: 10px;
}

QPushButton:hover {
    background-color: #357ABD;
}

QLabel {
    color: #333333;
}

QProgressBar {
    border: 1px solid #D1D1D1;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #4A90E2;
}

"""