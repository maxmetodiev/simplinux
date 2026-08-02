import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import os

class TimeRecorder(QWidget):
    def __init__(self):
        super().__init__()
        self.elapsed_time = 0
        self.is_running = False
        self.init_ui()
        
    def init_ui(self):
        # Create main layout
        layout = QVBoxLayout()
        
        # Create time display label
        self.time_label = QLabel('00:00:00')
        self.time_label.setFont(QFont('Arial', 48, QFont.Bold))
        self.time_label.setAlignment(Qt.AlignCenter)
        
        # Create start/stop button
        self.button = QPushButton('Start')
        self.button.setFont(QFont('Arial', 14))
        self.button.clicked.connect(self.toggle_timer)

        # Create clear button
        self.clear_button = QPushButton('Clear')
        self.clear_button.setFont(QFont('Arial', 14))
        self.clear_button.clicked.connect(self.clear_time)
        
        # Create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        
        # Add widgets to layout
        layout.addStretch()
        layout.addWidget(self.time_label)
        layout.addSpacing(20)
        layout.addWidget(self.button)
        layout.addStretch()
        layout.addWidget(self.clear_button)
        layout.addStretch()

        
        # Set layout and window properties
        self.setLayout(layout)
        self.setWindowTitle('Time Recorder')
        self.setGeometry(100, 100, 400, 300)
        
    def toggle_timer(self):
        if self.is_running:
            # Stop the timer
            self.timer.stop()
            self.is_running = False
            self.button.setText('Start')
        else:
            # Start the timer
            self.timer.start(100)  # Update every 100ms
            self.is_running = True
            self.button.setText('Stop')
    
    def update_time(self):
        self.elapsed_time += 0.1
        
        # Convert to hours, minutes, seconds
        total_seconds = int(self.elapsed_time)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        milliseconds = int((self.elapsed_time - total_seconds) * 10)
        
        # Format and display
        time_str = f'{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:01d}'
        self.time_label.setText(time_str)
    
    def clear_time(self):
        self.elapsed_time = 0
        self.time_label.setText('00:00:00.0')

    def closeEvent(self, event):
        # Stop timer when closing
        if self.is_running:
            self.timer.stop()
        self.save_time()  # Call save_time when closing
        event.accept()


    def save_time(self):
        # Save the elapsed time to a file
        save_path = os.path.join(os.path.dirname(__file__), 'elapsed_time.txt')
        with open(save_path, 'w') as f:
            f.write(f'Elapsed Time: {self.time_label.text()}\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = TimeRecorder()
    recorder.show()
    sys.exit(app.exec_())
