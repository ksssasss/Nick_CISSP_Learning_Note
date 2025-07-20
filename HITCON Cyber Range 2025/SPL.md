
```
index=* sourcetype=*
| eval Time = strftime(_time, "%Y-%m-%d %H:%M:%S")
| rename 
    src_addr AS "Source IP", 
    dst_addr AS "Destination IP",
    dst_port AS "Destination Port",
    msg AS "Event Name",
    action AS "Action",
    class AS "Category",
    _raw AS "Raw Data",
| table _time, "Source IP", "Destination IP", "Destination Port", "Action", "Event Name", Category, "Raw Data"
```

