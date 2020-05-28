# ATH10K-Timeline application

#### *Application for Debugging Ath10k driver in a convenient manner.*
_This application was made for a compeition conducted by Qualcomm, in which our team secured the **1st Position**._

The GUI for the application is made using `tkinter`, and supports all the required functionality.

###### The problem statement given was this:<br>
_The ATH10K driver in the Qualcomm *QCA9888* chipset provides debug log output during various actions and events. Since extensive logging can get chaotic and reduces readability in a developer environment, we had to hack together an application that would parse the debug log output from the chipset and make it more readable and navigable. The application needs to provide a timeline for various actions, events, warnings and error. We were to also parse the hexadecimal flags that the chipset produces in order to understand variable they pertain to._

###### We created the following application:
![GUI](/other/screenshots/img.png)

The application provides various events occuring in the chipset in a chronological fashion. The events are grouped together by the `Station Addresses (STAs)`.

`Fetch` - It fetches the most recent logs from the router containing the chipset using the open source framework **openwrt**.<br>
`Display` - Parses and displays the events for a particular STA.<br>
`Delete` - Clears the display. <br>
`Quit` - I guess it's self-explanatory (:D), but well, it quits the application.

_Note: In order to be able to access these logs, we installed an opensource framework called **openwrt** onto the routers firmware and configured it accordingly for our use._
