# DependencyDongle
A Python Software Dongle based on Arduino


I have developed an open source, Arduino-based Software Security Dongle system. This can be used in your software to only allow users who have bought a dongle with the correct code running on it to use your software.

This code does require PySerial to be installed. To do this, type `pip install pyserial` into a command prompt.


Please note that there is no encryption and the validation algorithm is **very, very, very basic**. If you know how I can improve my code to encrypt the connection, please let me know.


## The validation algorithm

This validation algorithm is very basic. To validate, Python sends a request to the Arduino for `AuthKey`, which is a pre-defined 15 character string. As long as the `AuthKey` variable that Python gets back is exactly 15 characters and not on the blacklist, it goes on to the next step, which is simply verifying that the `GlobalKey` variable that is sent from the Arduino matches the `GlobalKey` that the Python script has. If anyone knows how to make a better algorithm, please share that with me.

## How to set it all up

To set this up, make sure PySerial is installed. PySerial is required for communication between Arduino and Python.

1. Download all of my code and extract it to *somewhere* on your computer.
2. Open the Python script and modify the AuthKey and GlobalKey variables to be what you want them to be. Make the same changes to the Arduino script.
3. Upload the Arduino code to the Arduino. Then, plug in the Arduino and run the Python script. Chances are that it will verify. If it throws an error immediately, go into the Python script and change your COM port. This will eventually happen automatically, but manually changing it will work for now.

And it's done! The Python script should say something like "Dongle Verified Successfully!" if it works.

You can then modify the code to fit your needs.

Have a nice day!
