import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QGroupBox, QFont, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication(sys.argv)

# Create a QGroupBox component to act as the window

window = QGroupBox()
window.setWindowTitle("Main Window")

# Create and configure widgets

cpuLabel = QLabel()
cpuLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
cpuLabel.setAlignment(Qt.AlignCenter)
cpuLabel.setText("CPU Utilisation")

memoryLabel = QLabel()
memoryLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
memoryLabel.setAlignment(Qt.AlignCenter)
memoryLabel.setText("Memory Utilisation")

jobsLabel = QLabel()
jobsLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
jobsLabel.setAlignment(Qt.AlignCenter)
jobsLabel.setText("Current Jobs")

hierarchyLabel = QLabel()
hierarchyLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
hierarchyLabel.setAlignment(Qt.AlignCenter)
hierarchyLabel.setText("Hierarchy View")

latencyLabel = QLabel()
latencyLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
latencyLabel.setAlignment(Qt.AlignCenter)
latencyLabel.setText("Latency")

# Top Layout

topLayout = QHBoxLayout()

topLeftLayout = QVBoxLayout()
topLeftLayout.addWidget(cpuLabel)

topRightLayout = QVBoxLayout()
topRightLayout.addWidget(memoryLabel)

topLayout.addLayout(topLeftLayout)
topLayout.addLayout(topRightLayout)

# Middle Layout

middleLayout = QHBoxLayout()

middleLeftLayout = QVBoxLayout()
middleLeftLayout.addWidget(jobsLabel)

middleRightLayout = QVBoxLayout()
middleRightLayout.addWidget(hierarchyLabel)

middleLayout.addLayout(middleLeftLayout)
middleLayout.addLayout(middleRightLayout)

# Bottom layout

bottomLayout = QVBoxLayout()
bottomLayout.addWidget(latencyLabel)

# Stack layouts on top of each other

windowLayout = QVBoxLayout()
windowLayout.addLayout(topLayout);
windowLayout.addLayout(middleLayout);
windowLayout.addLayout(bottomLayout);

window.setLayout(windowLayout)

# Make window visible

window.show()

sys.exit(app.exec_())