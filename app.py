import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGridLayout,QPushButton
from PyQt5.QtGui import QPixmap,QGuiApplication
from PyQt5.QtCore import Qt
class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Viewer")
        screen_resolution = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen_resolution.width(), screen_resolution.height())
        

        # Create a label to hold the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Create a button to open the image file dialog
        self.open_image_button = QPushButton("Open Image", self)
        self.open_image_button.clicked.connect(self.open_image)

        # Create a layout to arrange the widgets
        layout = QGridLayout(self)
        layout.addWidget(self.image_label, 0, 0, 1, 2)
        layout.addWidget(self.open_image_button, 1, 0, 1, 2)

        self.setLayout(layout)

    def open_image(self):
        # Open a file dialog to select an image
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.jpg *.png *.jpeg)")

        if filename:
            # Load the image using QPixmap
            pixmap = QPixmap(filename)

            # Resize the pixmap to fit the label
            pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)

            # Set the pixmap to the image label
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
