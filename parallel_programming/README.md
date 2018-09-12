# Parallel Programming

Modern computers are now manufactured with CPUs that have multiple cores. This has become a standard of in computer architecture design, which previously was only seen in super computers. 

In this repo we will look at ways of making use of our computer power to perform tasks in parallel to obtain results in a shorter period as compared to performing them in series. Python has a built-in thread-safe mechanism, the Global Interpreter Lock (GIL), that prevents thread conflicts by executing takes one at a time.

We use the `multiprocessing` module to demonstrate how we can carry out parallel programming in Python and analyse large datasets using it.