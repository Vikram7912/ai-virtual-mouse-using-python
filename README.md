# ai-virtual-mouse-using-python

## Overview
This project demonstrates a computer mouse controlled using hand gestures, offering a touch-free interaction mechanism. The solution leverages OpenCV, MediaPipe, and Python to detect and interpret hand movements and gestures to emulate mouse functions such as cursor movement, left click, right click, and more.

## Features
- **Hand Tracking**: Real-time detection and tracking of hands using MediaPipe.
- **Gesture Recognition**: Identification of gestures for performing mouse operations like:
  - Cursor movement
  - Left click
  - Right click
  - Scroll
- **Touch-Free Interaction**: Enhances accessibility and reduces dependency on physical devices.
- **Efficient and Lightweight**: Optimized for smooth performance on various hardware setups.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - OpenCV: For image processing and camera integration
  - MediaPipe: For robust hand tracking and gesture recognition
  - PyAutoGUI: To control mouse operations programmatically

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/virtual-mouse.git
   cd virtual-mouse
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python virtual_mouse.py
   ```

## How It Works
1. The camera captures a live video stream.
2. MediaPipe detects the hand landmarks in the video frames.
3. Predefined gestures are mapped to specific mouse actions using PyAutoGUI.
4. The corresponding mouse operation is performed in real-time.

## Demo
Here is a preview of the project in action:
*(Include a GIF or link to a demonstration video)*

## File Structure
```
virtual-mouse/
├── virtual_mouse.py       # Main program file
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── demo/                  # Demo assets (images/videos)
```

## Future Enhancements
- Incorporate additional gestures for advanced controls.
- Optimize performance for low-spec hardware.
- Add multi-hand tracking capabilities.
- Integrate voice commands for hybrid control.

## Acknowledgments
- **OpenCV** for providing powerful computer vision tools.
- **MediaPipe** for its comprehensive hand tracking solution.
- **PyAutoGUI** for easy and flexible mouse control.

## Contact
For any queries or suggestions, feel free to reach out:
- **Name**: Vikram
- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [yourusername](https://github.com/yourusername)

---

Feel free to fork, star, and contribute to this project!
