import java.net.*;
import java.io.*;
import java.util.*;
class Server{
	public static void main(String args[]){
	try(
		ServerSocket ss=new ServerSocket(7777);
		Socket s=ss.accept();
		InputStream in=s.getInputStream();
		Scanner sc=new Scanner(in);
	){
		while(true){
		String msg = sc.nextLine();
		System.out.println(msg);
		if(msg.equals("stop")) break;
		}
	}catch(Exception e){
		e.printStackTrace();
	}
}
}
