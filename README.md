# First-GitHub-Project
For this project, I built an Airport class that will allow me to record the planes that want to land and takeoff with a queue. 
The way that I did this is that I took two lists, which are my takeoff_queue and my landing_queue. These queues are responsible for recording and tracking the waitlist for planes that want to take off and land.
In the simulation function, I have defined a for loop that iterates over 120 time steps. In each time step, a random number between 0 and 3 is assigned to the number of takeoff and landings.
For each landing and takeoff, a new plane object is created and is either given the name "American Airlines or "United Airlines" based on wether the plane is landing or taking off.
The code now iterates to see if a runway is available, if it is available then it calls the clear to land in one runway and calls clear to takeoff in another runway. It then prints all the results from the 120 time steps
