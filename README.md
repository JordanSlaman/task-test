# task-test

This is an entry test for potential developers that apply to CCN / 2M. 
It is for us to better understand your current skill level.

You can either do the Python version or the C++ version

When doing this test, please fork our repository and then send us a link to branch in your forked repository with your solution. Name of the branch should be your last name.

Good luck!

We are looking forward to see your solution.

---

# Jordan's Solution

I have chosen to work on the Python implementation.

## ID's
I've decided that it would be best to store the tasks as a dict, as it would make it much easier to track reference them by ID than by array position. In this implementation a task would not need to know it's ID, which I feel believe makes for better encapsulation - Unfortunately it results in overwriting all of the methods in the original Task Manager.

It's possible that multiple tasks would be created with the same name, so in order to avoid collisions I assigned the keys by hashing both the name and the timestamp of creation concatenated. Theoretically there could still be collisions, but that can be fixed/optimized with some error checking code, a larger hash digest and/or a finer time granularity.

Scheduling/Ordering of tasks was not addressed, but that could be done by prioritizing the created timestamp, or inserting them in a different processing queue as they are allocated/preformed.

### Finding Keys
The lookup\_tasks(name) function returns a subset of the tasks dict with matching names, alternatively if you are iterating over/operating on a task somewhere you could re-compute it with generate\_key(task).

### Scaling
The task manager could be theoretically be scaled to thousands of application servers operating on tasks stored in a redis cluster for high availibility. Performance bottlenecks could be addressed as they appear.

I haven't done comparisons of the algorithmic complexity of my changes.

I chose not to modify the 'task_manager.py' file at all in order to respect the 'external library' concept - so all the original bugs are included.