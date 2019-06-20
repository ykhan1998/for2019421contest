#include <Servo.h> 
Servo myservo;  //创建一个舵机控制对象
int servoData;
int motor1=7;   //继电器I1 左履带↑
int motor2=8;   //继电器I2 左履带↓
int motor3=12;  //继电器I3 右履带↑
int motor4=5;  //继电器I4 右履带↓

char var; //手动模式使用
int fromPos;
int toPos;

void right()//右转
{ //stoprun();
  //delay(150);
  digitalWrite(motor1,HIGH);
  digitalWrite(motor2,LOW);
  digitalWrite(motor3,LOW);
  digitalWrite(motor4,HIGH);
  
}
void left()//左转
{ //stoprun(); 
  //delay(150);
  digitalWrite(motor1,LOW);
  digitalWrite(motor2,HIGH);
  digitalWrite(motor3,HIGH);
  digitalWrite(motor4,LOW);
}
void back()//后退
{ //stoprun();
  //delay(150);
  digitalWrite(motor1,LOW);
  digitalWrite(motor2,HIGH);                                                                                                                                                                                                                                                                                                            
  digitalWrite(motor3,LOW);
  digitalWrite(motor4,HIGH);
}
void forward()//前进
{ //stoprun();
  //delay(150);
  digitalWrite(motor1,HIGH);
  digitalWrite(motor2,LOW);
  digitalWrite(motor3,HIGH);
  digitalWrite(motor4,LOW);
}
void stoprun()//停止！
{ //delay(500); 
  digitalWrite(motor1,LOW);
  digitalWrite(motor2,LOW);
  digitalWrite(motor3,LOW);
  digitalWrite(motor4,LOW);
}


void setup() 
{
  pinMode(motor1,OUTPUT);//引脚输出设置
  pinMode(motor2,OUTPUT);
  pinMode(motor3,OUTPUT);
  pinMode(motor4,OUTPUT);
  myservo.attach(11);    //舵机连3引脚
  delay(200);
  myservo.write(45);
  Serial.begin(9600);  //串口通讯设置
}

void loop() 
{
  while(Serial.available())//判断串口是否有值
  { 
    
    var=Serial.read();     //读取串口的值
    Serial.println(var);   //从串口输出var值
    if(var=='s')
      forward();
    else if(var=='w')
      back(); 
    else if(var=='a')
      left();
    else if(var=='d')
      right();
    else if(var=='t')
      stoprun();
    else if(var=='l')            //TO 71
      {
        fromPos = myservo.read(); //底盘当前位置给fromPos
        toPos = 75; 
        if(fromPos<= toPos)
        {
        for(int i=fromPos;i<=toPos;i++)
            {    //b小-大
              myservo.write(i);
              delay(15);
            }
        }
       else
       { 
         for(int i=fromPos;i>=toPos;i--)
          { //b大-小
             myservo.write(i);
             delay(15);
          }
       }
      }
    else if(var=='p')          //TO 30
    {
      fromPos = myservo.read(); //底盘当前位置给fromPos
      toPos = 45; 
      if(fromPos<= toPos)
      {
        for(int i=fromPos;i<=toPos;i++)
        {    //b小-大
          myservo.write(i);
          delay(15);
        }
      }
      else
      { 
        for(int i=fromPos;i>=toPos;i--)
        { //b大-小
        myservo.write(i);
        delay(15);
        }
      }
     }
    else if(var=='r')             //TO 0 
       {fromPos = myservo.read(); //底盘当前位置给fromPos
       toPos = 0; 
       for(int i=fromPos;i>=toPos;i--){ //b大-小
        myservo.write(i);
        delay(15);  }
        }
    
    else if(var=='m') //手动初始化
      {
        fromPos = myservo.read(); //底盘当前位置给fromPos
        toPos = 55; 
      for(int i=fromPos;i<=toPos;i++)   //30-45
      {  myservo.write(i);
         delay(15); 
       }
      //delay(100);
      fromPos = myservo.read();
      toPos = 10;
      for(int i=fromPos;i>=toPos;i--)   //45-10
      { myservo.write(i);
        delay(15); }
      //delay(100);
      fromPos = myservo.read();
      toPos = 55;
      for(int i=fromPos;i<=toPos;i++)   //10-30
      { myservo.write(i);
        delay(15); } 
      //delay(100);
      }
    //delay(500);
  }
}
