#!bin/sh
#! usr/bin/python3
while((1));
do
	echo "Please choose the mode you want to use."
	echo "Key in 'm' to turn to manual mode."
	echo "Key in 'a' to turn on auto mode."
	echo "Key in 'e' to exit."
	read key
	if [ $key = m ];then
		echo "You are going to manual mode."
		echo "Please select the channal you wnat to connect after connection to start control."
		sleep 2
		python3 ./miniterm.py
		echo "Do you want to exit? y/n ..."
		read input
		if [ $input = n ];then
			continue
		elif [ $input = y ];then
			exit
		fi	
	elif [ $key = a ];then
		echo "You are going to automatic color identify mode."
		sleep 2
		while((1));
		do
			python3 ./main.py
			python3 ./port2arduino.py
			echo "Do you satisfied with the answer?"
			echo "Key in 'n' to restart."
			echo "Key in 'y' yo exit."
			echo "Key in 'm' to go into manual mode."
			read reply
			if [ $reply = n ];then
                        	sleep 1.5
			elif [ $reply = y ];then
				break
			elif [ $reply = m ];then
				echo "You are going to manual mode."
               			echo "Please input 1 after connection to start control."
                		sleep 2
                		python3 ./miniterm.py
                		echo "Do you want to exit? y/n ..."
                		read input
                		if [ $input = n ];then
                        		continue
                		elif [ $input = y ];then
                        		exit
				fi
			fi		
		done
		exit
	elif [ $key = e ];then
		echo "Good bye!"
		sleep 1.5
		exit
	else
		echo"Invalid input!"
	fi
done	
