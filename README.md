
#Producer-Consumer pattern

By creating experiment with different amount of consumers and producers i estimated exact amount to have most items consumed per unit of time. In experiment i used amounts from 1 to 10 of producers and consumers and made combinations. 

Each combination i let run for 10 cycles and averaged amounts of produced and consumed.
 
For consumed I put all averages of consumed items on plot and was looking for maximum. 
![alt text](https://github.com/xkupkovic/ppds/blob/03/produced.png?raw=true)

For produced I put all  averages of produced items on plot and was also looking of maximum. I found that most produced happen to be when most threads are on producing task but in next experiment I increased time loop time and number of produced items fell from maximum.
![alt text](https://github.com/xkupkovic/ppds/blob/03/consumed.png?raw=true)