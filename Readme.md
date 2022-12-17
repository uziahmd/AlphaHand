#AlphaHAnd
This is the final project for the Basics of AI class - COE202.

##Details And Explanation 
AlphaHand - Rock Paper Scissors playing robot.

An AI backed image recognition existence that works with the help of media pipe that tracks the 21 landmarks in the on the players hand and also calculates the angles and distances between the points and the fingers to recognize the form that the user’s hand has taken and recognize accordingly the user's choice.

The AI opposes the player using a randomly chosen strike of his own that and acts upon it with the help of the MODI motors that move the 3D printed hand using tensile fishing wires. The hand is installed with a steal wire that provides the hand with tension that in turn helps it in getting back to its original upright position when the motors release it.

![AlphaHand](Resources/Pic1.png?raw=true "AlphaHand")

##Hardware Requirenments
We required a set of electronic modules provided by MODI LUXOROBO (Network Module, Motors, Display Modules), A set of Lego pieces to provide support and structure to the modules and a 3D printed hand parts, steel wires, and fishing wires.

![HardWare Image](Resources/Hardware_req.png?raw=true "Harwware_req")

##Install all the dependencies

```bash
conda env create -f environment.yml
```

##Refrences

MODI - Python API for controlling modular electronics, MODI. (https://github.com/LUXROBO/pymodi) 

MediaPipe - Python API for hand land mark detection. It is a cross-platform, customizable ML solutions for live and streaming media. (https://github.com/google/mediapipe)

The CAD Design - https://www.thingiverse.com/thing:1691704

OpenCV - https://github.com/opencv/opencv

