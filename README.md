# Air Gesture Gaming

Air Gesture Gaming is an innovative project that uses camera-based body detection to control a character in a game. Inspired by games like Subway Surfers, this project allows players to move their bodies to interact with the game, creating a fun and immersive experience.

## Features

- **Body Detection**: Uses a camera to detect player movements in real-time.
- **Gesture Controls**: Move left, right, jump, or crouch by performing corresponding body gestures.
- **Immersive Gameplay**: Control the character directly with your body, eliminating the need for traditional controllers.
- **Customizable Gestures**: Configure gestures to suit your preferences.

## How It Works

1. **Camera Input**: The system captures video input from a connected camera.
2. **Pose Detection**: AI-powered algorithms analyze the player's body position and movements.
3. **Game Interaction**: Detected gestures are mapped to in-game actions, such as dodging obstacles or collecting items.

## Requirements

- A computer with a webcam or external camera.
- Python 3.8 or higher.
- Required libraries: OpenCV, MediaPipe, and PyGame.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Air_Gesture_Gaming.git
    cd Air_Gesture_Gaming
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the game:
    ```bash
    python main.py
    ```

## Future Enhancements

- Add multiplayer support.
- Improve gesture recognition accuracy.
- Integrate with VR/AR devices for enhanced immersion.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by Subway Surfers.
- Built using OpenCV and MediaPipe for pose detection.

Enjoy gaming with your body as the controller!