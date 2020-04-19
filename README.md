redis clone built on python3

To run the server:
    python server.py
  
To connect:
    telnet localhost 9000

    # sample input/output
    SET ku 2
    OK
    GET ku
    2
    DEL ku
    OK
    GET ku
    NULL
    ZADD ku a 1 b 2 c 3
    OK
    ZRANGE ku 0 2 
    ['a', 'b']
    ZRANK ku b
    2  
  
  
