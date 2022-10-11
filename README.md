# Studio Command API Examples
Example code of interfacing with the Rokoko Studio Command API

Rokoko Studio Beta offers an API that allows you to operate a running application through a range of commands.

At the moment, the following commands are available - for any of them to work, you need to have a scene open:

* Start/stop recording
* Calibrate
* Reset actor
* Get scene info
* Attach tracker

## Setup and sending commands
In order to send commands to and receive messages from Studio, the following values will need to be defined:

* **IP address** (of the computer running Rokoko Studio that you want to interface with)
* **Port** (the port value defined in Rokoko Studio settings; defaults to 14053. This needs to be changed if this port is blocked or used by another application)
* **API key** (the API key defined in Rokoko Studio settings; defaults to 1234)
The command is then sent as a http request in the following format:

http://"IP address":"Port"/v1/"API key"/"command name"

for example

http://127.0.0.1:14053/v1/1234/recording/start

## Commands
### Start/Stop Recording
Used to start and stop a recording

Command: **recording/start** or **recording/stop**

Parameters:
* filename: The name of the clip you want to record (optional)
* time: Timecode to be used for the clip you want to record (optional)
* frame_rate: Defined framerate for the clip you want to record (optional)
* back_to_live: Set to true if you want to stay in "live view" after ending a recording (optional)
 
### Calibrate
Calibrates all paired live input devices in the scene or for the specified actor

Command: **calibrate**

Parameters:
* device_id: The name/id of the input device, e.g. a Smartsuit Pro, that you want to calibrate (optional)
If no value is given, all live devices in the scene will be calibrated
* countdown_delay: The countdown in seconds before the actual calibration happens (optional)
* skip_suit: If set to true, a paired Smartsuit Pro to the targeted actor will be skipped during calibration (optional)
* skip_gloves: If set to true, paired Smartgloves to the targeted actor will be skipped during calibration (optional)
* use_custom_pose: If set to true, a custom calibration pose can be used, as defined below (optional)
* pose: (optional)

Values for the pose argument could be the following:
* straight-arms-down
* straight-arms-forward
* tpose (default one)

### Reset Actor
Resets the actor pose and local position

Command: **resetactor**

Parameters:
* device_id: The name/id of the input device, e.g. a Smartsuit Pro, that is attached to the actor you want to reset

### Scene Info
Returns information about the current open scene

Command: **info**

Parameters:
* devices_info: Set to true if you want information about live input devices in the scene
* clips_info: Set to true if you want information about the recorded clips in the scene

### Attach Tracker
Attaches an external tracker, e.g. a HTC Vive Tracker, to an actor, which can then determine its global position.

Command: **tracker**

Parameters:
* device_id: The name/id of the input device, e.g. a Smartsuit Pro, that is attached to the actor you want to attach the tracker to
* bone_attached: The bone that the tracker should be attached to. Defaults to "Hips"
* position: Position of the tracker being attached
{'X': <value>, 'Y': <value>, 'Z': <value>}
* rotation: Rotation of the tracker being attached
{'X': <value>, 'Y': <value>, 'Z': <value>, 'W': <value>}
* timeout: Time in seconds until the attached tracker releases the attached object (optional)
* is_query_only: Use the command to only query a specified bone position and orientation rather than attaching the actual tracker and take control of the bone (optional)

## Python Examples

 In order to run python examples you have to use Python 3.3+ interpreter and you have to install **requests** library - https://pypi.org/project/requests/

## Web Page Example

 This is an example of a drift control for the actor. The example is a html web page with java script code.
 The grid on a page shows the ground plane, while a ball represents an actor. 
 
 When you click on a canvas and hold the mouse button, you take control over the actor by sending tracker commands
 When you release the mouse button but keep your mouse in the canvas area, the tracker command continue working in the query mode
 and you will see a yellow trajectory of the actor moving along the ground plane.

