# States Machne with Turtlebot Robot
The target of this exercise is to create a states machine. The behavior of the robot will be go forward untill it sees my hand.
When robot sees my hand, it will go backward and then, it will turn. So, we have three states:

* *Go Forward*
* *Go Backward*
* *Turning*

## rogram Esplanation:
This robot is programmed following an iterative structure, so it have an infinite loop like that:
```
while(True):
  #statements
```
Inside the loop, different conditions are evaluated. Each condition will cause that current state changes. On this wqay, our structur will be like that:

```
while(True):
  #statements
  evaluateConditions()
  runState()
```

where *evaluateConditions()* takes care of change the current state if it is necessary, and *runState()* have to run the correct 
code depending of the current state.

## Visual Example:
[Here](https://www.youtube.com/watch?v=osfcSLC7BQg) you can find a video where the robot behavior is shown.
