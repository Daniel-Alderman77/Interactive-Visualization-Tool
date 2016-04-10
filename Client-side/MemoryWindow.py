import sys
from PySide.QtCore import Qt
from PySide.QtGui import QGroupBox, QFont, QLabel, QVBoxLayout, QHBoxLayout

class MemoryWindow():

    # Create a QGroupBox component to act as the window

    window = QGroupBox()
    window.setWindowTitle("Memory Window")

    # Create and configure widgets

    totalLabel = QLabel()
    totalLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
    totalLabel.setAlignment(Qt.AlignCenter)
    totalLabel.setText("Total Utilisation")

    distributionLabel = QLabel()
    distributionLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
    distributionLabel.setAlignment(Qt.AlignCenter)
    distributionLabel.setText("Distribution by Job")

    latencyLabel = QLabel()
    latencyLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
    latencyLabel.setAlignment(Qt.AlignCenter)
    latencyLabel.setText("Latency")

    # Top Layout

    topLayout = QHBoxLayout()

    topLeftLayout = QVBoxLayout()
    topLeftLayout.addWidget(totalLabel)

    topRightLayout = QVBoxLayout()
    topRightLayout.addWidget(distributionLabel)

    topLayout.addLayout(topLeftLayout)
    topLayout.addLayout(topRightLayout)

    # Bottom layout

    bottomLayout = QVBoxLayout()
    bottomLayout.addWidget(latencyLabel)

    # Stack layouts on top of each other

    windowLayout = QVBoxLayout()
    windowLayout.addLayout(topLayout)
    windowLayout.addLayout(bottomLayout)

    window.setLayout(windowLayout)

    # Make window visible

    window.show()