# digipray
A digital prayer wheel developed almost entirely by the ChatGPT (with tedious work on my part trying to communicate with it), inspired by Intention Repeater.  Production time was around 12 hours.

The program repeats a mantra (string) of your choice in computer memory. It determines the maximum repetition rate per second based on available memory. A custom target repetition rate can be chosen or the estimated maximum. The actual repetition rate in memory is then displayed. The intent of the software is to implement a digital prayer wheel according to modern principles of technology, as Dalai Lama had allegedly said a hard drive that spins the mantra is effective (but HDDs are rarely used anymore). It is not so different from wind- and water-powered prayer wheels. So, this can be useful to Buddhists to let the computer pray for you automatically. I use the mantra OM MANI PADME HUM. It is written in Python.

The prerequisites.txt shows you need psutil.  You can run "pip install psutil" to get the latest version, or if that does not work, "pip install -r requirements.txt" to get the version the program was built on.
