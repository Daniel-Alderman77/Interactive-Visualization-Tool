from PySide.QtCore import Qt
from PySide.QtGui import QGroupBox, QFont, QLabel, QVBoxLayout, QHBoxLayout


class MemoryWindow:
    def __init__(self):
        self.name = self

    # Create a QGroupBox component to act as the window

    window = QGroupBox()
    window.setWindowTitle("Memory Window")

    # Create and configure widgets

    total_label = QLabel()
    total_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
    total_label.setAlignment(Qt.AlignCenter)
    total_label.setText("Total Utilisation")

    distribution_label = QLabel()
    distribution_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
    distribution_label.setAlignment(Qt.AlignCenter)
    distribution_label.setText("Distribution by Job")

    latency_label = QLabel()
    latency_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
    latency_label.setAlignment(Qt.AlignCenter)
    latency_label.setText("Latency")

    # Top Layout

    top_layout = QHBoxLayout()

    top_left_layout = QVBoxLayout()
    top_left_layout.addWidget(total_label)

    top_right_layout = QVBoxLayout()
    top_right_layout.addWidget(distribution_label)

    top_layout.addLayout(top_left_layout)
    top_layout.addLayout(top_right_layout)

    # Bottom layout

    bottom_layout = QVBoxLayout()
    bottom_layout.addWidget(latency_label)

    # Stack layouts on top of each other

    window_layout = QVBoxLayout()
    window_layout.addLayout(top_layout)
    window_layout.addLayout(bottom_layout)

    window.setLayout(window_layout)

    # Make window visible

    window.show()
