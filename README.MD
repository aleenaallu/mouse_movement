workflow 

  

1. Import Libraries 

 You import the necessary libraries logging, mouse and keyboard from the pynput module. 

  

2. Configure Logging 

 You configure the logging to save the mouse activity in a file named mouse_activity.log. The logging.basicConfig function sets up the format and level of logging. 

  

3. Mouse Event Handlers 

   - on_move(x, y): This function is called whenever the mouse cursor is moved. It logs the cursor's new position in the log file. 

   - on_click(x, y, button, pressed): This function is called when a mouse button is clicked (pressed or released). It logs the button action (pressed or released) along with the button type (left, right, or unknown) and the cursor's position. 

   - on_scroll(x, y, dx, dy): This function is called when the mouse wheel is scrolled. It logs the scrolling action along with the cursor's position and the scroll amount (delta). 

  

4. Keyboard Event Handler 

   - on_key_release(key): This function is called when a key is released on the keyboard. If the released key is the Esc key, it stops the mouse listener using mouse_listener.stop() and returns `False` to stop the keyboard listener. 

  

5. Set Up Listeners 

   - You create instances of the mouse.Listener and keyboard.Listener classes, providing the respective event handlers (on_move, on_click, on_scroll, and on_key_release). 

  

6. Start Listeners 

   - You start both listeners using mouse_listener.start() and keyboard_listener.start() 

  

7. Join Listeners 

   - You use mouse_listener.join() and keyboard_listener.join() to keep the program running and waiting for the listeners to finish. 
