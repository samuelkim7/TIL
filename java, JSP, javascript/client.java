import java.net.*;
import java.io.*;
import java.util.*;
class Client{
	public static void main(String args[]){
	try(
		Socket s=new Socket("localhost",7777);
		Scanner sc=new Scanner(System.in);
		OutputStream out=s.getOutputStream();
	){
		while(true){
		String msg=sc.nextLine()+"\n";
		out.write(msg.getBytes());
		if(msg.equals("stop\n")) break;
		}
	}catch(Exception e){
		e.printStackTrace();
	}
}
}